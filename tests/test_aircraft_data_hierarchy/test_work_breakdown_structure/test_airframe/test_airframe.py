import pytest
from pydantic import ValidationError

from aircraft_data_hierarchy.behavior import Behavior
from aircraft_data_hierarchy.common_base_model import Metadata
from aircraft_data_hierarchy.performance import Discipline
from aircraft_data_hierarchy.requirements import Requirement
from aircraft_data_hierarchy.work_breakdown_structure.airframe import Component


class TestComponent:
    """Unit tests for the Component class."""

    def test_component_creation(self):
        """
        Test creating a Component with all fields provided.
        """
        metadata = Metadata(key="example_key", value="example_value")
        component = Component(
            name="Engine",
            description="Main engine component",
            requirements=[
                Requirement(
                    name="Req1",
                    description="Requirement 1",
                    priority="High",
                    verification_method="Test",
                    status="Open",
                    acceptance_criteria="Criteria 1",
                )
            ],
            subcomponents=[],
            metadata=metadata,
            performance=[
                Discipline(name="Performance1", description="Performance description")
            ],
            behavior=[Behavior(name="Behavior1", description="Behavior description")],
        )
        assert component.name == "Engine"
        assert component.description == "Main engine component"
        assert component.metadata == metadata
        assert component.requirements is not None
        assert len(component.requirements) == 1
        assert component.subcomponents == []
        assert component.performance is not None
        assert len(component.performance) == 1
        assert component.behavior is not None
        assert len(component.behavior) == 1

    def test_default_values(self):
        """
        Test that default values are set correctly.
        """
        component = Component()
        assert component.name is None
        assert component.description is None
        assert component.requirements is None
        assert component.subcomponents is None
        assert component.geometry is None
        assert component.parameters is None
        assert component.metadata is None
        assert component.performance is None
        assert component.behavior is None

    def test_non_empty_validation(self):
        """
        Test that name and description fields must not be empty or whitespace only.
        """
        with pytest.raises(ValidationError):
            Component(name=" ", description="Valid description")
        with pytest.raises(ValidationError):
            Component(name="Valid name", description=" ")

    def test_optional_fields(self):
        """
        Test that optional fields can be omitted.
        """
        component = Component(name="Engine", description="Main engine component")
        assert component.name == "Engine"
        assert component.description == "Main engine component"
        assert component.requirements is None
        assert component.subcomponents is None
        assert component.geometry is None
        assert component.parameters is None
        assert component.metadata is None
        assert component.performance is None
        assert component.behavior is None

    def test_recursive_subcomponents(self):
        """
        Test that subcomponents can be nested within a component.
        """
        subcomponent = Component(name="SubEngine", description="Sub engine component")
        component = Component(
            name="Engine",
            description="Main engine component",
            subcomponents=[subcomponent],
        )
        assert component.subcomponents is not None
        assert len(component.subcomponents) == 1
        assert component.subcomponents[0].name == "SubEngine"
        assert component.subcomponents[0].description == "Sub engine component"
