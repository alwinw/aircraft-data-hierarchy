# ADH Theory

> "This parent-child relationship ensures that all analysis, requirements, and behavioral characteristics are derived
> from and traceable to the fundamental architectural definition."[^engelbeck-msosa]

The two core ideas in the Aircraft Data Hierarchy are that the aircraft is a tree, and each meaningful node in that tree
can carry four closely related views.[^engelbeck-central] [^engelbeck-msosa] The papers describe that structure in
theory. The current codebase implements a large part of it already, with a few places where the implementation still
runs ahead or behind the ideal model.

## Start With The Tree

The paper says the ADH should organise aircraft data through a Work Breakdown Structure with "hierarchical levels
representing systems, sub-systems, components".[^engelbeck-wbs] In the repository, that hierarchy shows up directly in
the Python object graph. An `AircraftSystem` contains an `AirVehicle`, which can contain an `Airframe`, which can
contain a `Wing`.[^aircraftsystem-code]

```python
from adh.wbs import AircraftSystem, AirVehicle, Airframe, Wing

aircraft = AircraftSystem(
    name="Example Aircraft",
    air_vehicle=AirVehicle(
        airframe=Airframe(
            wing=Wing(name="Main Wing"),
        ),
    ),
)
```

That object serialises as a nested tree, not as a flat registry with cross-references:

```json
{
  "name": "Example Aircraft",
  "wbs_no": "1.0",
  "air_vehicle": {
    "wbs_no": "1.2",
    "airframe": {
      "wbs_no": "1.2.2",
      "wing": {
        "name": "Main Wing",
        "wbs_no": "1.2.2.3"
      }
    }
  }
}
```

That is the first core idea. ADH is not primarily a catalogue of parts. It is a typed, nested system model following a
schema.

## Then Add The Four Views

The paper defines the recursive MSoSA pattern as "the Architecture view as the parent and Requirements, Performance, and
Behavior as child views".[^engelbeck-msosa] It then says the Architecture view defines "shape, position, and
interfaces", while the child views derive from that parent definition.[^engelbeck-architecture]

In the current code, those views map to the following
models:[^architecture-code] [^requirements-code] [^performance-code] [^behavior-code]

| View         | Paper-first role                                                                  | Current implementation                                                                                          |
| ------------ | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Architecture | Structural definition of the node and its place in the system                     | `Architecture` base model with `name`, `description`, `wbs_no`, and `source_info`                               |
| Requirements | Constraints, intent, verification, and traceability derived from the architecture | `Requirements` container holding `Requirement` items                                                            |
| Performance  | Analysis-facing description of tools, models, and discipline metadata             | `Performances` container holding `Discipline` items                                                             |
| Behavior     | Operational or off-design response of the component                               | `Behaviors` container holding `Behavior` items, including DaveML table fields and an optional activity sequence |

Here is a minimal current-code example using the richer propulsion node, which exposes all three child-view containers
directly:[^propulsion-code]

```python
from adh.msosa.behavior import Behavior, Behaviors
from adh.msosa.performance import Discipline, Performances, PerfDisciplines
from adh.msosa.requirements import Requirement, Requirements
from adh.wbs.propulsion.propulsion import Propulsion

propulsion = Propulsion(
    name="Example Propulsion",
    requirements=Requirements(
        requirements=[Requirement(name="min_thrust")],
    ),
    performance=Performances(
        performances=[Discipline(name=PerfDisciplines.propulsion)],
    ),
    behavior=Behaviors(
        behaviors=[Behavior(name="engine_deck")],
    ),
)
```

```json
{
  "name": "Example Propulsion",
  "requirements": {
    "requirements": [
      {
        "name": "min_thrust"
      }
    ]
  },
  "performance": {
    "performances": [
      {
        "name": "propulsion"
      }
    ]
  },
  "behavior": {
    "behaviors": [
      {
        "name": "engine_deck"
      }
    ]
  }
}
```

## Performance And Behaviour Need Careful Reading

The papers are clear that these two views are not interchangeable. In the propulsion demonstration, the ADH paper says:

> "Behavior Branch: This branch mirrors the architecture branch but contains off-design performance at user-specified
> design conditions."[^engelbeck-prop-behaviour]

And then, separately:

> "Performance Branch: This branch contains a Pydantic tool class that enables the user to specify solver setting
> inputs, outputs and options controlling the pyCycle propulsion analysis."[^engelbeck-prop-performance]

That distinction also shows up in the demo code. `PropulsionCyclePerformance` subclasses `ModelDescription` and stores
analysis setup such as `thermo_method`, `throttle_mode`, and `solver_settings`.[^cycle-performance-code] The helper that
writes an engine deck back into ADH writes DaveML tables into the behaviour branch, not the performance
branch.[^pycycle-to-adh-code] The generated demo JSON shows the same split: `performance` holds the cycle-analysis
configuration, while `behavior.engine_decks` holds the actual engine deck table data.[^step12-json]

