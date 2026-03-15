"""
WBS Propulsion model.

Aligned with MIL-STD-881F Work Breakdown Structure taxonomy.
"""

from __future__ import annotations

from typing import Any, Optional, Union

from pydantic import Field

from adh.msosa.architecture import Architecture
from adh.msosa.behavior import Behaviors
from adh.msosa.performance import Performances
from adh.msosa.requirements import Requirements
from adh.wbs.propulsion.propulsion_cycle import PropulsionCycle
from adh.wbs.propulsion.propulsion_geometry import PropulsionGeometry
from adh.wbs.propulsion.propulsion_multipoint import MultiPointCycle


class Propulsion(Architecture):
    """
    Represents the propulsion system within an air vehicle system, detailing its specifications, functionalities, and interrelations.

    Attributes:
        name (Optional[str]): The name of the propulsion system, acting as a unique identifier.
        description (Optional[str]): A brief description of the propulsion system purpose and functionality.
        geometry (Optional[PropulsionGeometry]): Geometric information of the propulsion system, if applicable.
        cycle (Optional[PropulsionCycle]): Engine cycle of the propulsion system.
        parameters (Optional[dict[str, Any]]): Cycle or physical parameters associated with the propulsion system.
        subcomponents (Optional[list[Propulsion]]): A list of sub-components, if any, within the propulsion system.
        requirements (Optional[Requirements]): Specific requirements associated with the propulsion system.
        performance (Optional[Performances]): Performance disciplines for the propulsion system.
        behavior (Optional[Behaviors]): Specific behaviors for the propulsion system.
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
    requirements: Optional[Requirements] = Field(
        default=None, description="Specific requirements for the propulsion system."
    )
    performance: Optional[Performances] = Field(
        default=None, description="Performance disciplines for the propulsion system."
    )
    behavior: Optional[Behaviors] = Field(
        default=None, description="Specific behaviors for the propulsion system."
    )


# Ensure all models are fully defined
Propulsion.model_rebuild()
