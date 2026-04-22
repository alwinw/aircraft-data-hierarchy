# Requirements

> "The detailed requirements captured in the ADH ensure thorough documentation of the aircraft design, creating a
> comprehensive and reliable resource for design reviews, analysis, and decision-making."[^engelbeck-requirements]

The Requirements view is where ADH stops describing the aircraft as-built and starts describing what the aircraft,
system, or component must satisfy.[^engelbeck-msosa] In the papers, that view supports both communication and
verification. In the current code, it is a compact Pydantic representation of individual requirement records inside a
`Requirements` container.[^requirements-code]

## What The Papers Emphasise

The ADH paper stays fairly high level and focuses on traceability, verification, and the role of requirements in the
digital thread.[^engelbeck-requirements] The MBSE integration paper is more explicit. It says:

> "The Requirements package contains all of the requirements associated with a given
> system/component."[^shi-requirements-package]

It also describes the intended shape of a requirement tree:

> "The requirement architecture should start from the top-level business requirement... When the ACM model is
> incorporated into the main airplane model, the requirement tree becomes complete from the top-level business
> requirement, down to system level, and then to subsystem level, and then finally to the component
> level."[^shi-requirements-tree]

That is the paper-first intent. Requirements are not just checklists. They are supposed to preserve derivation,
regulation, verification, and cross-level traceability.

## What The Current Schema Stores

In the repository today, a `Requirement` stores the fields you need for a practical requirement
record:[^requirements-code]

- `name`
- `description`
- `category`
- `priority`
- `verification_method`
- `status`
- `source`
- `acceptance_criteria`
- `target_component`
- `risk`
- `verification_evidence`
- `source_info`

The schema also constrains several fields through enums. Categories such as `functional`, `performance`, `constraints`,
and `regulatory and compliance` are explicit enum values, not ad hoc strings.[^requirements-code] Verification uses the
four-method set `test`, `analysis`, `inspection`, and `demonstration`.[^requirements-code]

## Usage Example

```python
from adh.msosa.requirements import (
    Priority,
    Requirement,
    Requirements,
    RequirementStatus,
    ReqsCategories,
    VerificationMethod,
)

reqs = Requirements(
    requirements=[
        Requirement(
            name="top_of_climb_thrust",
            description=(
                "The propulsion system shall provide the required net thrust "
                "at top of climb."
            ),
            category=ReqsCategories.performance,
            priority=Priority.high,
            verification_method=VerificationMethod.analysis,
            status=RequirementStatus.approved,
            target_component="propulsion",
            acceptance_criteria=(
                "Net thrust exceeds the sizing threshold at the specified "
                "condition."
            ),
        )
    ]
)
```

```json
{
  "requirements": [
    {
      "name": "top_of_climb_thrust",
      "description": "The propulsion system shall provide the required net thrust at top of climb.",
      "category": "performance",
      "priority": "high",
      "verification_method": "analysis",
      "status": "approved",
      "acceptance_criteria": "Net thrust exceeds the sizing threshold at the specified condition.",
      "target_component": "propulsion"
    }
  ]
}
```

## How To Read This In Practice

If you are modelling with the current code, treat each `Requirement` as a typed requirement record attached to a node.
Use `category`, `verification_method`, and `status` consistently. Those fields are what let downstream tooling filter
the requirement set into something engineers can actually review.

If you are modelling to the paper's fuller intent, keep one extra idea in mind: the requirement record should also sit
inside a derivation story. The MBSE paper expects top-level business requirements to derive system, subsystem, and
component requirements, and then expects analysis to feed verification back into that structure.[^shi-requirements-tree]

## Current Implementation Notes

This is one of the clearer places where the papers describe more than the current core schema implements.

The current `Requirements` model is a flat container of `Requirement` objects.[^requirements-code] It does not yet
encode explicit parent-child requirement relations, requirement-evolution stereotypes, or verification graphs of the
kind described in the Shi paper.[^shi-requirements-tree] That is not a bug in the current model. It just means the
schema currently stores requirement content and verification metadata more directly than the full MBSE metamodel does.

For documentation and examples in this repo, the safest paper-first reading is:

- The `Requirements` view is the place for constraints, intent, and verification metadata associated with a node.
- Cross-level derivation remains part of the intended ADH/MBSE story, even where the standalone Python schema has not
  encoded every relation yet.

<!-- markdownlint-disable MD013 -->
[^engelbeck-msosa]: Engelbeck et al., _Model-Based Systems Analysis and Engineering: Aircraft Data Hierarchy_, NASA/CR-20250007045, Section 10.4: "The ADH aligns with the Model-Based System-of-Systems Architecture (MSoSA) guidelines defined in Figure 12, which defines a hierarchical structure with the Architecture view as the parent and Requirements, Performance, and Behavior as child views."
[^engelbeck-requirements]: Engelbeck et al., NASA/CR-20250007045, Section 11.3: "The detailed requirements captured in the ADH ensure thorough documentation of the aircraft design, creating a comprehensive and reliable resource for design reviews, analysis, and decision-making. This documentation supports rigorous systems engineering processes, providing the traceability and evidence necessary for verification and validation activities."
[^shi-requirements-package]: Shi et al., _Model-Based Systems Analysis and Engineering: The Development of Enhanced MBSA and MBSE Couplings for Practical Applications_, NASA/CR-20250007047, section on ADH import into MagicDraw: "The Requirements package contains all of the requirements associated with a given system/component."
[^shi-requirements-tree]: Shi et al., NASA/CR-20250007047, section on requirement architecture: "The requirement architecture should start from the top-level business requirement... the requirement tree becomes complete from the top-level business requirement, down to system level, and then to subsystem level, and then finally to the component level."
[^requirements-code]: Current implementation: `src/adh/msosa/requirements.py`.
