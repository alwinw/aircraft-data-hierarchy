"""
WBS System model.

Aligned with MIL-STD-881F Work Breakdown Structure taxonomy.
"""

from __future__ import annotations

from typing import Any, Optional

from pydantic import Field

from adh.msosa.architecture import Architecture, MSoSAMixin


class System(MSoSAMixin, Architecture):
    """
    Represents a system within aircraft systems, detailing its specifications, functionalities, and interrelations.

    Attributes:
        name (Optional[str]): The name of the system, acting as a unique identifier.
        description (Optional[str]): A brief description of the system's purpose and functionality.
        parameters (Optional[dict[str, Any]]): Operational or physical parameters associated with the system.
        diagram (Optional[dict[str, Any]]): Flow diagram of the system.
        subsystems (Optional[list[System]]): A list of sub-systems, if any, within this system.
    """

    name: Optional[str] = Field(default=None, description="The name of the system.")
    description: Optional[str] = Field(
        default=None, description="A brief description of the system."
    )
    parameters: Optional[dict[str, Any]] = Field(
        default=None, description="Parameters of the system."
    )
    diagram: Optional[dict[str, Any]] = Field(
        default=None, description="Flow diagram of the system."
    )
    subsystems: Optional[list[System]] = Field(
        default=None, description="Sub-systems within this system."
    )


# Ensure all models are fully defined
System.model_rebuild()
