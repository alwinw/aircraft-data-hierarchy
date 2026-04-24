from __future__ import annotations

from typing import Optional

import pytest
from pydantic import ValidationError

from adh.msosa import (
    Architecture,
    Behaviors,
    MSoSAMixin,
    NodeMetaMixin,
    Performances,
    Requirements,
)
from adh.wbs import Avionics, Wing
from adh.wbs.airframe.airframe import Component
from adh.wbs.airframe.airframe_geometry import Float, Geometry
from adh.wbs.airframe.airframe_parameters import (
    AerodynamicsData,
    Parameters,
    ReferenceData,
)
from adh.wbs.equipment import Equipment
from adh.wbs.propulsion.propulsion import Propulsion
from adh.wbs.propulsion.propulsion_cycle import PropulsionCycle
from adh.wbs.propulsion.propulsion_geometry import PropulsionGeometry
from adh.wbs.propulsion.propulsion_multipoint import MultiPointCycle
from adh.wbs.systems.systems import System


class ExampleArchitectureNode(MSoSAMixin, Architecture):
    child: Optional[ExampleArchitectureNode] = None


ExampleArchitectureNode.model_rebuild()


@pytest.mark.parametrize(
    ("model_cls", "child_field"),
    [
        (Component, "subcomponents"),
        (Equipment, "subequipment"),
        (Propulsion, "subcomponents"),
        (System, "subsystems"),
    ],
)
def test_true_architecture_nodes_expose_recursive_msosa_fields(model_cls, child_field):
    node = model_cls(
        name="node",
        **{
            child_field: [
                model_cls(
                    name="child",
                    requirements=Requirements(),
                    performance=Performances(),
                    behavior=Behaviors(),
                )
            ]
        },
        requirements=Requirements(),
        performance=Performances(),
        behavior=Behaviors(),
    )

    assert isinstance(node.requirements, Requirements)
    assert isinstance(node.performance, Performances)
    assert isinstance(node.behavior, Behaviors)
    assert isinstance(getattr(node, child_field)[0].requirements, Requirements)


def test_mixin_fields_round_trip_with_architecture_validation():
    node = ExampleArchitectureNode(
        name="root",
        wbs_no="1.2",
        requirements=Requirements(),
        performance=Performances(),
        behavior=Behaviors(),
        child=ExampleArchitectureNode(name="leaf", wbs_no="1.2.1"),
    )

    payload = node.model_dump()
    restored = ExampleArchitectureNode.model_validate(payload)

    assert restored.wbs_no == "1.2"
    assert isinstance(restored.requirements, Requirements)
    assert isinstance(restored.performance, Performances)
    assert isinstance(restored.behavior, Behaviors)
    assert restored.child is not None


@pytest.mark.parametrize(
    "model_cls",
    [PropulsionCycle, PropulsionGeometry, Float, Geometry, Parameters],
)
def test_non_architecture_models_do_not_expose_recursive_msosa_fields(model_cls):
    assert not issubclass(model_cls, Architecture)
    assert "requirements" not in model_cls.model_fields
    assert "performance" not in model_cls.model_fields
    assert "behavior" not in model_cls.model_fields


@pytest.mark.parametrize(
    "model_cls",
    [PropulsionCycle, PropulsionGeometry, MultiPointCycle, ReferenceData],
)
def test_metadata_support_models_inherit_node_meta_mixin(model_cls):
    assert issubclass(model_cls, NodeMetaMixin)


def test_metadata_support_model_fields_expose_uuid_and_source_info():
    assert "uuid" in AerodynamicsData.model_fields
    assert "source_info" in AerodynamicsData.model_fields


def test_architecture_validation_still_applies_with_mixin():
    with pytest.raises(ValidationError, match="Invalid WBS number"):
        ExampleArchitectureNode(wbs_no="not-a-wbs")


@pytest.mark.parametrize("model_cls", [Wing, Avionics])
def test_generated_wbs_nodes_expose_recursive_msosa_fields(model_cls):
    node = model_cls(
        requirements=Requirements(),
        performance=Performances(),
        behavior=Behaviors(),
    )

    assert isinstance(node.requirements, Requirements)
    assert isinstance(node.performance, Performances)
    assert isinstance(node.behavior, Behaviors)
