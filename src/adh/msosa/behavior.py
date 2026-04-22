"""
ADH Behavior (Behv) Models.

Behavior models describe dynamic system interactions, workflows, and system responses to
stimuli across different mission or operational contexts.

The behavioral child nodes in the [ADH][1] are aligned with the
[ANSI/AIAA-S-119-2011 Simulation Model Exchange Format][2] (XML-based DAVE-ML).

[1]: https://ntrs.nasa.gov/citations/20250007045
[2]: https://arc.aiaa.org/doi/10.2514/4.867965.001
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator

from adh.msosa.fidelity import FidelityLevel
from adh.msosa.source_info import SourceInfo
from adh.tabular.tables import TablesMixin


class ActivityState(str, Enum):
    """Lifecycle state of an activity."""

    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"


class Activity(BaseModel):
    """An individual activity or task within a behaviour sequence."""

    name: Optional[str] = Field(
        default=None, description="A unique name identifying the activity."
    )
    description: Optional[str] = Field(
        default=None,
        description="A brief description of the activity's purpose and objectives.",
    )
    state: Optional[ActivityState] = Field(
        default=None, description="The current state of the activity."
    )
    dependencies: Optional[list[str]] = Field(
        default=None,
        description="List of activity names that this activity depends on.",
    )

    @field_validator("name", "description")
    @classmethod
    def validate_non_empty(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not value.strip():
            raise ValueError("Name and description fields must not be empty.")
        return value

    @field_validator("dependencies")
    @classmethod
    def validate_dependency_names(
        cls, value: Optional[list[str]]
    ) -> Optional[list[str]]:
        if value is not None:
            for item in value:
                if not item.strip():
                    raise ValueError(
                        "Dependency names must not be empty or just whitespace."
                    )
        return value


class Behavior(TablesMixin):
    """Behavioural model of a system, combining an activity sequence with DaveML tables."""

    name: Optional[str] = Field(
        default=None, description="A unique name identifying the behaviour."
    )
    description: Optional[str] = Field(
        default=None, description="A brief description of the behaviour."
    )
    sequence: Optional[list[Activity]] = Field(
        default=None, description="A sequence of activities that define the behaviour."
    )
    fidelity_level: Optional[FidelityLevel] = Field(
        default=None,
        description=(
            "Declared analysis fidelity for this behaviour model. "
            "L0 = empirical lookup or simple rule; L1 = parameterised model; "
            "L2 = multi-condition simulation model (e.g. DaveML table set); "
            "L3 = high-fidelity non-linear or time-varying model; "
            "L4 = validated against physical test data."
        ),
    )
    source_info: Optional[SourceInfo] = Field(
        default=None, description="Source and authorship metadata."
    )

    @field_validator("name", "description", mode="before")
    @classmethod
    def validate_non_empty(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not value.strip():
            raise ValueError("Name and description fields must not be empty.")
        return value

    @field_validator("sequence", mode="before")
    @classmethod
    def validate_sequence(
        cls, value: Optional[list[Activity]]
    ) -> Optional[list[Activity]]:
        if value is not None and not value:
            raise ValueError(
                "The behaviour sequence must contain at least one activity."
            )
        return value


class Behaviors(BaseModel):
    """Container for a list of behaviours."""

    behaviors: Optional[list[Behavior]] = None
