from __future__ import annotations

from typing import Optional

import pytest
from pydantic import ValidationError

from adh.msosa import Architecture, Behaviors, MSoSAMixin, Performances, Requirements
from adh.wbs.airframe.airframe import Component
from adh.wbs.equipment import Equipment
from adh.wbs.propulsion.propulsion import Propulsion
from adh.wbs.propulsion.propulsion_geometry import PropulsionGeometry
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


def test_propulsion_geometry_is_treated_as_true_architecture_node():
    geometry = PropulsionGeometry(
        requirements=Requirements(),
        performance=Performances(),
        behavior=Behaviors(),
    )

    assert isinstance(geometry.requirements, Requirements)
    assert isinstance(geometry.performance, Performances)
    assert isinstance(geometry.behavior, Behaviors)


def test_architecture_validation_still_applies_with_mixin():
    with pytest.raises(ValidationError, match="Invalid WBS number"):
        ExampleArchitectureNode(wbs_no="not-a-wbs")
