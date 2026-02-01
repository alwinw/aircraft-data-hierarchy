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
