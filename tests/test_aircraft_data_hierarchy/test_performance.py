import uuid
from datetime import datetime

import pytest
from pydantic import ValidationError

from aircraft_data_hierarchy.common_base_model import Metadata
from aircraft_data_hierarchy.performance import (
    DataExchange,
    Discipline,
    ModelDescription,
)


class TestModels:
    def test_data_exchange_creation(self):
        data_exchange = DataExchange(
            model_identifier="model_123",
            inputs=["input1", "input2"],
            outputs=["output1"],
        )
        assert data_exchange.model_identifier == "model_123"
        assert data_exchange.inputs == ["input1", "input2"]
        assert data_exchange.outputs == ["output1"]

    def test_data_exchange_optional_fields(self):
        data_exchange = DataExchange()
        assert data_exchange.model_identifier is None
        assert data_exchange.inputs == []
        assert data_exchange.outputs == []

    def test_model_description_creation(self):
        data_exchange = DataExchange(
            model_identifier="model_123",
            inputs=["input1", "input2"],
            outputs=["output1"],
        )
        model_description = ModelDescription(
            specification_version="2.0",
            model_name="Test Model",
            guid=str(uuid.uuid4()),
            generation_tool="Tool XYZ",
            generation_date_and_time=datetime.now(),
            data_exchange=data_exchange,
            license="MIT",
            copyright="NASA",
            author="John Doe",
            version="1.0",
            description="A test model",
        )
        assert model_description.specification_version == "2.0"
        assert model_description.model_name == "Test Model"
        assert model_description.data_exchange == data_exchange

    def test_model_description_optional_fields(self):
        model_description = ModelDescription()
        assert model_description.specification_version is None
        assert model_description.model_name is None
        assert model_description.guid is None
        assert model_description.generation_tool is None
        assert model_description.generation_date_and_time is None
        assert model_description.data_exchange is None
        assert model_description.license is None
        assert model_description.copyright is None
        assert model_description.author is None
        assert model_description.version is None
        assert model_description.description is None

    def test_model_description_invalid_specification_version(self):
        with pytest.raises(ValidationError):
            ModelDescription(specification_version="1.0")

    def test_model_description_invalid_guid(self):
        with pytest.raises(ValidationError):
            ModelDescription(guid="invalid-guid")

    def test_discipline_creation(self):
        metadata = Metadata(key="example_key", value="example_value")
        discipline = Discipline(
            name="Aerodynamics",
            description="Study of the motion of air",
            tools=[],
            metadata=metadata,
        )
        assert discipline.name == "Aerodynamics"
        assert discipline.description == "Study of the motion of air"
        assert discipline.tools == []
        assert discipline.metadata == metadata

    def test_discipline_optional_fields(self):
        metadata = Metadata(key="example_key", value="example_value")
        discipline = Discipline(metadata=metadata)
        assert discipline.name is None
        assert discipline.description is None
        assert discipline.tools == []
        assert discipline.metadata is not None

    def test_discipline_invalid_name(self):
        with pytest.raises(ValidationError):
            Discipline(
                name="Invalid Name!",
                metadata=Metadata(key="example_key", value="example_value"),
            )

    def test_discipline_add_tool(self):
        metadata = Metadata(key="example_key", value="example_value")
        discipline = Discipline(
            name="Aerodynamics",
            description="Study of the motion of air",
            tools=[],
            metadata=metadata,
        )
        data_exchange = DataExchange(
            model_identifier="model_123",
            inputs=["input1", "input2"],
            outputs=["output1"],
        )
        model_description = ModelDescription(
            specification_version="2.0",
            model_name="Test Model",
            guid=str(uuid.uuid4()),
            generation_tool="Tool XYZ",
            generation_date_and_time=datetime.now(),
            data_exchange=data_exchange,
            license="MIT",
            copyright="NASA",
            author="John Doe",
            version="1.0",
            description="A test model",
        )
        discipline.add_tool(model_description)
        assert discipline.tools is not None
        assert len(discipline.tools) == 1
        assert discipline.tools[0] == model_description
