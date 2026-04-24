# Generated from scripts/taxonomy/air_vehicle.yaml by scripts/gen_wbs_classes.py
# Re-run the generator if taxonomy/*.yaml files change.
# Hand edits to this file are preserved across --check runs,
# but class definitions, wbs_no defaults, and child fields will be
# overwritten if the generator is re-run in write mode.

from __future__ import annotations

from typing import Optional

from pydantic import Field

from adh.msosa.architecture import Architecture, MSoSAMixin
from adh.wbs.ground_segment import GroundHostSegment
from adh.wbs.payload import PayloadMissionSystem
from adh.wbs.program_common import (
    AircraftSystemSoftwareRelease,
    CommonSupportEquipment,
    ContractorLogisticsSupport,
    Data,
    IndustrialFacilities,
    InitialSparesAndRepairParts,
    OperationalSiteActivation,
    PeculiarSupportEquipment,
    ProgramManagement,
    SystemsEngineering,
    SystemTestAndEvaluation,
    Training,
)


class AircraftSystem(MSoSAMixin, Architecture):
    """Aircraft System. MIL-STD-881F A.4.1. WBS 1.0."""

    wbs_no: str = Field(default="1.0", description="WBS number per MIL-STD-881F.")
    integration: Optional[AircraftSystemIntegrationAssemblyTestAndCheckout] = Field(
        default=None
    )
    air_vehicle: Optional[AirVehicle] = Field(default=None)
    payload_mission_system: Optional[PayloadMissionSystem] = Field(default=None)
    ground_host_segment: Optional[GroundHostSegment] = Field(default=None)
    software_release: Optional[AircraftSystemSoftwareRelease] = Field(default=None)
    systems_engineering: Optional[SystemsEngineering] = Field(default=None)
    program_management: Optional[ProgramManagement] = Field(default=None)
    system_test_and_evaluation: Optional[SystemTestAndEvaluation] = Field(default=None)
    training: Optional[Training] = Field(default=None)
    data: Optional[Data] = Field(default=None)
    peculiar_support_equipment: Optional[PeculiarSupportEquipment] = Field(default=None)
    common_support_equipment: Optional[CommonSupportEquipment] = Field(default=None)
    operational_site_activation: Optional[OperationalSiteActivation] = Field(
        default=None
    )
    contractor_logistics_support: Optional[ContractorLogisticsSupport] = Field(
        default=None
    )
    industrial_facilities: Optional[IndustrialFacilities] = Field(default=None)
    initial_spares_and_repair_parts: Optional[InitialSparesAndRepairParts] = Field(
        default=None
    )


class AircraftSystemIntegrationAssemblyTestAndCheckout(MSoSAMixin, Architecture):
    """Aircraft System, Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.2. WBS 1.1."""

    wbs_no: str = Field(default="1.1", description="WBS number per MIL-STD-881F.")


class AirVehicle(MSoSAMixin, Architecture):
    """Air Vehicle. MIL-STD-881F A.4.3. WBS 1.2."""

    wbs_no: str = Field(default="1.2", description="WBS number per MIL-STD-881F.")
    integration: Optional[AirVehicleIntegrationAssemblyTestAndCheckout] = Field(
        default=None
    )
    airframe: Optional[Airframe] = Field(default=None)
    propulsion: Optional[Propulsion] = Field(default=None)
    vehicle_subsystems: Optional[VehicleSubsystems] = Field(default=None)
    avionics: Optional[Avionics] = Field(default=None)
    armament_weapons_delivery: Optional[ArmamentWeaponsDelivery] = Field(default=None)
    auxiliary_equipment: Optional[AuxiliaryEquipment] = Field(default=None)
    furnishings_and_equipment: Optional[FurnishingsAndEquipment] = Field(default=None)
    software_release: Optional[AirVehicleSoftwareRelease] = Field(default=None)
    other: Optional[OtherAirVehicle] = Field(default=None)


class AirVehicleIntegrationAssemblyTestAndCheckout(MSoSAMixin, Architecture):
    """Air Vehicle Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.3.1. WBS 1.2.1."""

    wbs_no: str = Field(default="1.2.1", description="WBS number per MIL-STD-881F.")


