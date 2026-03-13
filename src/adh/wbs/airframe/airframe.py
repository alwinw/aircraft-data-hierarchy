from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field, field_validator

from adh.msosa.architecture import Architecture, Metadata
from adh.msosa.behavior import Behavior
from adh.msosa.performance import Discipline
from adh.msosa.requirements import Requirement
from adh.wbs.airframe.airframe_geometry import Geometry
from adh.wbs.airframe.airframe_parameters import Parameters


class Component(Architecture):
    """
    Represents a component within an aircraft's system, detailing its specifications, functionalities, and interrelations.

    Attributes:
        name (Optional[str]): The name of the component, acting as a unique identifier.
        description (Optional[str]): A brief description of the component's purpose and functionality.
        geometry (Optional[Geometry]): Geometric information of the component, if applicable.
        parameters (Optional[Parameters]): Operational or physical parameters associated with the component.
        metadata (Optional[Metadata]): Additional metadata providing context or details about the component.
        subcomponents (Optional[List[Component]]): A list of sub-components, if any, within this component.
        requirements (Optional[List[Requirement]]): Specific requirements associated with this component.
        performance (Optional[List[Discipline]]): List of disciplines analyzing the component.
        behavior (Optional[List[Behavior]]): Specific behaviors for the component.

    Raises:
        ValueError: If any string field is empty, ensuring all components have meaningful identifiers and descriptions.
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
    metadata: Optional[Metadata] = Field(
        default=None, description="Additional metadata for the component."
    )
    subcomponents: Optional[list[Component]] = Field(
        default=None, description="Sub-components within this component."
    )
    requirements: Optional[list[Requirement]] = Field(
        default=None, description="Specific requirements for the component."
    )
    performance: Optional[list[Discipline]] = Field(
        default=None, description="List of disciplines analyzing the component."
    )
    behavior: Optional[list[Behavior]] = Field(
        default=None, description="Specific behaviors for the component."
    )

    @field_validator("name", "description", mode="before")
    @classmethod
    def validate_non_empty_string(cls, value: Optional[str]) -> Optional[str]:
        """
        Validates that the name and description fields are not empty or whitespace only.

        Args:
            value (Optional[str]): The value to validate.

        Returns:
            Optional[str]: The validated string value.

        Raises:
            ValueError: If the input value is empty or consists only of whitespace.
        """
        if value is not None and not value.strip():
            raise ValueError(
                "Name and description fields must not be empty or whitespace only."
            )
        return value

    model_config = ConfigDict(arbitrary_types_allowed=True, from_attributes=True)


# Ensure all models are fully defined
Component.model_rebuild()
