"""
ADH Performance (Perf) Models.

Performance models describe evaluations of how well the system meets its operational
goals, often using parametric models or performance measures.

The performance child nodes in the [ADH][1] are aligned with
[NASA SP-6105 Systems Engineering Handbook][2]

[1]: https://ntrs.nasa.gov/citations/20250007045
[2]: https://www.nasa.gov/reference/systems-engineering-handbook/

Additional alignment with MIL-F-8785C, MIL-STD-1374, and MIL-STD-881.
"""

from __future__ import annotations

import uuid
from datetime import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field, field_validator

from adh.msosa.source_info import SourceInfo


class PerfDisciplines(str, Enum):
    """
    Taxonomy for performance measures.
    """

    configuration = "configuration"
    """Geometric and layout attributes (e.g., wing area, aspect ratio, OML)."""

    propulsion = "propulsion"
    """Engine performance, thrust, fuel flow, and thermal efficiency."""

    mass_properties = "mass properties"
    """Weight, balance, center of gravity (CG), and moments of inertia."""

    aerodynamics = "aerodynamics"
    """Lift, drag, stability derivatives, and flight envelope performance."""

    signature = "signature"
    """Radar Cross Section (RCS), infrared (IR), acoustic, and visual signatures."""

    finance = "finance"
    """Life cycle cost (LCC), non-recurring engineering (NRE), and unit cost."""

    payloads = "payloads"
    """Sensor performance, weapon integration, and cargo capacity."""

    structures = "structures"
    """Load factors, aeroelasticity, fatigue life, and material stress."""

    systems = "systems"
    """Subsystem performance (Avionics, Hydraulics, Electrical, Environmental)."""

    manufacturing = "manufacturing"
    """Producibility metrics, build rate, and assembly tolerances."""


class DataExchange(BaseModel):
    """The data exchange information of a model or tool."""

    id: str = Field(
        description="The identifier of the model.",
    )
    inputs: Optional[list[Any]] = Field(
        default=None,
        description="The list of input variables to the model.",
    )
    outputs: Optional[list[Any]] = Field(
        default=None,
        description="The list of output variables of the model.",
    )


class ModelDescription(BaseModel):
    """
    The description of a tool or model.
    """

    name: str = Field(
        description="The name of the model.",
    )
    spec_version: Optional[str] = Field(
        default=None,
        description="The specification version of the model.",
    )
    guid: Optional[str] = Field(
        default=None,
        description="The globally unique identifier of the model.",
    )
    generation_tool: Optional[str] = Field(
        default=None,
        description="The tool used to generate the model.",
    )
    generation_time: Optional[datetime] = Field(
        default=None,
        description="The date and time when the model was generated.",
    )
    data_exchange: Optional[DataExchange] = Field(
        default=None,
        description="The data exchange information of the model.",
    )
    license: Optional[str] = Field(
        default=None,
        description="The license of the model.",
    )
    copyright: Optional[str] = Field(
        default=None,
        description="The copyright information of the model.",
    )
    author: Optional[str] = Field(
        default=None,
        description="The author of the model.",
    )
    version: Optional[str] = Field(
        default=None,
        description="The version of the model.",
    )
    description: Optional[str] = Field(
        default=None,
        description="A description of the model.",
    )

    @field_validator("guid")
    def validate_guid(cls, v: str):
        try:
            uuid_obj = uuid.UUID(v, version=4)
            return str(uuid_obj)
        except ValueError as e:
            raise ValueError(
                "Invalid GUID format. Must be a valid UUID version 4"
            ) from e


class Discipline(BaseModel):
    """
    A specific discipline organizing associated tools, models, and methodologies.
    """

    name: PerfDisciplines = Field(
        description="The name of the discipline.",
    )
    description: Optional[str] = Field(
        default=None,
        description="A brief description of the discipline and its scope.",
    )
    tools: Optional[list[ModelDescription]] = Field(
        default=None,
        description="A list of tools and models associated with the discipline.",
    )
    source_info: Optional[SourceInfo] = Field(
        default=None, description="Source and authorship metadata."
    )

    def add_tool(self, tool: ModelDescription) -> None:
        """
        Add a new tool or model to the discipline.

        Args:
            tool: The tool or model being added.
        """
        if self.tools is None:
            self.tools = []
        self.tools.append(tool)


class Performances(BaseModel):
    """Container for a list of performance disciplines."""

    performances: Optional[list[Discipline]] = None
