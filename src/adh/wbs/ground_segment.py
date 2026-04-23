# Generated from scripts/taxonomy/ground_segment.yaml by scripts/gen_wbs_classes.py
# Re-run the generator if taxonomy/*.yaml files change.
# Hand edits to this file are preserved across --check runs,
# but class definitions, wbs_no defaults, and child fields will be
# overwritten if the generator is re-run in write mode.

from __future__ import annotations

from typing import Optional

from pydantic import Field

from adh.msosa.architecture import Architecture
from adh.msosa.mixin import MSoSAMixin


class GroundHostSegment(MSoSAMixin, Architecture):
    """Ground/Host Segment. MIL-STD-881F A.4.5. WBS 1.4."""

    wbs_no: str = Field(default="1.4", description="WBS number per MIL-STD-881F.")
    integration: Optional[GroundSegmentIntegrationAssemblyTestAndCheckout] = Field(
        default=None
    )
    ground_control_systems: Optional[GroundControlSystems] = Field(default=None)
    command_and_control_subsystem: Optional[CommandAndControlSubsystem] = Field(
        default=None
    )
    launch_equipment: Optional[LaunchEquipment] = Field(default=None)
    recovery_equipment: Optional[RecoveryEquipment] = Field(default=None)
    transport_vehicles: Optional[TransportVehicles] = Field(default=None)
    software_release: Optional[GroundSegmentSoftwareRelease] = Field(default=None)
    other: Optional[OtherGroundHostSegment] = Field(default=None)


class GroundSegmentIntegrationAssemblyTestAndCheckout(MSoSAMixin, Architecture):
    """Ground Segment Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.5.1. WBS 1.4.1."""

    wbs_no: str = Field(default="1.4.1", description="WBS number per MIL-STD-881F.")


class GroundControlSystems(MSoSAMixin, Architecture):
    """Ground Control Systems. MIL-STD-881F A.4.5.2. WBS 1.4.2."""

    wbs_no: str = Field(default="1.4.2", description="WBS number per MIL-STD-881F.")


class CommandAndControlSubsystem(MSoSAMixin, Architecture):
    """Command and Control Subsystem. MIL-STD-881F A.4.5.3. WBS 1.4.3."""

    wbs_no: str = Field(default="1.4.3", description="WBS number per MIL-STD-881F.")


class LaunchEquipment(MSoSAMixin, Architecture):
    """Launch Equipment. MIL-STD-881F A.4.5.4. WBS 1.4.4."""

    wbs_no: str = Field(default="1.4.4", description="WBS number per MIL-STD-881F.")


class RecoveryEquipment(MSoSAMixin, Architecture):
    """Recovery Equipment. MIL-STD-881F A.4.5.5. WBS 1.4.5."""

    wbs_no: str = Field(default="1.4.5", description="WBS number per MIL-STD-881F.")


class TransportVehicles(MSoSAMixin, Architecture):
    """Transport Vehicles. MIL-STD-881F A.4.5.6. WBS 1.4.6."""

    wbs_no: str = Field(default="1.4.6", description="WBS number per MIL-STD-881F.")


class GroundSegmentSoftwareRelease(MSoSAMixin, Architecture):
    """Ground Segment Software Release. MIL-STD-881F A.4.5.7. WBS 1.4.7."""

    wbs_no: str = Field(default="1.4.7", description="WBS number per MIL-STD-881F.")


class OtherGroundHostSegment(MSoSAMixin, Architecture):
    """Other Ground/Host Segment. MIL-STD-881F A.4.5.8. WBS 1.4.8."""

    wbs_no: str = Field(default="1.4.8", description="WBS number per MIL-STD-881F.")


GroundHostSegment.model_rebuild()

__all__ = [
    "CommandAndControlSubsystem",
    "GroundControlSystems",
    "GroundHostSegment",
    "GroundSegmentIntegrationAssemblyTestAndCheckout",
    "GroundSegmentSoftwareRelease",
    "LaunchEquipment",
    "OtherGroundHostSegment",
    "RecoveryEquipment",
    "TransportVehicles",
]