class Airframe(MSoSAMixin, Architecture):
    """Airframe. MIL-STD-881F A.4.3.2. WBS 1.2.2."""

    wbs_no: str = Field(default="1.2.2", description="WBS number per MIL-STD-881F.")
    integration: Optional[AirframeIntegrationAssemblyTestAndCheckout] = Field(
        default=None
    )
    fuselage: Optional[Fuselage] = Field(default=None)
    wing: Optional[Wing] = Field(default=None)
    empennage: Optional[Empennage] = Field(default=None)
    nacelle: Optional[Nacelle] = Field(default=None)
    other: Optional[OtherAirframeComponents] = Field(default=None)


class AirframeIntegrationAssemblyTestAndCheckout(MSoSAMixin, Architecture):
    """Airframe Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.3.2.1. WBS 1.2.2.1."""

    wbs_no: str = Field(default="1.2.2.1", description="WBS number per MIL-STD-881F.")


class Fuselage(MSoSAMixin, Architecture):
    """Fuselage. MIL-STD-881F A.4.3.2.2. WBS 1.2.2.2."""

    wbs_no: str = Field(default="1.2.2.2", description="WBS number per MIL-STD-881F.")


class Wing(MSoSAMixin, Architecture):
    """Wing. MIL-STD-881F A.4.3.2.3. WBS 1.2.2.3."""

    wbs_no: str = Field(default="1.2.2.3", description="WBS number per MIL-STD-881F.")


class Empennage(MSoSAMixin, Architecture):
    """Empennage. MIL-STD-881F A.4.3.2.4. WBS 1.2.2.4."""

    wbs_no: str = Field(default="1.2.2.4", description="WBS number per MIL-STD-881F.")


class Nacelle(MSoSAMixin, Architecture):
    """Nacelle. MIL-STD-881F A.4.3.2.5. WBS 1.2.2.5."""

    wbs_no: str = Field(default="1.2.2.5", description="WBS number per MIL-STD-881F.")


class OtherAirframeComponents(MSoSAMixin, Architecture):
    """Other Airframe Components. MIL-STD-881F A.4.3.2.6. WBS 1.2.2.6."""

    wbs_no: str = Field(default="1.2.2.6", description="WBS number per MIL-STD-881F.")


class Propulsion(MSoSAMixin, Architecture):
    """Propulsion. MIL-STD-881F A.4.3.3. WBS 1.2.3."""

    wbs_no: str = Field(default="1.2.3", description="WBS number per MIL-STD-881F.")


class VehicleSubsystems(MSoSAMixin, Architecture):
    """Vehicle Subsystems. MIL-STD-881F A.4.3.4. WBS 1.2.4."""

    wbs_no: str = Field(default="1.2.4", description="WBS number per MIL-STD-881F.")
    integration: Optional[VehicleSubsystemIntegrationAssemblyTestAndCheckout] = Field(
        default=None
    )
    flight_control_subsystem: Optional[FlightControlSubsystem] = Field(default=None)
    auxiliary_power_subsystem: Optional[AuxiliaryPowerSubsystem] = Field(default=None)
    hydraulic_subsystem: Optional[HydraulicSubsystem] = Field(default=None)
    electrical_subsystem: Optional[ElectricalSubsystem] = Field(default=None)
    crew_station_subsystem: Optional[CrewStationSubsystem] = Field(default=None)
    environmental_control_subsystem: Optional[EnvironmentalControlSubsystem] = Field(
        default=None
    )
    fuel_subsystem: Optional[FuelSubsystem] = Field(default=None)
    landing_gear: Optional[LandingGear] = Field(default=None)
    rotor_group: Optional[RotorGroup] = Field(default=None)
    drive_group: Optional[DriveGroup] = Field(default=None)
    software_release: Optional[VehicleSubsystemSoftwareRelease] = Field(default=None)
    other: Optional[OtherSubsystems] = Field(default=None)


