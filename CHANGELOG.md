## v0.3.0 (2026-03-18)

### Feat

- **propulsion**: fix PropulsionDemo JSON round-trip via MultiPointCycle
- **msosa**: add Performances container and export perf types
- **wbs**: add MIL-STD-881F taxonomy YAML and generator script
- **msosa**: implement Behavior model with DaveML document classes
- **tabular**: extract DaveML table primitives
- **msosa**: complete Requirements model with enums and container
- **msosa**: implement Architecture base class
- **core**: add pint units support

### Fix

- **demos/PropulsionDemo**: migrate imports to current adh package paths
- **demos**: migrate NacelleDemo notebook to adh package and pydantic v2
- **demos**: update NacelleDemo fixture to MIL-STD-881F WBS
- **msosa**: strengthen Architecture model_config
- **python**: remove end-of-life python 3.8 support
- **ruff**: address ruff lint errors

### Refactor

- **wbs**: rename systems_parameters.Systems to SystemRecord
- **wbs**: adopt Requirements/Performances/Behaviors containers in leaf models
- **wbs**: collapse _generated.py into domain files
- **wbs**: replace work_breakdown_structure with generated domain modules
- **msosa**: SourceInfo model for authorship and metadata management based on DAVE-ML
- **wbs**: replace CommonBaseModel with Architecture
- **adh**: make __init__.py intentionally minimal
- **msosa**: move and restructure architecture, behavior and requirements.py into msosa module
- **msosa**: move performance into msosa and add enum of disciplines
- **geom**: move units from msosa to geom module
- **ruff**: remove relative imports
- **adh**: shorten names to adh and wbs
- **systems_diagrams**: lazy load libraries required for diagrams as optional extras

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
