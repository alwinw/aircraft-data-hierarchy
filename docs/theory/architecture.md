# Architecture

> "The Architecture view defines the fundamental characteristics of each component and its relationship with the system
> and other components, including shape, position, and interfaces."[^engelbeck-architecture]

Architecture is the anchor view in ADH. Before we ask what a thing must do, how well it performs, or how it behaves off
design, we need to say what the thing _is_ and where it sits in the aircraft.[^engelbeck-msosa][^engelbeck-architecture]

## What Architecture Means In ADH

The paper-first model is straightforward. Architecture is the parent view. Requirements, Performance, and Behavior
derive from it and stay traceable back to it.[^engelbeck-msosa] The abstract makes the same point in plainer engineering
language when it says ADH exchanges "geometry definitions, disciplinary tool inputs/outputs, and engineering
requirements" through one central structure.[^engelbeck-abstract]

In the current code, the base `Architecture` model inherits shared node metadata and then adds its WBS identifier.[^architecture-code]

- `name`
- `description`
- `source_info`
- `uuid`
- `wbs_no`

That is a deliberately small core. The richer subclasses add domain content on top of it. For example, `Component` adds
`geometry`, `parameters`, and `subcomponents`; `System` adds `parameters`, `diagram`, and `subsystems`; `Propulsion`
adds `geometry`, `cycle`, and `parameters`.[^component-code][^system-code][^propulsion-code]

## What The Base Model Actually Enforces

The current implementation uses `Architecture` only for true architecture-view nodes in the WBS hierarchy.[^architecture-code]
Two details matter in practice.

First, `wbs_no` is a string, not an integer and not a free-form label. The validator enforces a dotted numeric pattern
such as `1.2.2.3`.[^architecture-code] That keeps the serialised tree aligned with MIL-STD-881-style numbering.

Second, `source_info` sits on the architecture node itself through the shared
node metadata mixin.[^source-info-code] That means the structural definition can
carry authorship, dates, versioning, and external references before any child view appears. It is a pragmatic choice.
Engineers usually know where geometry or configuration data came from long before they know every requirement or every
off-design table.

Third, every remaining architecture node also carries optional `requirements`, `performance`, and `behavior` child
views through `MSoSAMixin`.[^architecture-code] That is the recursive MSoSA rule the cleanup restored across both
hand-maintained and generated WBS nodes.

## Usage Example

The simplest way to see the Architecture view is to instantiate a WBS node that only carries architectural data. A
generated `Wing` node works well for that because, in the current repository, it is a light `Architecture` subclass with
a fixed WBS number.[^wing-code]

```python
from adh.msosa.metadata import Author, SourceInfo
from adh.wbs import Wing

wing = Wing(
    name="Main Wing",
    description="Reference lifting surface for the baseline aircraft",
    source_info=SourceInfo(
        authors=[Author(name="Example Analyst", organisation="ADH Docs")],
        version="0.1.0",
    ),
)
```

```json
{
  "name": "Main Wing",
  "description": "Reference lifting surface for the baseline aircraft",
  "wbs_no": "1.2.2.3",
  "source_info": {
    "authors": [
      {
        "name": "Example Analyst",
        "organisation": "ADH Docs"
      }
    ],
    "version": "0.1.0"
  }
}
```

## Current Implementation Notes

The paper presents Architecture as the universal parent view for every recursive WBS node.[^engelbeck-msosa] The
repository now follows that rule directly: if a class still inherits `Architecture`, it also inherits `MSoSAMixin`.

Generated taxonomy nodes such as `Wing`, `Fuselage`, and `AircraftSystem` express hierarchy, WBS numbering, and the
recursive MSoSA child views.[^aircraftsystem-code][^wing-code] Richer domain classes such as `Component`, `System`,
`Equipment`, and the hand-maintained `Propulsion` class add the fields that make an architecture node useful in
day-to-day modelling.[^component-code][^system-code][^equipment-code][^propulsion-code]

The cleanup also removed several long-standing misuses. Helper geometry models, scalar wrappers, and solver-support
models no longer inherit `Architecture`; they now live as plain supporting models instead.

<!-- markdownlint-disable MD013 -->
[^engelbeck-abstract]: Engelbeck et al., _Model-Based Systems Analysis and Engineering: Aircraft Data Hierarchy_, NASA/CR-20250007045, Abstract: "The ADH facilitates efficient exchange of critical information-geometry definitions, disciplinary tool inputs/outputs, and engineering requirements-through a centralized, validatable data structure..."
[^engelbeck-msosa]: Engelbeck et al., NASA/CR-20250007045, Section 10.4: "The ADH aligns with the Model-Based System-of-Systems Architecture (MSoSA) guidelines defined in Figure 12, which defines a hierarchical structure with the Architecture view as the parent and Requirements, Performance, and Behavior as child views."
[^engelbeck-architecture]: Engelbeck et al., NASA/CR-20250007045, Section 10.4: "The Architecture view defines the fundamental characteristics of each component and its relationship with the system and other components, including shape, position, and interfaces."
[^architecture-code]: Current implementation: `src/adh/msosa/architecture.py`.
[^source-info-code]: Current implementation: `src/adh/msosa/metadata.py`.
[^component-code]: Current implementation: `src/adh/wbs/airframe/airframe.py`.
[^system-code]: Current implementation: `src/adh/wbs/systems/systems.py`.
[^equipment-code]: Current implementation: `src/adh/wbs/equipment.py`.
[^propulsion-code]: Current implementation: `src/adh/wbs/propulsion/propulsion.py`.
[^aircraftsystem-code]: Current implementation: `src/adh/wbs/air_vehicle.py` defines the nested WBS tree for `AircraftSystem`, `AirVehicle`, `Airframe`, and other taxonomy nodes.
[^wing-code]: Current implementation: `src/adh/wbs/air_vehicle.py` defines `Wing` as a direct `Architecture` subclass with `wbs_no="1.2.2.3"`.