So the paper-first reading is:

- `Performance` describes how an analysis tool is configured, identified, or organised.
- `Behavior` carries the resulting response model or off-design data that the rest of the system can consume.

## Current Implementation Notes

The theory is cleaner than the current repository, so it is worth being explicit about the gaps.

First, the paper describes the recursive four-view pattern as universal. In the current codebase, the richer domain base
classes such as `Component`, `Propulsion`, `System`, and `Equipment` expose `requirements`, `performance`, and
`behavior` fields directly.[^component-code][^propulsion-code][^system-code][^equipment-code] Some generated taxonomy
classes such as `Wing` and `Fuselage` in `adh.wbs.air_vehicle` are still lighter `Architecture` subclasses without those
child-view fields on the class itself.[^wing-code]

Second, the current `Behavior` model intentionally carries both an optional activity sequence and the DaveML table
primitives through `TablesMixin`.[^behavior-code][^tables-mixin-code] The propulsion paper discussion emphasises
off-design response tables, while the source model also leaves room for workflow-like activity sequences. The docs in
this section treat the paper definition as normative and call out those implementation details where they matter.

## Where To Go Next

The rest of this section walks the four views one by one:

- [Architecture](architecture.md)
- [Requirements](requirements.md)
- [Performance](performance.md)
- [Behavior](behavior.md)

<!-- markdownlint-disable MD013 -->
[^engelbeck-central]: Engelbeck et al., _Model-Based Systems Analysis and Engineering: Aircraft Data Hierarchy_, NASA/CR-20250007045, Abstract: "The ADH serves as a central repository for aircraft data, ensuring consistency and accuracy across various aspects of aircraft design and analysis."

[^engelbeck-msosa]: Engelbeck et al., NASA/CR-20250007045, Section 10.4: "The ADH aligns with the Model-Based System-of-Systems Architecture (MSoSA) guidelines defined in Figure 12, which defines a hierarchical structure with the Architecture view as the parent and Requirements, Performance, and Behavior as child views."

[^engelbeck-wbs]: Engelbeck et al., NASA/CR-20250007045, Section 10.3: "By breaking down the aircraft and its associated data into hierarchical levels representing systems, sub-systems, components, and even specific data types..."

[^engelbeck-architecture]: Engelbeck et al., NASA/CR-20250007045, Section 10.4: "The Architecture view defines the fundamental characteristics of each component and its relationship with the system and other components, including shape, position, and interfaces."

[^engelbeck-prop-behaviour]: Engelbeck et al., NASA/CR-20250007045, Section 13.4: "Behavior Branch: This branch mirrors the architecture branch but contains off-design performance at user-specified design conditions."

[^engelbeck-prop-performance]: Engelbeck et al., NASA/CR-20250007045, Section 13.4: "Performance Branch: This branch contains a Pydantic tool class that enables the user to specify solver setting inputs, outputs and options controlling the pyCycle propulsion analysis."

[^aircraftsystem-code]: Current implementation: `src/adh/wbs/air_vehicle.py` defines `AircraftSystem`, `AirVehicle`, `Airframe`, and `Wing` as nested WBS nodes with typed child fields.

[^architecture-code]: Current implementation: `src/adh/msosa/architecture.py`.

[^requirements-code]: Current implementation: `src/adh/msosa/requirements.py`.

[^performance-code]: Current implementation: `src/adh/msosa/performance.py`.

[^behavior-code]: Current implementation: `src/adh/msosa/behavior.py`.

[^tables-mixin-code]: Current implementation: `src/adh/tabular/tables.py` defines `TablesMixin` with DaveML fields such as `variable_defs`, `gridded_table_defs`, `ungridded_table_defs`, and `functions`.

[^propulsion-code]: Current implementation: `src/adh/wbs/propulsion/propulsion.py`.

[^component-code]: Current implementation: `src/adh/wbs/airframe/airframe.py`.

[^system-code]: Current implementation: `src/adh/wbs/systems/systems.py`.

[^equipment-code]: Current implementation: `src/adh/wbs/equipment.py`.

[^wing-code]: Current implementation: `src/adh/wbs/air_vehicle.py` defines `Wing` as a direct `Architecture` subclass without explicit `requirements`, `performance`, or `behavior` fields.

[^cycle-performance-code]: Current implementation: `demos/PropulsionDemo/performanceLib/propulsion/propulsion_cycle_performance.py`.

[^pycycle-to-adh-code]: Current implementation: `demos/PropulsionDemo/performanceLib/propulsion/utils/pycycle_to_ADH.py` initialises a `Behavior` with DaveML `functions` and `ungridded_table_defs` before writing engine-deck data.

[^step12-json]: Current implementation: `demos/PropulsionDemo/output_files/step12_adh.json` stores cycle setup under `performance` and engine deck data under `behavior.engine_decks`.
