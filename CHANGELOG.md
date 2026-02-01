## v0.2.0 (2026-02-01)

Initial community version release

### Fix

- **common_base_model**: initialise dict() by default instead of letting it be None
- **pydanticv2**: use ValidationInfo instead of Field
- **pydanticv2**: make optional fields not required
- **prek**: apply ruff, typos and whitespace fixes
- **docs**: remove mkdocs setup in favour of sphinx
- **pydantic**: depreciation warning on class-based config replaced by class attribute `model_config`
- **pydantic**: depreciation warning on _items replaced by_length

### Refactor

- **tests**: use pytest instead of unittest

## v0.1.0 (2025-08-06)

Initial release for `NASA/CR-20250007045`

### Feat

- **models**: establish core aircraft data hierarchy and work breakdown structure,
  including propulsion and performance components
- **propulsion**: add pydantic models plus cycle builder and pyCycle integration for analysis workflows
- **analysis**: support design-point and multipoint analysis scenarios
- **demos**: add propulsion, nacelle, and systems demos with sample outputs and datasets
- **exports**: enable JSON/DaveML save and read-back paths for demos
- **metadata**: add NASA-requested metadata attributes

### Fix

- **propulsion**: fix bleed connections, shaft connections, splitter outputs, and related deck/JSON issues
- **demos**: stabilize demo steps, file naming, and output generation

### Refactor

- **structure**: move demo libraries into demos and clean up scripts/builders
- **cleanup**: simplify project layout and remove unused components
