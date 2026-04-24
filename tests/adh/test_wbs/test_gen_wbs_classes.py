from __future__ import annotations

import importlib.util
from pathlib import Path

_MODULE_PATH = Path(__file__).resolve().parents[3] / "scripts" / "gen_wbs_classes.py"
_SPEC = importlib.util.spec_from_file_location("gen_wbs_classes", _MODULE_PATH)
assert _SPEC is not None
assert _SPEC.loader is not None
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)
generate_init_py = _MODULE.generate_init_py


def test_generate_init_py_preserves_hand_maintained_exports():
    entries = [
        {"_yaml_stem": "air_vehicle", "class_name": "AirVehicle"},
        {"_yaml_stem": "payload", "class_name": "PayloadMissionSystem"},
        {"_yaml_stem": "ground_segment", "class_name": "GroundHostSegment"},
        {"_yaml_stem": "program_common", "class_name": "ProgramManagement"},
    ]
    existing_content = """# Taxonomy imports are generated from scripts/taxonomy/*.yaml
# Re-run scripts/gen_wbs_classes.py to regenerate.
# Submodule imports (airframe, propulsion, systems, equipment) are maintained by hand.
from __future__ import annotations

from adh.wbs.airframe import (
    Component,
)
from adh.wbs.equipment import Equipment
from adh.wbs.propulsion import (
    PropulsionCycle,
)
from adh.wbs.systems import (
    System,
)

__all__ = [
    "AirVehicle",
    "GroundHostSegment",
    "PayloadMissionSystem",
    "ProgramManagement",
    "Component",
    "Equipment",
    "PropulsionCycle",
    "System",
]
"""

    rendered = generate_init_py(entries, existing_content)

    assert "from adh.wbs.airframe import (\n    Component,\n)" in rendered
    assert "from adh.wbs.equipment import Equipment" in rendered
    assert "from adh.wbs.propulsion import (\n    PropulsionCycle,\n)" in rendered
    assert "from adh.wbs.systems import (\n    System,\n)" in rendered
    assert '    "Component",' in rendered
    assert '    "Equipment",' in rendered
    assert '    "PropulsionCycle",' in rendered
    assert '    "System",' in rendered
