# Behavior

> "Behavior Branch: This branch mirrors the architecture branch but contains off-design performance at user-specified
> design conditions."[^engelbeck-prop-behaviour]

Behavior is the most overloaded word in this part of the repo, so it is worth slowing down. In the papers, the clearest
concrete meaning comes from the propulsion demo: Behaviour holds the off-design response model that analysis produces
and that other tools can consume later.[^engelbeck-prop-behaviour]

## What The Papers Mean By Behavior

The propulsion section of the ADH paper defines the branch in operational terms: it mirrors the architecture branch, but
it stores off-design response data for user-specified conditions.[^engelbeck-prop-behaviour] A few paragraphs later, the
same section makes the storage format explicit:

> "The DaveML format has been integrated with the Pydantic class structure to represent the DaveML standard. The engine
> deck is generated using the DaveML Pydantic classes in the ADH library, specifically following the
> ANSI/AIAA-S-119-2011 specification."[^engelbeck-daveml]

That is the paper-first centre of gravity. Behaviour is not just a vague bag of dynamic facts. It is the place where
reusable behavioural response data, especially off-design data, gets stored in a standardised form.

## What The Current Schema Stores

The core `Behavior` model subclasses `TablesMixin`, so it can carry DaveML table primitives
directly.[^behavior-code][^tables-mixin-code] That includes:

- `variable_defs`
- `breakpoint_defs`
- `gridded_table_defs`
- `ungridded_table_defs`
- `functions`
- `check_data`

On top of those table fields, the current model also adds:

- `name`
- `description`
- `sequence`
- `fidelity_level`
- `source_info`

This is the main implementation wrinkle on the page. The paper emphasises off-design response data. The current code
keeps that meaning, but it also allows an optional activity sequence alongside the DaveML content.[^behavior-code]

## Usage Example

```python
from adh.msosa.behavior import Activity, ActivityState, Behavior, Behaviors
from adh.msosa.metadata import FidelityLevel
from adh.tabular.tables import DataPoint, UngriddedTableDef, VariableDef

behaviors = Behaviors(
    behaviors=[
        Behavior(
            name="engine_deck",
            description="Off-design propulsion response represented as an ungridded table.",
            fidelity_level=FidelityLevel.layout,
            sequence=[
                Activity(
                    name="populate_engine_deck",
                    description="Load the off-design response data into the behaviour model.",
                    state=ActivityState.completed,
                )
            ],
            variable_defs=[
                VariableDef(var_id="mn", units="unitless"),
                VariableDef(var_id="alt", units="ft"),
                VariableDef(var_id="net_thrust", units="lbf", is_output=True),
            ],
            ungridded_table_defs=[
                UngriddedTableDef(
                    name="Engine Deck Data",
                    units="unitless, ft, lbf",
                    data_point=[
                        DataPoint(value="0.80 35000 5900"),
                        DataPoint(value="0.40 20000 9906"),
                    ],
                )
            ],
        )
    ]
)
```

```json
{
  "behaviors": [
    {
      "variable_defs": [
        {
          "var_id": "mn",
          "units": "unitless"
        },
        {
          "var_id": "alt",
          "units": "ft"
        },
        {
          "var_id": "net_thrust",
          "units": "lbf",
          "is_output": true
        }
      ],
      "ungridded_table_defs": [
        {
          "name": "Engine Deck Data",
          "units": "unitless, ft, lbf",
          "data_point": [
            {
              "value": "0.80 35000 5900"
            },
            {
              "value": "0.40 20000 9906"
            }
          ]
        }
      ],
      "name": "engine_deck",
      "description": "Off-design propulsion response represented as an ungridded table.",
      "sequence": [
        {
          "name": "populate_engine_deck",
          "description": "Load the off-design response data into the behaviour model.",
          "state": "completed"
        }
      ],
      "fidelity_level": "L1"
    }
  ]
}
```

## What The Propulsion Demo Shows

The propulsion demo remains the most concrete example in the repository. After running pyCycle, the helper code
initialises a `Behavior` object with DaveML `functions` and `ungridded_table_defs`, then appends table data points into
that structure.[^pycycle-to-adh-code] The generated JSON in `step12_adh.json` stores the engine deck under
`behavior.engine_decks`, and those engine decks contain DaveML-style ungridded table rows.[^step12-json]

That is strong evidence for the intended use of the branch: Behaviour is where the component's reusable response model
lives after the solver runs.

## Current Implementation Notes

The current core `Behavior` API is slightly broader than the paper language suggests.

It does store DaveML response data directly, which matches the paper and the propulsion
demo.[^engelbeck-daveml][^pycycle-to-adh-code] But it also stores an optional activity sequence with names, states, and
dependencies.[^behavior-code] That means the current implementation can describe both the behavioural artefact and a
lightweight process around it.

The propulsion demo broadens things a little further. Its demo-local `PropulsionCycleBehavior` adds
`flight_conditions_design`, `performance_components`, and `engine_decks` on top of the base `Behavior`
model.[^propulsion-cycle-behavior-code] Those fields are useful for the demo, but they are not the same thing as the
generic `Behavior` API in `src/adh/msosa/behavior.py`.

For this documentation, the safest interpretation is:

- Paper-first ADH: `Behavior` is the off-design or operational response model tied to a node.
- Current core schema: `Behavior` is that response model plus optional activity-sequence metadata.
- Demo-specific propulsion code: `Behavior` is further specialised to support the pyCycle-to-DaveML workflow.

<!-- markdownlint-disable MD013 -->
[^engelbeck-prop-behaviour]: Engelbeck et al., _Model-Based Systems Analysis and Engineering: Aircraft Data Hierarchy_, NASA/CR-20250007045, Section 13.4: "Behavior Branch: This branch mirrors the architecture branch but contains off-design performance at user-specified design conditions."
[^engelbeck-daveml]: Engelbeck et al., NASA/CR-20250007045, Section 13.4: "The DaveML format has been integrated with the Pydantic class structure to represent the DaveML standard. The engine deck is generated using the DaveML Pydantic classes in the ADH library, specifically following the ANSI/AIAA-S-119-2011 specification."
[^behavior-code]: Current implementation: `src/adh/msosa/behavior.py`.
[^tables-mixin-code]: Current implementation: `src/adh/tabular/tables.py` defines `TablesMixin` and the DaveML table primitives.
[^pycycle-to-adh-code]: Current implementation: `demos/PropulsionDemo/performanceLib/propulsion/utils/pycycle_to_ADH.py` initialises a `Behavior` with DaveML structures before writing engine-deck data.
[^step12-json]: Current implementation: `demos/PropulsionDemo/output_files/step12_adh.json` stores propulsion engine decks under `behavior.engine_decks` as ungridded DaveML-style tables.
[^propulsion-cycle-behavior-code]: Current implementation: `demos/PropulsionDemo/behaviorLib/propulsion/propulsion_cycle_behavior.py`.