class VehicleSubsystemIntegrationAssemblyTestAndCheckout(MSoSAMixin, Architecture):
    """Vehicle Subsystem Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.3.4.1. WBS 1.2.4.1."""

    wbs_no: str = Field(default="1.2.4.1", description="WBS number per MIL-STD-881F.")


class FlightControlSubsystem(MSoSAMixin, Architecture):
    """Flight Control Subsystem. MIL-STD-881F A.4.3.4.2. WBS 1.2.4.2."""

    wbs_no: str = Field(default="1.2.4.2", description="WBS number per MIL-STD-881F.")


class AuxiliaryPowerSubsystem(MSoSAMixin, Architecture):
    """Auxiliary Power Subsystem. MIL-STD-881F A.4.3.4.3. WBS 1.2.4.3."""

    wbs_no: str = Field(default="1.2.4.3", description="WBS number per MIL-STD-881F.")


class HydraulicSubsystem(MSoSAMixin, Architecture):
    """Hydraulic Subsystem. MIL-STD-881F A.4.3.4.4. WBS 1.2.4.4."""

    wbs_no: str = Field(default="1.2.4.4", description="WBS number per MIL-STD-881F.")


class ElectricalSubsystem(MSoSAMixin, Architecture):
    """Electrical Subsystem. MIL-STD-881F A.4.3.4.5. WBS 1.2.4.5."""

    wbs_no: str = Field(default="1.2.4.5", description="WBS number per MIL-STD-881F.")


class CrewStationSubsystem(MSoSAMixin, Architecture):
    """Crew Station Subsystem. MIL-STD-881F A.4.3.4.6. WBS 1.2.4.6."""

    wbs_no: str = Field(default="1.2.4.6", description="WBS number per MIL-STD-881F.")


class EnvironmentalControlSubsystem(MSoSAMixin, Architecture):
    """Environmental Control Subsystem. MIL-STD-881F A.4.3.4.7. WBS 1.2.4.7."""

    wbs_no: str = Field(default="1.2.4.7", description="WBS number per MIL-STD-881F.")


class FuelSubsystem(MSoSAMixin, Architecture):
    """Fuel Subsystem. MIL-STD-881F A.4.3.4.8. WBS 1.2.4.8."""

    wbs_no: str = Field(default="1.2.4.8", description="WBS number per MIL-STD-881F.")


class LandingGear(MSoSAMixin, Architecture):
    """Landing Gear. MIL-STD-881F A.4.3.4.9. WBS 1.2.4.9."""

    wbs_no: str = Field(default="1.2.4.9", description="WBS number per MIL-STD-881F.")


class RotorGroup(MSoSAMixin, Architecture):
    """Rotor Group. MIL-STD-881F A.4.3.4.10. WBS 1.2.4.10."""

    wbs_no: str = Field(default="1.2.4.10", description="WBS number per MIL-STD-881F.")


class DriveGroup(MSoSAMixin, Architecture):
    """Drive Group. MIL-STD-881F A.4.3.4.11. WBS 1.2.4.11."""

    wbs_no: str = Field(default="1.2.4.11", description="WBS number per MIL-STD-881F.")


class VehicleSubsystemSoftwareRelease(MSoSAMixin, Architecture):
    """Vehicle Subsystem Software Release. MIL-STD-881F A.4.3.4.12. WBS 1.2.4.12."""

    wbs_no: str = Field(default="1.2.4.12", description="WBS number per MIL-STD-881F.")


class OtherSubsystems(MSoSAMixin, Architecture):
    """Other Subsystems. MIL-STD-881F A.4.3.4.13. WBS 1.2.4.13."""

    wbs_no: str = Field(default="1.2.4.13", description="WBS number per MIL-STD-881F.")


