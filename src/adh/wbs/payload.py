# Generated from scripts/taxonomy/payload.yaml by scripts/gen_wbs_classes.py
# Re-run the generator if taxonomy/*.yaml files change.
# Hand edits to this file are preserved across --check runs,
# but class definitions, wbs_no defaults, and child fields will be
# overwritten if the generator is re-run in write mode.

from __future__ import annotations

from typing import Optional

from pydantic import Field

from adh.msosa.architecture import Architecture, MSoSAMixin


class PayloadMissionSystem(MSoSAMixin, Architecture):
    """Payload/Mission System. MIL-STD-881F A.4.4. WBS 1.3."""

    wbs_no: str = Field(default="1.3", description="WBS number per MIL-STD-881F.")
    integration: Optional[PayloadIntegrationAssemblyTestAndCheckout] = Field(
        default=None
    )
    survivability_payload: Optional[SurvivabilityPayload] = Field(default=None)
    reconnaissance_payload: Optional[ReconnaissancePayload] = Field(default=None)
    electronic_warfare_payload: Optional[ElectronicWarfarePayload] = Field(default=None)
    armament_weapons_delivery_payload: Optional[ArmamentWeaponsDeliveryPayload] = Field(
        default=None
    )
    software_release: Optional[PayloadSoftwareRelease] = Field(default=None)
    other: Optional[OtherPayload] = Field(default=None)


class PayloadIntegrationAssemblyTestAndCheckout(MSoSAMixin, Architecture):
    """Payload Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.4.1. WBS 1.3.1."""

    wbs_no: str = Field(default="1.3.1", description="WBS number per MIL-STD-881F.")


class SurvivabilityPayload(MSoSAMixin, Architecture):
    """Survivability Payload. MIL-STD-881F A.4.4.2. WBS 1.3.2."""

    wbs_no: str = Field(default="1.3.2", description="WBS number per MIL-STD-881F.")


class ReconnaissancePayload(MSoSAMixin, Architecture):
    """Reconnaissance Payload. MIL-STD-881F A.4.4.3. WBS 1.3.3."""

    wbs_no: str = Field(default="1.3.3", description="WBS number per MIL-STD-881F.")


class ElectronicWarfarePayload(MSoSAMixin, Architecture):
    """Electronic Warfare Payload. MIL-STD-881F A.4.4.4. WBS 1.3.4."""

    wbs_no: str = Field(default="1.3.4", description="WBS number per MIL-STD-881F.")


class ArmamentWeaponsDeliveryPayload(MSoSAMixin, Architecture):
    """Armament/Weapons Delivery Payload. MIL-STD-881F A.4.4.5. WBS 1.3.5."""

    wbs_no: str = Field(default="1.3.5", description="WBS number per MIL-STD-881F.")


class PayloadSoftwareRelease(MSoSAMixin, Architecture):
    """Payload Software Release. MIL-STD-881F A.4.4.6. WBS 1.3.6."""

    wbs_no: str = Field(default="1.3.6", description="WBS number per MIL-STD-881F.")


class OtherPayload(MSoSAMixin, Architecture):
    """Other Payload. MIL-STD-881F A.4.4.7. WBS 1.3.7."""

    wbs_no: str = Field(default="1.3.7", description="WBS number per MIL-STD-881F.")


PayloadMissionSystem.model_rebuild()

__all__ = [
    "ArmamentWeaponsDeliveryPayload",
    "ElectronicWarfarePayload",
    "OtherPayload",
    "PayloadIntegrationAssemblyTestAndCheckout",
    "PayloadMissionSystem",
    "PayloadSoftwareRelease",
    "ReconnaissancePayload",
    "SurvivabilityPayload",
]
