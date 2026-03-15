"""
WBS Equipment model.

Aligned with MIL-STD-881F Work Breakdown Structure taxonomy.
"""

from __future__ import annotations

from typing import Any, Optional

from pydantic import Field

from adh.msosa.architecture import Architecture
from adh.msosa.behavior import Behaviors
from adh.msosa.performance import Performances
from adh.msosa.requirements import Requirements


class Equipment(Architecture):
    """
    Represents miscellaneous equipment onboard an aircraft required for it's operational use.

    Attributes:
        name (Optional[str]): The name of the equipment, acting as a unique identifier.
        description (Optional[str]): A brief description of the equipment's purpose and functionality.
        geometry (Optional[dict[str, Any]]): Geometric information of the equipment, if applicable.
        parameters (Optional[dict[str, Any]]): Operational or physical parameters associated with the equipment.
        subequipment (Optional[list[Equipment]]): A list of sub-components, if any, within this equipment.
        requirements (Optional[Requirements]): Specific requirements associated with this equipment.
        performance (Optional[Performances]): Performance disciplines for the equipment.
        behavior (Optional[Behaviors]): Specific behaviors for the equipment.
    """

    name: Optional[str] = Field(default=None, description="The name of the equipment.")
    description: Optional[str] = Field(
        default=None, description="A brief description of the equipment."
    )
    geometry: Optional[dict[str, Any]] = Field(
        default=None, description="Geometry of the equipment."
    )
    parameters: Optional[dict[str, Any]] = Field(
        default=None, description="Parameters of the equipment."
    )
    subequipment: Optional[list[Equipment]] = Field(
        default=None, description="Sub-equipment within this equipment."
    )
    requirements: Optional[Requirements] = Field(
        default=None, description="Specific requirements for the equipment."
    )
    performance: Optional[Performances] = Field(
        default=None, description="Performance disciplines for the equipment."
    )
    behavior: Optional[Behaviors] = Field(
        default=None, description="Specific behaviors for the equipment."
    )


# Ensure all models are fully defined
Equipment.model_rebuild()