class Avionics(MSoSAMixin, Architecture):
    """Avionics. MIL-STD-881F A.4.3.5. WBS 1.2.5."""

    wbs_no: str = Field(default="1.2.5", description="WBS number per MIL-STD-881F.")
    integration: Optional[AvionicsIntegrationAssemblyTestAndCheckout] = Field(
        default=None
    )
    communication_identification: Optional[CommunicationIdentification] = Field(
        default=None
    )
    navigation_guidance: Optional[NavigationGuidance] = Field(default=None)
    mission_computer_processing: Optional[MissionComputerProcessing] = Field(
        default=None
    )
    fire_control: Optional[FireControl] = Field(default=None)
    data_display_and_controls: Optional[DataDisplayAndControls] = Field(default=None)
    survivability: Optional[Survivability] = Field(default=None)
    reconnaissance: Optional[Reconnaissance] = Field(default=None)
    electronic_warfare: Optional[ElectronicWarfare] = Field(default=None)
    automatic_flight_control: Optional[AutomaticFlightControl] = Field(default=None)
    health_monitoring_system: Optional[HealthMonitoringSystem] = Field(default=None)
    stores_management: Optional[StoresManagement] = Field(default=None)
    software_release: Optional[AvionicsSoftwareRelease] = Field(default=None)
    other: Optional[OtherAvionicsSubsystems] = Field(default=None)


class AvionicsIntegrationAssemblyTestAndCheckout(MSoSAMixin, Architecture):
    """Avionics Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.3.5.1. WBS 1.2.5.1."""

    wbs_no: str = Field(default="1.2.5.1", description="WBS number per MIL-STD-881F.")


class CommunicationIdentification(MSoSAMixin, Architecture):
    """Communication/Identification. MIL-STD-881F A.4.3.5.2. WBS 1.2.5.2."""

    wbs_no: str = Field(default="1.2.5.2", description="WBS number per MIL-STD-881F.")


class NavigationGuidance(MSoSAMixin, Architecture):
    """Navigation/Guidance. MIL-STD-881F A.4.3.5.3. WBS 1.2.5.3."""

    wbs_no: str = Field(default="1.2.5.3", description="WBS number per MIL-STD-881F.")


class MissionComputerProcessing(MSoSAMixin, Architecture):
    """Mission Computer/Processing. MIL-STD-881F A.4.3.5.4. WBS 1.2.5.4."""

    wbs_no: str = Field(default="1.2.5.4", description="WBS number per MIL-STD-881F.")


class FireControl(MSoSAMixin, Architecture):
    """Fire Control. MIL-STD-881F A.4.3.5.5. WBS 1.2.5.5."""

    wbs_no: str = Field(default="1.2.5.5", description="WBS number per MIL-STD-881F.")


class DataDisplayAndControls(MSoSAMixin, Architecture):
    """Data Display and Controls. MIL-STD-881F A.4.3.5.6. WBS 1.2.5.6."""

    wbs_no: str = Field(default="1.2.5.6", description="WBS number per MIL-STD-881F.")


class Survivability(MSoSAMixin, Architecture):
    """Survivability. MIL-STD-881F A.4.3.5.7. WBS 1.2.5.7."""

    wbs_no: str = Field(default="1.2.5.7", description="WBS number per MIL-STD-881F.")


class Reconnaissance(MSoSAMixin, Architecture):
    """Reconnaissance. MIL-STD-881F A.4.3.5.8. WBS 1.2.5.8."""

    wbs_no: str = Field(default="1.2.5.8", description="WBS number per MIL-STD-881F.")


class ElectronicWarfare(MSoSAMixin, Architecture):
    """Electronic Warfare. MIL-STD-881F A.4.3.5.9. WBS 1.2.5.9."""

    wbs_no: str = Field(default="1.2.5.9", description="WBS number per MIL-STD-881F.")


class AutomaticFlightControl(MSoSAMixin, Architecture):
    """Automatic Flight Control. MIL-STD-881F A.4.3.5.10. WBS 1.2.5.10."""

    wbs_no: str = Field(default="1.2.5.10", description="WBS number per MIL-STD-881F.")


class HealthMonitoringSystem(MSoSAMixin, Architecture):
    """Health Monitoring System. MIL-STD-881F A.4.3.5.11. WBS 1.2.5.11."""

    wbs_no: str = Field(default="1.2.5.11", description="WBS number per MIL-STD-881F.")


