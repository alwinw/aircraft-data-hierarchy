from __future__ import annotations

from adh.wbs.systems.systems_parameters import (
    CoolingRequirements,
    DataSignal,
    FunctionalBlock,
    PhysicalCharacteristics,
    PowerRequirements,
    SignalDirection,
    SignalType,
    SystemAttributes,
    SystemRecord,
)


def _make_attributes() -> SystemAttributes:
    return SystemAttributes(
        functional_blocks=[
            FunctionalBlock(
                block_id="fb_1",
                name="PowerDistribution",
                description="Distributes electrical power to subsystems",
                inputs=["main_bus"],
                outputs=["subsystem_a", "subsystem_b"],
            )
        ],
        data_signals=[
            DataSignal(
                name="bus_voltage",
                type=SignalType.ANALOG,
                direction=SignalDirection.OUTPUT,
                source="fb_1",
                destination="subsystem_a",
                description="Main bus voltage signal",
            )
        ],
        physical_characteristics=PhysicalCharacteristics(
            weight=45.0,
            dimensions={"length": 0.6, "width": 0.4, "height": 0.2},
            volume=0.048,
            center_of_gravity={"x": 0.3, "y": 0.2, "z": 0.1},
        ),
        cooling_requirements=CoolingRequirements(
            method="Air",
            heat_dissipation=500.0,
            max_operating_temperature=70.0,
        ),
        power_requirements=PowerRequirements(
            voltage=28.0,
            current=15.0,
            power_type="DC",
            peak_power=600.0,
            average_power=420.0,
        ),
    )


def test_system_record_minimal():
    """SystemRecord validates with required fields."""
    record = SystemRecord(
        wbs_id="1.2.4",
        mil_std_881f_reference="1.2.4",
        name="VehicleSubsystems",
        attributes=_make_attributes(),
        components=["1.2.4.2", "1.2.4.3"],
    )
    assert record.name == "VehicleSubsystems"
    assert record.wbs_id == "1.2.4"
    assert record.type == "System"
    assert len(record.components) == 2


def test_system_record_attributes():
    """SystemRecord attributes fields are accessible after validation."""
    record = SystemRecord(
        wbs_id="1.2.4",
        mil_std_881f_reference="1.2.4",
        name="VehicleSubsystems",
        attributes=_make_attributes(),
        components=["1.2.4.2"],
    )
    attrs = record.attributes
    assert len(attrs.functional_blocks) == 1
    assert attrs.functional_blocks[0].block_id == "fb_1"
    assert attrs.physical_characteristics.weight == 45.0
    assert attrs.fluid_flow is None
