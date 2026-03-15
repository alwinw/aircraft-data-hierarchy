"""Generate WBS Python files from scripts/taxonomy/*.yaml files.

Usage:
    uv run python scripts/gen_wbs_classes.py           # write all generated files
    uv run python scripts/gen_wbs_classes.py --check   # verify YAML-derived content is present;
                                                       # extra hand-edited content is allowed
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
WBS_DIR = REPO_ROOT / "src" / "adh" / "wbs"
TAXONOMY_DIR = Path(__file__).parent / "taxonomy"

DOMAIN_STEMS = ["air_vehicle", "payload", "ground_segment", "program_common"]


def load_taxonomy() -> list[dict]:
    """Load all taxonomy YAML files in sorted order; return combined flat entry list."""
    entries: list[dict] = []
    for yaml_file in sorted(TAXONOMY_DIR.glob("*.yaml")):
        with yaml_file.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        if data:
            for entry in data:
                entry["_yaml_stem"] = yaml_file.stem
            entries.extend(data)
    return entries


def _wbs_parts(wbs_no: str) -> list[str]:
    return wbs_no.split(".")


def build_tree(entries: list[dict]) -> dict[str, list[dict]]:
    """Map each wbs_no to its list of direct children (in YAML order).

    Handles the MIL-STD-881F convention where the top-level system uses a ".0"
    suffix (e.g. "1.0"), making "1.1", "1.2" etc. its direct children even though
    the naive prefix "1" does not exist.
    """
    all_nos = {e["wbs_no"] for e in entries}
    children: dict[str, list[dict]] = {e["wbs_no"]: [] for e in entries}

    for entry in entries:
        wbs_no = entry["wbs_no"]
        parts = _wbs_parts(wbs_no)
        parent_no = None

        for length in range(len(parts) - 1, 0, -1):
            candidate = ".".join(parts[:length])
            if candidate in all_nos:
                parent_no = candidate
                break
            # Check if candidate + ".0" exists (root-level ".0" convention)
            candidate_root = candidate + ".0"
            if candidate_root in all_nos and candidate_root != wbs_no:
                parent_no = candidate_root
                break

        if parent_no is not None:
            children[parent_no].append(entry)

    # Sort each child list numerically by wbs_no so field order is deterministic
    for child_list in children.values():
        child_list.sort(key=lambda e: [int(x) for x in e["wbs_no"].split(".")])

    return children


def _derive_field_name(name: str) -> str:
    """Derive a snake_case field name from a WBS entry name.

    Rules (applied in order):
    - Strip parenthetical qualifiers like "(Airframe/Hull/Vehicle)"
    - Strip common trailing patterns that collapse to a fixed token
    - Normalise remaining text to snake_case
    """
    # Strip anything in parentheses - these are qualifier phrases, not the noun
    name = re.sub(r"\s*\(.*?\)", "", name).strip()

    name_lower = name.lower()

    # Trailing "integration, assembly, test and checkout" variants
    for suffix in (
        ", integration, assembly, test and checkout",
        "integration, assembly, test and checkout",
        " integration, assembly, test and checkout",
    ):
        if name_lower.endswith(suffix):
            return "integration"

    if name_lower.endswith("software release"):
        return "software_release"

    if name_lower.startswith("other"):
        return "other"

    # General case: replace slashes, hyphens, commas, ampersands with spaces
    cleaned = re.sub(r"[/\-,&]", " ", name)
    words = cleaned.split()
    return "_".join(w.lower() for w in words if w)


def _deduplicate_field_names(children: list[dict]) -> dict[str, str]:
    """Return {wbs_no: field_name} with collisions resolved by appending last wbs digit."""
    raw: dict[str, str] = {c["wbs_no"]: _derive_field_name(c["name"]) for c in children}
    counts: dict[str, int] = {}
    for name in raw.values():
        counts[name] = counts.get(name, 0) + 1
    result: dict[str, str] = {}
    seen: dict[str, int] = {}
    for wbs_no, field_name in raw.items():
        if counts[field_name] > 1:
            suffix = wbs_no.split(".")[-1]
            result[wbs_no] = f"{field_name}_{suffix}"
        else:
            result[wbs_no] = field_name
    # Guard against residual collisions after suffix append
    final_counts: dict[str, int] = {}
    for name in result.values():
        final_counts[name] = final_counts.get(name, 0) + 1
    for wbs_no, name in list(result.items()):
        if final_counts[name] > 1:
            if name not in seen:
                seen[name] = 0
            seen[name] += 1
            result[wbs_no] = f"{name}_{seen[name]}"
    return result


def _noqa_comment(class_name: str) -> str:
    return "  # noqa: N801" if "_" in class_name else ""


def generate_domain_py(
    stem: str, entries: list[dict], tree: dict[str, list[dict]]
) -> str:
    """Render a self-contained domain file with full class definitions."""
    yaml_path = f"scripts/taxonomy/{stem}.yaml"
    domain_entries = [e for e in entries if e["_yaml_stem"] == stem]

    # Collect cross-stem imports needed by parent classes in this stem
    cross_imports: dict[str, set[str]] = {}
    for entry in domain_entries:
        for child in tree.get(entry["wbs_no"], []):
            if child["_yaml_stem"] != stem:
                cross_imports.setdefault(child["_yaml_stem"], set()).add(
                    child["class_name"]
                )

    lines = f"""# Generated from {yaml_path} by scripts/gen_wbs_classes.py