class StoresManagement(MSoSAMixin, Architecture):
    """Stores Management. MIL-STD-881F A.4.3.5.12. WBS 1.2.5.12."""

    wbs_no: str = Field(default="1.2.5.12", description="WBS number per MIL-STD-881F.")


class AvionicsSoftwareRelease(MSoSAMixin, Architecture):
    """Avionics Software Release. MIL-STD-881F A.4.3.5.13. WBS 1.2.5.13."""

    wbs_no: str = Field(default="1.2.5.13", description="WBS number per MIL-STD-881F.")


class OtherAvionicsSubsystems(MSoSAMixin, Architecture):
    """Other Avionics Subsystems. MIL-STD-881F A.4.3.5.14. WBS 1.2.5.14."""

    wbs_no: str = Field(default="1.2.5.14", description="WBS number per MIL-STD-881F.")


class ArmamentWeaponsDelivery(MSoSAMixin, Architecture):
    """Armament/Weapons Delivery. MIL-STD-881F A.4.3.6. WBS 1.2.6."""

    wbs_no: str = Field(default="1.2.6", description="WBS number per MIL-STD-881F.")


class AuxiliaryEquipment(MSoSAMixin, Architecture):
    """Auxiliary Equipment. MIL-STD-881F A.4.3.7. WBS 1.2.7."""

    wbs_no: str = Field(default="1.2.7", description="WBS number per MIL-STD-881F.")


class FurnishingsAndEquipment(MSoSAMixin, Architecture):
    """Furnishings and Equipment. MIL-STD-881F A.4.3.8. WBS 1.2.8."""

    wbs_no: str = Field(default="1.2.8", description="WBS number per MIL-STD-881F.")


class AirVehicleSoftwareRelease(MSoSAMixin, Architecture):
    """Air Vehicle Software Release. MIL-STD-881F A.4.3.9. WBS 1.2.9."""

    wbs_no: str = Field(default="1.2.9", description="WBS number per MIL-STD-881F.")


class OtherAirVehicle(MSoSAMixin, Architecture):
    """Other Air Vehicle. MIL-STD-881F A.4.3.10. WBS 1.2.10."""

    wbs_no: str = Field(default="1.2.10", description="WBS number per MIL-STD-881F.")


Airframe.model_rebuild()
VehicleSubsystems.model_rebuild()
Avionics.model_rebuild()
AircraftSystem.model_rebuild()
AirVehicle.model_rebuild()

__all__ = [
    "AircraftSystem",
    "AircraftSystemIntegrationAssemblyTestAndCheckout",
    "Airframe",
    "AirframeIntegrationAssemblyTestAndCheckout",
    "AirVehicle",
    "AirVehicleIntegrationAssemblyTestAndCheckout",
    "AirVehicleSoftwareRelease",
    "ArmamentWeaponsDelivery",
    "AutomaticFlightControl",
    "AuxiliaryEquipment",
    "AuxiliaryPowerSubsystem",
    "Avionics",
    "AvionicsIntegrationAssemblyTestAndCheckout",
    "AvionicsSoftwareRelease",
    "CommunicationIdentification",
    "CrewStationSubsystem",
    "DataDisplayAndControls",
    "DriveGroup",
    "ElectricalSubsystem",
    "ElectronicWarfare",
    "Empennage",
    "EnvironmentalControlSubsystem",
    "FireControl",
    "FlightControlSubsystem",
    "FuelSubsystem",
    "FurnishingsAndEquipment",
    "Fuselage",
    "HealthMonitoringSystem",
    "HydraulicSubsystem",
    "LandingGear",
    "MissionComputerProcessing",
    "Nacelle",
    "NavigationGuidance",
    "OtherAirframeComponents",
    "OtherAirVehicle",
    "OtherAvionicsSubsystems",
    "OtherSubsystems",
    "Propulsion",
    "Reconnaissance",
    "RotorGroup",
    "StoresManagement",
    "Survivability",
    "VehicleSubsystemIntegrationAssemblyTestAndCheckout",
    "VehicleSubsystems",
    "VehicleSubsystemSoftwareRelease",
    "Wing",
]
