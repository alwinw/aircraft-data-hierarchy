import pytest
from pydantic import ValidationError

from adh.common_base_model import Metadata
from adh.requirements import (
    Requirement,
    Requirements,
)  # Replace 'your_module' with the actual module name


class TestRequirement:
    def test_valid_requirement(self):
        """Test creating a valid Requirement instance."""
        metadata = Metadata(key="example_key", value="example_value")
        req = Requirement(
            name="REQ-001",
            description="This is a test requirement.",
            category="performance",
            priority="high",
            verification_method="test",
            status="open",
            source="customer",
            target_component="component-1",
            acceptance_criteria="Must pass all tests.",
            risk="Low risk",
            verification_evidence="Test report",
            metadata=metadata,
        )
        assert req.name == "REQ-001"
        assert req.description == "This is a test requirement."
        assert req.category == "performance"
        assert req.priority == "high"
        assert req.verification_method == "test"
        assert req.status == "open"
        assert req.source == "customer"
        assert req.target_component == "component-1"
        assert req.acceptance_criteria == "Must pass all tests."
        assert req.risk == "Low risk"
        assert req.verification_evidence == "Test report"
        assert isinstance(req.metadata, Metadata)

    def test_invalid_requirement_empty_fields(self):
        """Test creating a Requirement instance with empty critical fields."""
        with pytest.raises(ValidationError):
            Requirement(
                name="",
                description="",
                priority="",
                verification_method="",
                status="",
                acceptance_criteria="",
            )

    def test_optional_fields(self):
        """Test creating a Requirement instance with optional fields omitted."""
        req = Requirement(
            name="REQ-002",
            description="This is another test requirement.",
            priority="medium",
            verification_method="analysis",
            status="in progress",
            acceptance_criteria="Must meet analysis criteria.",
        )
        assert req.category is None
        assert req.source is None
        assert req.target_component is None
        assert req.risk is None
        assert req.verification_evidence is None
        assert req.metadata is None


class TestRequirements:
    def setup_method(self):
        """Set up a Requirements instance for testing."""
        metadata = Metadata(key="example_key", value="example_value")
        self.requirements = Requirements(
            name="Project Requirements",
            description="A set of project requirements.",
            metadata=metadata,
        )

    def test_add_requirement(self):
        """Test adding a requirement to a category."""
        req = Requirement(
            name="REQ-003",
            description="A new requirement.",
            priority="low",
            verification_method="inspection",
            status="open",
            acceptance_criteria="Must pass inspection.",
        )
        self.requirements.add_requirement(req, "safety")
        assert "safety" in self.requirements.requirements
        assert len(self.requirements.requirements["safety"]) == 1
        assert self.requirements.requirements["safety"][0].name == "REQ-003"

    def test_remove_requirement(self):
        """Test removing a requirement from a category."""
        req = Requirement(
            name="REQ-004",
            description="Another new requirement.",
            priority="medium",
            verification_method="test",
            status="open",
            acceptance_criteria="Must pass all tests.",
        )
        self.requirements.add_requirement(req, "performance")
        self.requirements.remove_requirement("REQ-004", "performance")
        assert "REQ-004" not in [
            r.name for r in self.requirements.requirements["performance"]
        ]

    def test_remove_nonexistent_requirement(self):
        """Test removing a non-existent requirement."""
        with pytest.raises(ValueError):
            self.requirements.remove_requirement("REQ-999", "performance")

    def test_get_requirements_by_category(self):
        """Test retrieving requirements by category."""
        req1 = Requirement(
            name="REQ-005",
            description="Requirement 1.",
            priority="high",
            verification_method="test",
            status="open",
            acceptance_criteria="Must pass all tests.",
        )
        req2 = Requirement(
            name="REQ-006",
            description="Requirement 2.",
            priority="medium",
            verification_method="analysis",
            status="in progress",
            acceptance_criteria="Must meet analysis criteria.",
        )
        self.requirements.add_requirement(req1, "design")
        self.requirements.add_requirement(req2, "design")
        design_reqs = self.requirements.get_requirements_by_category("design")
        assert len(design_reqs) == 2
        assert design_reqs[0].name == "REQ-005"
        assert design_reqs[1].name == "REQ-006"

    def test_get_requirements_by_nonexistent_category(self):
        """Test retrieving requirements from a non-existent category."""
        with pytest.raises(ValueError):
            self.requirements.get_requirements_by_category("nonexistent")