# Re-run the generator if taxonomy/*.yaml files change.
# Hand edits to this file are preserved across --check runs,
# but class definitions, wbs_no defaults, and child fields will be
# overwritten if the generator is re-run in write mode.

from __future__ import annotations

from typing import Optional

from pydantic import Field
from adh.msosa.architecture import Architecture""".splitlines()

    if cross_imports:
        lines.append("")
        for other_stem in sorted(cross_imports.keys()):
            class_names = sorted(cross_imports[other_stem])
            if len(class_names) == 1:
                lines.append(f"from adh.wbs.{other_stem} import {class_names[0]}")
            else:
                names_str = ",\n    ".join(class_names)
                lines.append(f"from adh.wbs.{other_stem} import (\n    {names_str},\n)")

    lines.append("")
    lines.append("")

    for entry in domain_entries:
        wbs_no = entry["wbs_no"]
        class_name = entry["class_name"]
        name = entry["name"]
        standard_ref = entry["standard_ref"]
        noqa = _noqa_comment(class_name)

        docstring = f"{name}. {standard_ref}. WBS {wbs_no}."
        lines.append(f"class {class_name}(Architecture):{noqa}")
        lines.append(f'    """{docstring}"""')
        lines.append("")
        lines.append(
            f'    wbs_no: str = Field(default="{wbs_no}", description="WBS number per MIL-STD-881F.")'
        )

        child_entries = tree.get(wbs_no, [])
        if child_entries:
            field_map = _deduplicate_field_names(child_entries)
            for child in child_entries:
                child_no = child["wbs_no"]
                child_class = child["class_name"]
                field_name = field_map[child_no]
                lines.append(
                    f"    {field_name}: Optional[{child_class}] = Field(default=None)"
                )

        lines.append("")
        lines.append("")

    # model_rebuild() for classes with child fields, deepest first
    parents_with_children = [e for e in domain_entries if tree.get(e["wbs_no"])]
    parents_with_children.sort(key=lambda e: len(_wbs_parts(e["wbs_no"])), reverse=True)

    if parents_with_children:
        for entry in parents_with_children:
            noqa = _noqa_comment(entry["class_name"])
            lines.append(f"{entry['class_name']}.model_rebuild(){noqa}")
        lines.append("")

    class_names_sorted = sorted(
        (e["class_name"] for e in domain_entries), key=str.casefold
    )
    all_entries_str = '",\n    "'.join(class_names_sorted)
    lines.append(f'__all__ = [\n    "{all_entries_str}",\n]')
    lines.append("")

    source = "\n".join(lines)
    return source.rstrip("\n") + "\n"


def generate_init_py(entries: list[dict]) -> str:
    """Render __init__.py with taxonomy imports from domain files.

    Submodule imports (airframe, propulsion, systems, equipment) and their
    __all__ entries are maintained by hand below the generated section.
    """
    header = (
        "# Taxonomy imports are generated from scripts/taxonomy/*.yaml\n"
        "# Re-run scripts/gen_wbs_classes.py to regenerate.\n"
        "# Submodule imports (airframe, propulsion, systems, equipment) are maintained by hand.\n"
        "from __future__ import annotations\n"
    )

    all_taxonomy_names: list[str] = []
    domain_blocks: list[tuple[str, str]] = []
    for stem in DOMAIN_STEMS:
        domain_entries = [e for e in entries if e["_yaml_stem"] == stem]
        class_names = sorted(
            (e["class_name"] for e in domain_entries), key=str.casefold
        )
        all_taxonomy_names.extend(class_names)
        imports = ",\n    ".join(class_names)
        block = f"from adh.wbs.{stem} import (\n    {imports},\n)"
        domain_blocks.append((stem, block))

    domain_blocks.sort(key=lambda t: t[0].casefold())
    import_section = "\n".join(block for _, block in domain_blocks)

    all_names = sorted(set(all_taxonomy_names), key=str.casefold)
    all_entries_str = '",\n    "'.join(all_names)
    all_section = f'__all__ = [\n    "{all_entries_str}",\n]\n'

    return f"{header}\n{import_section}\n\n{all_section}"


def generate_all(entries: list[dict], tree: dict[str, list[dict]]) -> dict[str, str]:
    """Return mapping of repo-relative path to file content for all generated files."""
    files: dict[str, str] = {}
    for stem in DOMAIN_STEMS:
        files[f"src/adh/wbs/{stem}.py"] = generate_domain_py(stem, entries, tree)
    files["src/adh/wbs/__init__.py"] = generate_init_py(entries)
    return files


def write_all(files: dict[str, str], base: Path) -> None:
    for rel_path, content in files.items():
        target = base / rel_path
        target.write_text(content, encoding="utf-8")
        print(f"Written: {target}")


def _check_domain_py(
    stem: str, entries: list[dict], tree: dict[str, list[dict]], content: str
) -> list[str]:
    """Return list of missing items in a domain file."""
    missing = []
    for entry in (e for e in entries if e["_yaml_stem"] == stem):
        class_name = entry["class_name"]
        wbs_no = entry["wbs_no"]
        if f"class {class_name}(" not in content:
            missing.append(f"class {class_name}(")
        if f'default="{wbs_no}"' not in content:
            missing.append(f'default="{wbs_no}"')
        child_entries = tree.get(wbs_no, [])
        if child_entries:
            field_map = _deduplicate_field_names(child_entries)
            for child in child_entries:
                field_name = field_map[child["wbs_no"]]
                # Check for field prefix only: ruff may wrap long lines so the
                # class name may appear on the next line rather than inline.
                snippet = f"    {field_name}: Optional["
                if snippet not in content:
                    missing.append(snippet)
    return missing


def _check_init_py(entries: list[dict], content: str) -> list[str]:
    """Return list of taxonomy class names missing from __init__.py __all__."""
    return [
        f'    "{e["class_name"]}",  (__all__)'
        for e in entries
        if f'    "{e["class_name"]}",' not in content
    ]


def check_subset(
    files: dict[str, str], base: Path, entries: list[dict], tree: dict[str, list[dict]]
) -> bool:
    """Verify YAML-derived content is present in each file; extra hand-edited content is allowed."""
    all_ok = True
    for rel_path in files:
        target = base / rel_path
        if not target.exists():
            print(f"MISSING FILE: {target}  - run: python scripts/gen_wbs_classes.py")
            all_ok = False
            continue
        content = target.read_text(encoding="utf-8")
        if rel_path == "src/adh/wbs/__init__.py":
            missing = _check_init_py(entries, content)
        else:
            stem = Path(rel_path).stem
            missing = _check_domain_py(stem, entries, tree, content)
        if missing:
            print(f"OUT OF SYNC: {rel_path}")
            for item in missing:
                print(f"  missing: {item}")
            all_ok = False
    return all_ok


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate or check WBS Python files from taxonomy YAML."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check YAML-derived content is present; extra hand-edited content is allowed.",
    )
    args = parser.parse_args()

    entries = load_taxonomy()
    tree = build_tree(entries)
    files = generate_all(entries, tree)

    if args.check:
        ok = check_subset(files, REPO_ROOT, entries, tree)
        if ok:
            print("OK: all YAML-derived WBS content is present.")
        else:
            sys.exit(1)
    else:
        write_all(files, REPO_ROOT)
        print(f"Generated {len(files)} files from {len(entries)} taxonomy entries.")


if __name__ == "__main__":
    main()
