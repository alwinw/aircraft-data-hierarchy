"""
WBS Propulsion model.

Aligned with MIL-STD-881F Work Breakdown Structure taxonomy.
"""

from __future__ import annotations

from typing import Any, Optional, Union

from pydantic import Field

from adh.msosa.architecture import Architecture, MSoSAMixin
from adh.wbs.propulsion.propulsion_cycle import PropulsionCycle
from adh.wbs.propulsion.propulsion_geometry import PropulsionGeometry
from adh.wbs.propulsion.propulsion_multipoint import MultiPointCycle


class Propulsion(MSoSAMixin, Architecture):
    """
    Represents the propulsion system within an air vehicle system, detailing its specifications, functionalities, and interrelations.

    Attributes:
        name (Optional[str]): The name of the propulsion system, acting as a unique identifier.
        description (Optional[str]): A brief description of the propulsion system purpose and functionality.
        geometry (Optional[PropulsionGeometry]): Geometric information of the propulsion system, if applicable.
        cycle (Optional[PropulsionCycle]): Engine cycle of the propulsion system.
        parameters (Optional[dict[str, Any]]): Cycle or physical parameters associated with the propulsion system.
        subcomponents (Optional[list[Propulsion]]): A list of sub-components, if any, within the propulsion system.
    """

    name: Optional[str] = Field(
        default=None, description="The name of the propulsion system."
    )
    description: Optional[str] = Field(
        default=None, description="A brief description of the propulsion system."
    )
    geometry: Optional[PropulsionGeometry] = Field(
        default=None, description="Geometry of the propulsion system."
    )
    cycle: Optional[Union[MultiPointCycle, PropulsionCycle]] = Field(
        default=None, description="Cycle of the propulsion system."
    )
    parameters: Optional[dict[str, Any]] = Field(
        default=None, description="Parameters of the propulsion system."
    )
    subcomponents: Optional[list[Propulsion]] = Field(
        default=None, description="Sub-components within the propulsion system."
    )


# Ensure all models are fully defined
Propulsion.model_rebuild()
