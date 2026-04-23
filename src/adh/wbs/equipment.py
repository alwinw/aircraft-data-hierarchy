"""
WBS Equipment model.

Aligned with MIL-STD-881F Work Breakdown Structure taxonomy.
"""

from __future__ import annotations

from typing import Any, Optional

from pydantic import Field

from adh.msosa.architecture import Architecture
from adh.msosa.mixin import MSoSAMixin


class Equipment(MSoSAMixin, Architecture):
    """
    Represents miscellaneous equipment onboard an aircraft required for it's operational use.

    Attributes:
        name (Optional[str]): The name of the equipment, acting as a unique identifier.
        description (Optional[str]): A brief description of the equipment's purpose and functionality.
        geometry (Optional[dict[str, Any]]): Geometric information of the equipment, if applicable.
        parameters (Optional[dict[str, Any]]): Operational or physical parameters associated with the equipment.
        subequipment (Optional[list[Equipment]]): A list of sub-components, if any, within this equipment.
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


# Ensure all models are fully defined
Equipment.model_rebuild()
