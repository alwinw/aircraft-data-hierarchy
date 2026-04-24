# Performance

> "Performance Branch: This branch contains a Pydantic tool class that enables the user to specify solver setting
> inputs, outputs and options controlling the pyCycle propulsion analysis."[^engelbeck-prop-performance]

Performance in ADH is easy to misread if you come in expecting it to hold every numeric result. The papers use it more
narrowly. Performance is the analysis-facing view: the place where ADH records the discipline, tool, interface, and
configuration that drive an analysis.[^engelbeck-prop-performance][^engelbeck-abstract]

## What The Papers Mean By Performance

The ADH paper introduces ADH as a way to exchange "disciplinary tool inputs/outputs" alongside geometry and
requirements.[^engelbeck-abstract] That is still broad enough to be fuzzy. The propulsion demonstration is the clearer
guide because it separates the branches explicitly.

The performance branch, in that demo, is not the engine deck itself. It is the tool-side description of the pyCycle
analysis: inputs, outputs, options, and solver settings.[^engelbeck-prop-performance] The off-design response data then
lands in the behaviour branch instead.[^engelbeck-prop-behaviour]

That distinction matters well beyond propulsion. A useful mental model is:

- `Performance` describes the analysis setup and discipline context.
- `Behavior` carries the resulting response model when that response needs to be stored as reusable data.

## What The Core Schema Stores

In the current core MSoSA schema, the Performance view is modelled as a `Performances` container holding one or more
`Discipline` records.[^performance-code]

Each `Discipline` stores:[^performance-code]

- `name`: the discipline enum value, such as `propulsion` or `aerodynamics`
- `description`: a short statement of scope
- `tools`: one or more `ModelDescription` records
- `fidelity_level`: the declared analysis level in the current codebase
- `source_info`: authorship and provenance metadata

Each `ModelDescription` then carries the tool or model metadata, including `name`, `version`, `uuid`, `generation_time`,
and a `DataExchange` object with declared `inputs` and `outputs`.[^performance-code]

## Usage Example

```python
from adh.msosa.metadata import FidelityLevel
from adh.msosa.performance import (
    DataExchange,
    Discipline,
    ModelDescription,
    PerfDisciplines,
    Performances,
)

perf = Performances(
    performances=[
        Discipline(
            name=PerfDisciplines.propulsion,
            description="Zero-dimensional propulsion cycle analysis.",
            fidelity_level=FidelityLevel.layout,
            tools=[
                ModelDescription(
                    name="pyCycle",
                    version="4.2.0",
                    data_exchange=DataExchange(
                        id="pycycle-cycle",
                        inputs=["flight_conditions", "cycle_parameters"],
                        outputs=["thrust", "fuel_flow"],
                    ),
                )
            ],
        )
    ]
)
```

```json
{
  "performances": [
    {
      "name": "propulsion",
      "description": "Zero-dimensional propulsion cycle analysis.",
      "tools": [
        {
          "name": "pyCycle",
          "data_exchange": {
            "id": "pycycle-cycle",
            "inputs": [
              "flight_conditions",
              "cycle_parameters"
            ],
            "outputs": [
              "thrust",
              "fuel_flow"
            ]
          },
          "version": "4.2.0"
        }
      ],
      "fidelity_level": "L1"
    }
  ]
}
```

## Current Implementation Notes

There are two layers to know here.

First, the core schema uses `Performances -> Discipline -> ModelDescription`.[^performance-code] That is the
general-purpose representation used by the main ADH source tree.

Second, the propulsion demo uses a more specialised pattern. `PropulsionDemo` subclasses `Propulsion` and narrows
`performance` to a demo-local `PropulsionCyclePerformance` type, which itself subclasses `ModelDescription` and adds
propulsion-specific fields such as `thermo_method`, `throttle_mode`, and
`solver_settings`.[^propulsion-demo-code][^cycle-performance-code]

That means the demos do not only _use_ the performance idea. They specialise it for a particular solver workflow. For
this documentation, the core `Performances` schema is the canonical API, and the propulsion demo is the concrete worked
example that shows how a discipline-specific tool model can extend `ModelDescription`.

## Fidelity In The Current Code

The `fidelity_level` field is a current implementation detail, not something the ADH papers define
directly.[^fidelity-code] It uses the enum values `L0` through `L4` and appears on `Discipline` so a performance record
can declare the analysis approach that produced or governs it.[^performance-code][^fidelity-code]

That is useful in practice, especially when the same discipline exists at several levels of detail, but it should be
read as code-level evolution rather than as original paper terminology.

<!-- markdownlint-disable MD013 -->
[^engelbeck-abstract]: Engelbeck et al., _Model-Based Systems Analysis and Engineering: Aircraft Data Hierarchy_, NASA/CR-20250007045, Abstract: "The ADH facilitates efficient exchange of critical information-geometry definitions, disciplinary tool inputs/outputs, and engineering requirements-through a centralized, validatable data structure..."
[^engelbeck-prop-performance]: Engelbeck et al., NASA/CR-20250007045, Section 13.4: "Performance Branch: This branch contains a Pydantic tool class that enables the user to specify solver setting inputs, outputs and options controlling the pyCycle propulsion analysis."
[^engelbeck-prop-behaviour]: Engelbeck et al., NASA/CR-20250007045, Section 13.4: "Behavior Branch: This branch mirrors the architecture branch but contains off-design performance at user-specified design conditions."
[^performance-code]: Current implementation: `src/adh/msosa/performance.py`.
[^fidelity-code]: Current implementation: `src/adh/msosa/metadata.py`.
[^propulsion-demo-code]: Current implementation: `demos/PropulsionDemo/utils/generate_demo_adh.py` defines `PropulsionDemo` with `performance: Optional[PropulsionCyclePerformance]`.
[^cycle-performance-code]: Current implementation: `demos/PropulsionDemo/performanceLib/propulsion/propulsion_cycle_performance.py`.
