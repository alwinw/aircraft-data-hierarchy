# Aircraft Data Hierarchy

<!-- TODO: create logo where the [A] is includes the bottom of the branch. i.e. /\ and |--| -->

```txt
   [A]
 ┌──┴──┐
[D]   [H]
```

> _A Model-Based Systems Analysis & Engineering (MBSA&E) Framework for Standardised Aerospace Data Exchange_

Based on [NASA/CR-20250007045](https://ntrs.nasa.gov/citations/20250007045)

## Overview

The Aircraft Data Hierarchy (ADH) is an open, standards-aligned, model-based data framework designed to unify
Model-Based Systems Engineering (MBSE) and Model-Based Systems Analysis (MBSA). It provides a centralised,
authoritative, and validatable structure for representing aircraft architecture, requirements, performance, and
behavior.

The ADH addresses long-standing aerospace challenges: fragmented data, tool-specific silos, inconsistent
representations, and inefficient cross-disciplinary integration. By defining a recursive, hierarchical,
standards-aligned schema, the ADH enables seamless data exchange across engineering disciplines, tools, and
organisations.

## Key Features

- Standards-Aligned Architecture

    Built on MSoSA, MIL-STD-881F, SAWE RP A-8, and ANSI/AIAA-S-119-2011.

- Unified MBSE + MBSA Data Model

    A recursive structure linking Architecture → Requirements → Performance → Behavior.

- Centralised Authoritative Data Source

    Eliminates duplication, reduces interfaces, and supports digital thread continuity.

- Modern Python Implementation

    Implemented using Pydantic v2 with built-in validation and multi-format serialisation (JSON, YAML, XML).

- Flexible & Extensible

    Supports diverse aircraft configurations, fidelity levels, and evolving design methodologies.

- Interoperable by Design

    Vendor-neutral, open-source, and demonstrated compatibility with NASA's MBSA&E framework, OpenMDAO, Aviary, and MBSE
    tools such as MagicDraw/Cameo.

## Architecture

The ADH is organised into:

- Work Breakdown Structure (WBS)

    - Based on MIL-STD-881F, adapted for aircraft systems.
    - Provides the top-level decomposition of the air vehicle.

- Model-Based System-of-Systems Architecture (MSoSA)

    Each WBS element contains four recursive views:

    | View         | Purpose                                       |
    | ------------ | --------------------------------------------- |
    | Architecture | Geometry, topology, interfaces, configuration |
    | Requirements | Constraints, standards, verification criteria |
    | Performance  | Quantitative metrics, analysis results        |
    | Behavior     | Dynamic, logical, and functional behavior     |

- Principle of Similar Treatment

    Similar components (e.g., lifting surfaces, axial bodies, propulsion elements) share consistent data structures.

- Dictionary of Aliases

    Short, human-friendly paths for accessing deeply nested data objects.

The source code is organised into: <!-- Edited output of `tree` command below -->

```md
.
├── src
│   └── adh
│       ├── core
│       │   │   # custom pydantic base models based on MSoSA
│       │   ├── architecture.py
│       │   ├── requirements.py
│       │   ├── performance.py
│       │   ├── behavior.py
│       │   └── units.py
│       └── wbs
│           │   # data objects
│           ├── airframe
│           ├── propulsion
│           ├── systems
│           └── equipment
└── tests
    ├── unit
    │   ├── test_core
    │   └── test_wbs
    └── functional
```

## ADH File Format

```json
{
  "aircraft_system": {
    "wbs_no": "1.0",
    "metadata": {
      // name, description, creation info, version, etc.
    },
    "architecture": {
      // parameters;
      // geometry
    },
    "requirements": {
      // name and text; or
      // name, description and value
    },
    "performance": {
      // discipline and parameters
    },
    "behavior": {
      //
    }
  }
}
```

## Citation

> Engelbeck, R. M., Ocampo, E., Gablonsky, J., Shi, M., Wakayama, S., Carrere, A., Plybon, R., Refford, M., Mokotoff,
> P., Bakhshi, S., Kerlee, A., Cinar, G., & Martins, J. (2025). _Model-Based Systems Analysis and Engineering: Aircraft
> Data Hierarchy_ (NASA/CR-20250007045). <https://ntrs.nasa.gov/citations/20250007045>

```bibtex
@report{engelbeckModelBasedSystemsAnalysis2025,
  title = {Model-{{Based Systems Analysis}} and {{Engineering}}: {{Aircraft Data Hierarchy}}},
  shorttitle = {{{MBSA}}\&{{E}}: {{ADH}}},
  author = {Engelbeck, Ranald M. and Ocampo, Eduardo and Gablonsky, Joerg and Shi, Mingxuan and Wakayama, Sean and Carrere, Alexander and Plybon, Ronald and Refford, Melinda and Mokotoff, Paul and Bakhshi, Safa and Kerlee, Alex and Cinar, Gokcin and Martins, Joaquim},
  date = {2025-08-01},
  number = {NASA/CR-20250007045},
  url = {https://ntrs.nasa.gov/citations/20250007045},
  keywords = {ADH},
}
```
