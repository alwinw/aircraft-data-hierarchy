"""
WBS Airframe Component model.

Aligned with MIL-STD-881F Work Breakdown Structure taxonomy.
"""

from __future__ import annotations

from typing import Optional

from pydantic import Field

from adh.msosa.architecture import Architecture
from adh.msosa.mixin import MSoSAMixin
from adh.wbs.airframe.airframe_geometry import Geometry
from adh.wbs.airframe.airframe_parameters import Parameters


class Component(MSoSAMixin, Architecture):
    """
    Represents a component within an aircraft's system, detailing its specifications, functionalities, and interrelations.

    Attributes:
        name (Optional[str]): The name of the component, acting as a unique identifier.
        description (Optional[str]): A brief description of the component's purpose and functionality.
        geometry (Optional[Geometry]): Geometric information of the component, if applicable.
        parameters (Optional[Parameters]): Operational or physical parameters associated with the component.
        subcomponents (Optional[list[Component]]): A list of sub-components, if any, within this component.
    """

    name: Optional[str] = Field(default=None, description="The name of the component.")
    description: Optional[str] = Field(
        default=None, description="A brief description of the component."
    )
    geometry: Optional[Geometry] = Field(
        default=None, description="Geometry of the component."
    )
    parameters: Optional[Parameters] = Field(
        default=None, description="Parameters of the component."
    )
    subcomponents: Optional[list[Component]] = Field(
        default=None, description="Sub-components within this component."
    )


# Ensure all models are fully defined
Component.model_rebuild()
