# Generated from scripts/taxonomy/ by scripts/gen_wbs_classes.py
# Re-run the generator if taxonomy/*.yaml files change.
# Hand edits below the generated classes are preserved across --check runs,
# but will be overwritten if the generator is re-run in write mode.

from __future__ import annotations

from typing import Optional

from pydantic import Field

from adh.msosa.architecture import Architecture


class AircraftSystem(Architecture):
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


class AircraftSystemIntegrationAssemblyTestAndCheckout(Architecture):
    """Aircraft System, Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.2. WBS 1.1."""

    wbs_no: str = Field(default="1.1", description="WBS number per MIL-STD-881F.")


class AirVehicle(Architecture):
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


class AirVehicleIntegrationAssemblyTestAndCheckout(Architecture):
    """Air Vehicle Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.3.1. WBS 1.2.1."""

    wbs_no: str = Field(default="1.2.1", description="WBS number per MIL-STD-881F.")


class Airframe(Architecture):
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


class AirframeIntegrationAssemblyTestAndCheckout(Architecture):
    """Airframe Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.3.2.1. WBS 1.2.2.1."""

    wbs_no: str = Field(default="1.2.2.1", description="WBS number per MIL-STD-881F.")


class Fuselage(Architecture):
    """Fuselage. MIL-STD-881F A.4.3.2.2. WBS 1.2.2.2."""

    wbs_no: str = Field(default="1.2.2.2", description="WBS number per MIL-STD-881F.")


class Wing(Architecture):
    """Wing. MIL-STD-881F A.4.3.2.3. WBS 1.2.2.3."""

    wbs_no: str = Field(default="1.2.2.3", description="WBS number per MIL-STD-881F.")


class Empennage(Architecture):
    """Empennage. MIL-STD-881F A.4.3.2.4. WBS 1.2.2.4."""

    wbs_no: str = Field(default="1.2.2.4", description="WBS number per MIL-STD-881F.")


class Nacelle(Architecture):
    """Nacelle. MIL-STD-881F A.4.3.2.5. WBS 1.2.2.5."""

    wbs_no: str = Field(default="1.2.2.5", description="WBS number per MIL-STD-881F.")


class OtherAirframeComponents(Architecture):
    """Other Airframe Components. MIL-STD-881F A.4.3.2.6. WBS 1.2.2.6."""

    wbs_no: str = Field(default="1.2.2.6", description="WBS number per MIL-STD-881F.")


class Propulsion(Architecture):
    """Propulsion. MIL-STD-881F A.4.3.3. WBS 1.2.3."""

    wbs_no: str = Field(default="1.2.3", description="WBS number per MIL-STD-881F.")


class VehicleSubsystems(Architecture):
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


class VehicleSubsystemIntegrationAssemblyTestAndCheckout(Architecture):
    """Vehicle Subsystem Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.3.4.1. WBS 1.2.4.1."""

    wbs_no: str = Field(default="1.2.4.1", description="WBS number per MIL-STD-881F.")


class FlightControlSubsystem(Architecture):
    """Flight Control Subsystem. MIL-STD-881F A.4.3.4.2. WBS 1.2.4.2."""

    wbs_no: str = Field(default="1.2.4.2", description="WBS number per MIL-STD-881F.")


class AuxiliaryPowerSubsystem(Architecture):
    """Auxiliary Power Subsystem. MIL-STD-881F A.4.3.4.3. WBS 1.2.4.3."""

    wbs_no: str = Field(default="1.2.4.3", description="WBS number per MIL-STD-881F.")


class HydraulicSubsystem(Architecture):
    """Hydraulic Subsystem. MIL-STD-881F A.4.3.4.4. WBS 1.2.4.4."""

    wbs_no: str = Field(default="1.2.4.4", description="WBS number per MIL-STD-881F.")


class ElectricalSubsystem(Architecture):
    """Electrical Subsystem. MIL-STD-881F A.4.3.4.5. WBS 1.2.4.5."""

    wbs_no: str = Field(default="1.2.4.5", description="WBS number per MIL-STD-881F.")


class CrewStationSubsystem(Architecture):
    """Crew Station Subsystem. MIL-STD-881F A.4.3.4.6. WBS 1.2.4.6."""

    wbs_no: str = Field(default="1.2.4.6", description="WBS number per MIL-STD-881F.")


class EnvironmentalControlSubsystem(Architecture):
    """Environmental Control Subsystem. MIL-STD-881F A.4.3.4.7. WBS 1.2.4.7."""

    wbs_no: str = Field(default="1.2.4.7", description="WBS number per MIL-STD-881F.")


class FuelSubsystem(Architecture):
    """Fuel Subsystem. MIL-STD-881F A.4.3.4.8. WBS 1.2.4.8."""

    wbs_no: str = Field(default="1.2.4.8", description="WBS number per MIL-STD-881F.")


class LandingGear(Architecture):
    """Landing Gear. MIL-STD-881F A.4.3.4.9. WBS 1.2.4.9."""

    wbs_no: str = Field(default="1.2.4.9", description="WBS number per MIL-STD-881F.")


class RotorGroup(Architecture):
    """Rotor Group. MIL-STD-881F A.4.3.4.10. WBS 1.2.4.10."""

    wbs_no: str = Field(default="1.2.4.10", description="WBS number per MIL-STD-881F.")


class DriveGroup(Architecture):
    """Drive Group. MIL-STD-881F A.4.3.4.11. WBS 1.2.4.11."""

    wbs_no: str = Field(default="1.2.4.11", description="WBS number per MIL-STD-881F.")


class VehicleSubsystemSoftwareRelease(Architecture):
    """Vehicle Subsystem Software Release. MIL-STD-881F A.4.3.4.12. WBS 1.2.4.12."""

    wbs_no: str = Field(default="1.2.4.12", description="WBS number per MIL-STD-881F.")


class OtherSubsystems(Architecture):
    """Other Subsystems. MIL-STD-881F A.4.3.4.13. WBS 1.2.4.13."""

    wbs_no: str = Field(default="1.2.4.13", description="WBS number per MIL-STD-881F.")


class Avionics(Architecture):
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


class AvionicsIntegrationAssemblyTestAndCheckout(Architecture):
    """Avionics Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.3.5.1. WBS 1.2.5.1."""

    wbs_no: str = Field(default="1.2.5.1", description="WBS number per MIL-STD-881F.")


class CommunicationIdentification(Architecture):
    """Communication/Identification. MIL-STD-881F A.4.3.5.2. WBS 1.2.5.2."""

    wbs_no: str = Field(default="1.2.5.2", description="WBS number per MIL-STD-881F.")


class NavigationGuidance(Architecture):
    """Navigation/Guidance. MIL-STD-881F A.4.3.5.3. WBS 1.2.5.3."""

    wbs_no: str = Field(default="1.2.5.3", description="WBS number per MIL-STD-881F.")


class MissionComputerProcessing(Architecture):
    """Mission Computer/Processing. MIL-STD-881F A.4.3.5.4. WBS 1.2.5.4."""

    wbs_no: str = Field(default="1.2.5.4", description="WBS number per MIL-STD-881F.")


class FireControl(Architecture):
    """Fire Control. MIL-STD-881F A.4.3.5.5. WBS 1.2.5.5."""

    wbs_no: str = Field(default="1.2.5.5", description="WBS number per MIL-STD-881F.")


class DataDisplayAndControls(Architecture):
    """Data Display and Controls. MIL-STD-881F A.4.3.5.6. WBS 1.2.5.6."""

    wbs_no: str = Field(default="1.2.5.6", description="WBS number per MIL-STD-881F.")


class Survivability(Architecture):
    """Survivability. MIL-STD-881F A.4.3.5.7. WBS 1.2.5.7."""

    wbs_no: str = Field(default="1.2.5.7", description="WBS number per MIL-STD-881F.")


class Reconnaissance(Architecture):
    """Reconnaissance. MIL-STD-881F A.4.3.5.8. WBS 1.2.5.8."""

    wbs_no: str = Field(default="1.2.5.8", description="WBS number per MIL-STD-881F.")


class ElectronicWarfare(Architecture):
    """Electronic Warfare. MIL-STD-881F A.4.3.5.9. WBS 1.2.5.9."""

    wbs_no: str = Field(default="1.2.5.9", description="WBS number per MIL-STD-881F.")


class AutomaticFlightControl(Architecture):
    """Automatic Flight Control. MIL-STD-881F A.4.3.5.10. WBS 1.2.5.10."""

    wbs_no: str = Field(default="1.2.5.10", description="WBS number per MIL-STD-881F.")


class HealthMonitoringSystem(Architecture):
    """Health Monitoring System. MIL-STD-881F A.4.3.5.11. WBS 1.2.5.11."""

    wbs_no: str = Field(default="1.2.5.11", description="WBS number per MIL-STD-881F.")


class StoresManagement(Architecture):
    """Stores Management. MIL-STD-881F A.4.3.5.12. WBS 1.2.5.12."""

    wbs_no: str = Field(default="1.2.5.12", description="WBS number per MIL-STD-881F.")


class AvionicsSoftwareRelease(Architecture):
    """Avionics Software Release. MIL-STD-881F A.4.3.5.13. WBS 1.2.5.13."""

    wbs_no: str = Field(default="1.2.5.13", description="WBS number per MIL-STD-881F.")


class OtherAvionicsSubsystems(Architecture):
    """Other Avionics Subsystems. MIL-STD-881F A.4.3.5.14. WBS 1.2.5.14."""

    wbs_no: str = Field(default="1.2.5.14", description="WBS number per MIL-STD-881F.")


class ArmamentWeaponsDelivery(Architecture):
    """Armament/Weapons Delivery. MIL-STD-881F A.4.3.6. WBS 1.2.6."""

    wbs_no: str = Field(default="1.2.6", description="WBS number per MIL-STD-881F.")


class AuxiliaryEquipment(Architecture):
    """Auxiliary Equipment. MIL-STD-881F A.4.3.7. WBS 1.2.7."""

    wbs_no: str = Field(default="1.2.7", description="WBS number per MIL-STD-881F.")


class FurnishingsAndEquipment(Architecture):
    """Furnishings and Equipment. MIL-STD-881F A.4.3.8. WBS 1.2.8."""

    wbs_no: str = Field(default="1.2.8", description="WBS number per MIL-STD-881F.")


class AirVehicleSoftwareRelease(Architecture):
    """Air Vehicle Software Release. MIL-STD-881F A.4.3.9. WBS 1.2.9."""

    wbs_no: str = Field(default="1.2.9", description="WBS number per MIL-STD-881F.")


class OtherAirVehicle(Architecture):
    """Other Air Vehicle. MIL-STD-881F A.4.3.10. WBS 1.2.10."""

    wbs_no: str = Field(default="1.2.10", description="WBS number per MIL-STD-881F.")


class GroundHostSegment(Architecture):
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


class GroundSegmentIntegrationAssemblyTestAndCheckout(Architecture):
    """Ground Segment Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.5.1. WBS 1.4.1."""

    wbs_no: str = Field(default="1.4.1", description="WBS number per MIL-STD-881F.")


class GroundControlSystems(Architecture):
    """Ground Control Systems. MIL-STD-881F A.4.5.2. WBS 1.4.2."""

    wbs_no: str = Field(default="1.4.2", description="WBS number per MIL-STD-881F.")


class CommandAndControlSubsystem(Architecture):
    """Command and Control Subsystem. MIL-STD-881F A.4.5.3. WBS 1.4.3."""

    wbs_no: str = Field(default="1.4.3", description="WBS number per MIL-STD-881F.")


class LaunchEquipment(Architecture):
    """Launch Equipment. MIL-STD-881F A.4.5.4. WBS 1.4.4."""

    wbs_no: str = Field(default="1.4.4", description="WBS number per MIL-STD-881F.")


class RecoveryEquipment(Architecture):
    """Recovery Equipment. MIL-STD-881F A.4.5.5. WBS 1.4.5."""

    wbs_no: str = Field(default="1.4.5", description="WBS number per MIL-STD-881F.")


class TransportVehicles(Architecture):
    """Transport Vehicles. MIL-STD-881F A.4.5.6. WBS 1.4.6."""

    wbs_no: str = Field(default="1.4.6", description="WBS number per MIL-STD-881F.")


class GroundSegmentSoftwareRelease(Architecture):
    """Ground Segment Software Release. MIL-STD-881F A.4.5.7. WBS 1.4.7."""

    wbs_no: str = Field(default="1.4.7", description="WBS number per MIL-STD-881F.")


class OtherGroundHostSegment(Architecture):
    """Other Ground/Host Segment. MIL-STD-881F A.4.5.8. WBS 1.4.8."""

    wbs_no: str = Field(default="1.4.8", description="WBS number per MIL-STD-881F.")


class PayloadMissionSystem(Architecture):
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


class PayloadIntegrationAssemblyTestAndCheckout(Architecture):
    """Payload Integration, Assembly, Test and Checkout. MIL-STD-881F A.4.4.1. WBS 1.3.1."""

    wbs_no: str = Field(default="1.3.1", description="WBS number per MIL-STD-881F.")


class SurvivabilityPayload(Architecture):
    """Survivability Payload. MIL-STD-881F A.4.4.2. WBS 1.3.2."""

    wbs_no: str = Field(default="1.3.2", description="WBS number per MIL-STD-881F.")


class ReconnaissancePayload(Architecture):
    """Reconnaissance Payload. MIL-STD-881F A.4.4.3. WBS 1.3.3."""

    wbs_no: str = Field(default="1.3.3", description="WBS number per MIL-STD-881F.")


class ElectronicWarfarePayload(Architecture):
    """Electronic Warfare Payload. MIL-STD-881F A.4.4.4. WBS 1.3.4."""

    wbs_no: str = Field(default="1.3.4", description="WBS number per MIL-STD-881F.")


class ArmamentWeaponsDeliveryPayload(Architecture):
    """Armament/Weapons Delivery Payload. MIL-STD-881F A.4.4.5. WBS 1.3.5."""

    wbs_no: str = Field(default="1.3.5", description="WBS number per MIL-STD-881F.")


class PayloadSoftwareRelease(Architecture):
    """Payload Software Release. MIL-STD-881F A.4.4.6. WBS 1.3.6."""

    wbs_no: str = Field(default="1.3.6", description="WBS number per MIL-STD-881F.")


class OtherPayload(Architecture):
    """Other Payload. MIL-STD-881F A.4.4.7. WBS 1.3.7."""

    wbs_no: str = Field(default="1.3.7", description="WBS number per MIL-STD-881F.")


class AircraftSystemSoftwareRelease(Architecture):
    """Aircraft System Software Release. MIL-STD-881F A.4.6. WBS 1.5."""

    wbs_no: str = Field(default="1.5", description="WBS number per MIL-STD-881F.")


class SystemsEngineering(Architecture):
    """Systems Engineering. MIL-STD-881F A.4.7. WBS 1.6."""

    wbs_no: str = Field(default="1.6", description="WBS number per MIL-STD-881F.")
    software_systems_engineering: Optional[SoftwareSystemsEngineering] = Field(
        default=None
    )
    integrated_logistics_support_systems_engineering: Optional[
        IntegratedLogisticsSupportSystemsEngineering
    ] = Field(default=None)
    cybersecurity_systems_engineering: Optional[CybersecuritySystemsEngineering] = (
        Field(default=None)
    )
    core_systems_engineering: Optional[CoreSystemsEngineering] = Field(default=None)
    other: Optional[OtherSystemsEngineering] = Field(default=None)


class SoftwareSystemsEngineering(Architecture):
    """Software Systems Engineering. MIL-STD-881F A.4.7.1. WBS 1.6.1."""

    wbs_no: str = Field(default="1.6.1", description="WBS number per MIL-STD-881F.")


class IntegratedLogisticsSupportSystemsEngineering(Architecture):
    """Integrated Logistics Support Systems Engineering. MIL-STD-881F A.4.7.2. WBS 1.6.2."""

    wbs_no: str = Field(default="1.6.2", description="WBS number per MIL-STD-881F.")


class CybersecuritySystemsEngineering(Architecture):
    """Cybersecurity Systems Engineering. MIL-STD-881F A.4.7.3. WBS 1.6.3."""

    wbs_no: str = Field(default="1.6.3", description="WBS number per MIL-STD-881F.")


class CoreSystemsEngineering(Architecture):
    """Core Systems Engineering. MIL-STD-881F A.4.7.4. WBS 1.6.4."""

    wbs_no: str = Field(default="1.6.4", description="WBS number per MIL-STD-881F.")


class OtherSystemsEngineering(Architecture):
    """Other Systems Engineering. MIL-STD-881F A.4.7.5. WBS 1.6.5."""

    wbs_no: str = Field(default="1.6.5", description="WBS number per MIL-STD-881F.")


class ProgramManagement(Architecture):
    """Program Management. MIL-STD-881F A.4.8. WBS 1.7."""

    wbs_no: str = Field(default="1.7", description="WBS number per MIL-STD-881F.")
    software_program_management: Optional[SoftwareProgramManagement] = Field(
        default=None
    )
    integrated_logistics_support_program_management: Optional[
        IntegratedLogisticsSupportProgramManagement
    ] = Field(default=None)
    cybersecurity_management: Optional[CybersecurityManagement] = Field(default=None)
    core_program_management: Optional[CoreProgramManagement] = Field(default=None)
    other: Optional[OtherProgramManagement] = Field(default=None)


class SoftwareProgramManagement(Architecture):
    """Software Program Management. MIL-STD-881F A.4.8.1. WBS 1.7.1."""

    wbs_no: str = Field(default="1.7.1", description="WBS number per MIL-STD-881F.")


class IntegratedLogisticsSupportProgramManagement(Architecture):
    """Integrated Logistics Support Program Management. MIL-STD-881F A.4.8.2. WBS 1.7.2."""

    wbs_no: str = Field(default="1.7.2", description="WBS number per MIL-STD-881F.")


class CybersecurityManagement(Architecture):
    """Cybersecurity Management. MIL-STD-881F A.4.8.3. WBS 1.7.3."""

    wbs_no: str = Field(default="1.7.3", description="WBS number per MIL-STD-881F.")


class CoreProgramManagement(Architecture):
    """Core Program Management. MIL-STD-881F A.4.8.4. WBS 1.7.4."""

    wbs_no: str = Field(default="1.7.4", description="WBS number per MIL-STD-881F.")


class OtherProgramManagement(Architecture):
    """Other Program Management. MIL-STD-881F A.4.8.5. WBS 1.7.5."""

    wbs_no: str = Field(default="1.7.5", description="WBS number per MIL-STD-881F.")


class SystemTestAndEvaluation(Architecture):
    """System Test and Evaluation. MIL-STD-881F A.4.9. WBS 1.8."""

    wbs_no: str = Field(default="1.8", description="WBS number per MIL-STD-881F.")
    developmental_test_and_evaluation: Optional[DevelopmentalTestAndEvaluation] = Field(
        default=None
    )
    operational_test_and_evaluation: Optional[OperationalTestAndEvaluation] = Field(
        default=None
    )
    live_fire_test_and_evaluation: Optional[LiveFireTestAndEvaluation] = Field(
        default=None
    )
    mock_ups_system_integration_labs: Optional[MockupsSystemIntegrationLabs] = Field(
        default=None
    )
    test_and_evaluation_support: Optional[TestAndEvaluationSupport] = Field(
        default=None
    )
    test_facilities: Optional[TestFacilities] = Field(default=None)


class DevelopmentalTestAndEvaluation(Architecture):
    """Developmental Test and Evaluation. MIL-STD-881F A.4.9.1. WBS 1.8.1."""

    wbs_no: str = Field(default="1.8.1", description="WBS number per MIL-STD-881F.")
    system_acceptance_test: Optional[SystemAcceptanceTest] = Field(default=None)
    wind_tunnel_tests: Optional[WindTunnelTests] = Field(default=None)
    structural_tests: Optional[StructuralTests] = Field(default=None)
    flight_tests: Optional[DTE_FlightTests] = Field(default=None)
    ground_tests: Optional[DTE_GroundTests] = Field(default=None)
    cybersecurity_test_and_evaluation: Optional[DTE_CybersecurityTestAndEvaluation] = (
        Field(default=None)
    )
    other: Optional[OtherDTETests] = Field(default=None)


class SystemAcceptanceTest(Architecture):
    """System Acceptance Test. MIL-STD-881F A.4.9.1.1. WBS 1.8.1.1."""

    wbs_no: str = Field(default="1.8.1.1", description="WBS number per MIL-STD-881F.")


class WindTunnelTests(Architecture):
    """Wind Tunnel Tests. MIL-STD-881F A.4.9.1.2. WBS 1.8.1.2."""

    wbs_no: str = Field(default="1.8.1.2", description="WBS number per MIL-STD-881F.")


class StructuralTests(Architecture):
    """Structural Tests. MIL-STD-881F A.4.9.1.3. WBS 1.8.1.3."""

    wbs_no: str = Field(default="1.8.1.3", description="WBS number per MIL-STD-881F.")


class DTE_FlightTests(Architecture):  # noqa: N801
    """Flight Tests. MIL-STD-881F A.4.9.1.4. WBS 1.8.1.4."""

    wbs_no: str = Field(default="1.8.1.4", description="WBS number per MIL-STD-881F.")


class DTE_GroundTests(Architecture):  # noqa: N801
    """Ground Tests. MIL-STD-881F A.4.9.1.5. WBS 1.8.1.5."""

    wbs_no: str = Field(default="1.8.1.5", description="WBS number per MIL-STD-881F.")


class DTE_CybersecurityTestAndEvaluation(Architecture):  # noqa: N801
    """Cybersecurity Test and Evaluation. MIL-STD-881F A.4.9.1.6. WBS 1.8.1.6."""

    wbs_no: str = Field(default="1.8.1.6", description="WBS number per MIL-STD-881F.")


class OtherDTETests(Architecture):
    """Other DT&E Tests. MIL-STD-881F A.4.9.1.7. WBS 1.8.1.7."""

    wbs_no: str = Field(default="1.8.1.7", description="WBS number per MIL-STD-881F.")


class OperationalTestAndEvaluation(Architecture):
    """Operational Test and Evaluation. MIL-STD-881F A.4.9.2. WBS 1.8.2."""

    wbs_no: str = Field(default="1.8.2", description="WBS number per MIL-STD-881F.")
    limited_user_evaluation: Optional[LimitedUserEvaluation] = Field(default=None)
    interoperability_testing: Optional[InteroperabilityTesting] = Field(default=None)
    flight_tests: Optional[OTE_FlightTests] = Field(default=None)
    ground_tests: Optional[OTE_GroundTests] = Field(default=None)
    cybersecurity_test_and_evaluation: Optional[OTE_CybersecurityTestAndEvaluation] = (
        Field(default=None)
    )
    other: Optional[OtherOTETests] = Field(default=None)


class LimitedUserEvaluation(Architecture):
    """Limited User Evaluation. MIL-STD-881F A.4.9.2.1. WBS 1.8.2.1."""

    wbs_no: str = Field(default="1.8.2.1", description="WBS number per MIL-STD-881F.")


class InteroperabilityTesting(Architecture):
    """Interoperability Testing. MIL-STD-881F A.4.9.2.2. WBS 1.8.2.2."""

    wbs_no: str = Field(default="1.8.2.2", description="WBS number per MIL-STD-881F.")


class OTE_FlightTests(Architecture):  # noqa: N801
    """Flight Tests. MIL-STD-881F A.4.9.2.3. WBS 1.8.2.3."""

    wbs_no: str = Field(default="1.8.2.3", description="WBS number per MIL-STD-881F.")


class OTE_GroundTests(Architecture):  # noqa: N801
    """Ground Tests. MIL-STD-881F A.4.9.2.4. WBS 1.8.2.4."""

    wbs_no: str = Field(default="1.8.2.4", description="WBS number per MIL-STD-881F.")


class OTE_CybersecurityTestAndEvaluation(Architecture):  # noqa: N801
    """Cybersecurity Test and Evaluation. MIL-STD-881F A.4.9.2.5. WBS 1.8.2.5."""

    wbs_no: str = Field(default="1.8.2.5", description="WBS number per MIL-STD-881F.")


class OtherOTETests(Architecture):
    """Other OT&E Tests. MIL-STD-881F A.4.9.2.6. WBS 1.8.2.6."""

    wbs_no: str = Field(default="1.8.2.6", description="WBS number per MIL-STD-881F.")


class LiveFireTestAndEvaluation(Architecture):
    """Live Fire Test and Evaluation. MIL-STD-881F A.4.9.3. WBS 1.8.3."""

    wbs_no: str = Field(default="1.8.3", description="WBS number per MIL-STD-881F.")


class MockupsSystemIntegrationLabs(Architecture):
    """Mock-ups/System Integration Labs. MIL-STD-881F A.4.9.4. WBS 1.8.4."""

    wbs_no: str = Field(default="1.8.4", description="WBS number per MIL-STD-881F.")


class TestAndEvaluationSupport(Architecture):
    """Test and Evaluation Support. MIL-STD-881F A.4.9.5. WBS 1.8.5."""

    wbs_no: str = Field(default="1.8.5", description="WBS number per MIL-STD-881F.")


class TestFacilities(Architecture):
    """Test Facilities. MIL-STD-881F A.4.9.6. WBS 1.8.6."""

    wbs_no: str = Field(default="1.8.6", description="WBS number per MIL-STD-881F.")


class Training(Architecture):
    """Training. MIL-STD-881F A.4.10. WBS 1.9."""

    wbs_no: str = Field(default="1.9", description="WBS number per MIL-STD-881F.")
    equipment: Optional[TrainingEquipment] = Field(default=None)
    services: Optional[TrainingServices] = Field(default=None)
    data: Optional[TrainingData] = Field(default=None)
    facilities: Optional[TrainingFacilities] = Field(default=None)


class TrainingEquipment(Architecture):
    """Equipment. MIL-STD-881F A.4.10.1. WBS 1.9.1."""

    wbs_no: str = Field(default="1.9.1", description="WBS number per MIL-STD-881F.")
    operator_instructional_equipment: Optional[OperatorInstructionalEquipment] = Field(
        default=None
    )
    maintainer_instructional_equipment: Optional[MaintainerInstructionalEquipment] = (
        Field(default=None)
    )


class OperatorInstructionalEquipment(Architecture):
    """Operator Instructional Equipment. MIL-STD-881F A.4.10.1.1. WBS 1.9.1.1."""

    wbs_no: str = Field(default="1.9.1.1", description="WBS number per MIL-STD-881F.")


class MaintainerInstructionalEquipment(Architecture):
    """Maintainer Instructional Equipment. MIL-STD-881F A.4.10.1.2. WBS 1.9.1.2."""

    wbs_no: str = Field(default="1.9.1.2", description="WBS number per MIL-STD-881F.")


class TrainingServices(Architecture):
    """Services. MIL-STD-881F A.4.10.2. WBS 1.9.2."""

    wbs_no: str = Field(default="1.9.2", description="WBS number per MIL-STD-881F.")
    operator_instructional_services: Optional[OperatorInstructionalServices] = Field(
        default=None
    )
    maintainer_instructional_services: Optional[MaintainerInstructionalServices] = (
        Field(default=None)
    )


class OperatorInstructionalServices(Architecture):
    """Operator Instructional Services. MIL-STD-881F A.4.10.2.1. WBS 1.9.2.1."""

    wbs_no: str = Field(default="1.9.2.1", description="WBS number per MIL-STD-881F.")


class MaintainerInstructionalServices(Architecture):
    """Maintainer Instructional Services. MIL-STD-881F A.4.10.2.2. WBS 1.9.2.2."""

    wbs_no: str = Field(default="1.9.2.2", description="WBS number per MIL-STD-881F.")


class TrainingData(Architecture):
    """Data. MIL-STD-881F A.4.10.3. WBS 1.9.3."""

    wbs_no: str = Field(default="1.9.3", description="WBS number per MIL-STD-881F.")


class TrainingFacilities(Architecture):
    """Facilities. MIL-STD-881F A.4.10.4. WBS 1.9.4."""

    wbs_no: str = Field(default="1.9.4", description="WBS number per MIL-STD-881F.")


class Data(Architecture):
    """Data. MIL-STD-881F A.4.11. WBS 1.10."""

    wbs_no: str = Field(default="1.10", description="WBS number per MIL-STD-881F.")
    data_deliverables: Optional[DataDeliverables] = Field(default=None)
    data_repository: Optional[DataRepository] = Field(default=None)
    data_rights: Optional[DataRights] = Field(default=None)


class DataDeliverables(Architecture):
    """Data Deliverables. MIL-STD-881F A.4.11.1. WBS 1.10.1."""

    wbs_no: str = Field(default="1.10.1", description="WBS number per MIL-STD-881F.")


class DataRepository(Architecture):
    """Data Repository. MIL-STD-881F A.4.11.2. WBS 1.10.2."""

    wbs_no: str = Field(default="1.10.2", description="WBS number per MIL-STD-881F.")


class DataRights(Architecture):
    """Data Rights. MIL-STD-881F A.4.11.3. WBS 1.10.3."""

    wbs_no: str = Field(default="1.10.3", description="WBS number per MIL-STD-881F.")


class PeculiarSupportEquipment(Architecture):
    """Peculiar Support Equipment. MIL-STD-881F A.4.12. WBS 1.11."""

    wbs_no: str = Field(default="1.11", description="WBS number per MIL-STD-881F.")
    test_and_measurement_equipment: Optional[PSE_TestAndMeasurementEquipment] = Field(
        default=None
    )
    support_and_handling_equipment: Optional[PSE_SupportAndHandlingEquipment] = Field(
        default=None
    )


class PSE_TestAndMeasurementEquipment(Architecture):  # noqa: N801
    """Test and Measurement Equipment. MIL-STD-881F A.4.12.1. WBS 1.11.1."""

    wbs_no: str = Field(default="1.11.1", description="WBS number per MIL-STD-881F.")
    test_and_measurement_equipment_1: Optional[TIME_AirframeHullVehicle] = Field(
        default=None
    )
    test_and_measurement_equipment_2: Optional[TIME_Propulsion] = Field(default=None)
    test_and_measurement_equipment_3: Optional[TIME_ElectronicsAvionics] = Field(
        default=None
    )
    test_and_measurement_equipment_4: Optional[TIME_OtherMajorSubsystems] = Field(
        default=None
    )


class TIME_AirframeHullVehicle(Architecture):  # noqa: N801
    """Test and Measurement Equipment (Airframe/Hull/Vehicle). MIL-STD-881F A.4.12.1.1. WBS 1.11.1.1."""

    wbs_no: str = Field(default="1.11.1.1", description="WBS number per MIL-STD-881F.")


class TIME_Propulsion(Architecture):  # noqa: N801
    """Test and Measurement Equipment (Propulsion). MIL-STD-881F A.4.12.1.2. WBS 1.11.1.2."""

    wbs_no: str = Field(default="1.11.1.2", description="WBS number per MIL-STD-881F.")


class TIME_ElectronicsAvionics(Architecture):  # noqa: N801
    """Test and Measurement Equipment (Electronics/Avionics). MIL-STD-881F A.4.12.1.3. WBS 1.11.1.3."""

    wbs_no: str = Field(default="1.11.1.3", description="WBS number per MIL-STD-881F.")


class TIME_OtherMajorSubsystems(Architecture):  # noqa: N801
    """Test and Measurement Equipment (Other Major Subsystems). MIL-STD-881F A.4.12.1.4. WBS 1.11.1.4."""

    wbs_no: str = Field(default="1.11.1.4", description="WBS number per MIL-STD-881F.")


class PSE_SupportAndHandlingEquipment(Architecture):  # noqa: N801
    """Support and Handling Equipment. MIL-STD-881F A.4.12.2. WBS 1.11.2."""

    wbs_no: str = Field(default="1.11.2", description="WBS number per MIL-STD-881F.")
    support_and_handling_equipment_1: Optional[SHE_AirframeHullVehicle] = Field(
        default=None
    )
    support_and_handling_equipment_2: Optional[SHE_Propulsion] = Field(default=None)
    support_and_handling_equipment_3: Optional[SHE_ElectronicsAvionics] = Field(
        default=None
    )
    support_and_handling_equipment_4: Optional[SHE_OtherMajorSubsystems] = Field(
        default=None
    )


class SHE_AirframeHullVehicle(Architecture):  # noqa: N801
    """Support and Handling Equipment (Airframe/Hull/Vehicle). MIL-STD-881F A.4.12.2.1. WBS 1.11.2.1."""

    wbs_no: str = Field(default="1.11.2.1", description="WBS number per MIL-STD-881F.")


class SHE_Propulsion(Architecture):  # noqa: N801
    """Support and Handling Equipment (Propulsion). MIL-STD-881F A.4.12.2.2. WBS 1.11.2.2."""

    wbs_no: str = Field(default="1.11.2.2", description="WBS number per MIL-STD-881F.")


class SHE_ElectronicsAvionics(Architecture):  # noqa: N801
    """Support and Handling Equipment (Electronics/Avionics). MIL-STD-881F A.4.12.2.3. WBS 1.11.2.3."""

    wbs_no: str = Field(default="1.11.2.3", description="WBS number per MIL-STD-881F.")


class SHE_OtherMajorSubsystems(Architecture):  # noqa: N801
    """Support and Handling Equipment (Other Major Subsystems). MIL-STD-881F A.4.12.2.4. WBS 1.11.2.4."""

    wbs_no: str = Field(default="1.11.2.4", description="WBS number per MIL-STD-881F.")


class CommonSupportEquipment(Architecture):
    """Common Support Equipment. MIL-STD-881F A.4.13. WBS 1.12."""

    wbs_no: str = Field(default="1.12", description="WBS number per MIL-STD-881F.")
    test_and_measurement_equipment: Optional[CSE_TestAndMeasurementEquipment] = Field(
        default=None
    )
    support_and_handling_equipment: Optional[CSE_SupportAndHandlingEquipment] = Field(
        default=None
    )


class CSE_TestAndMeasurementEquipment(Architecture):  # noqa: N801
    """Test and Measurement Equipment. MIL-STD-881F A.4.13.1. WBS 1.12.1."""

    wbs_no: str = Field(default="1.12.1", description="WBS number per MIL-STD-881F.")
    test_and_measurement_equipment_1: Optional[CSE_TIME_AirframeHullVehicle] = Field(
        default=None
    )
    test_and_measurement_equipment_2: Optional[CSE_TIME_Propulsion] = Field(
        default=None
    )
    test_and_measurement_equipment_3: Optional[CSE_TIME_ElectronicsAvionics] = Field(
        default=None
    )
    test_and_measurement_equipment_4: Optional[CSE_TIME_OtherMajorSubsystems] = Field(
        default=None
    )


class CSE_TIME_AirframeHullVehicle(Architecture):  # noqa: N801
    """Test and Measurement Equipment (Airframe/Hull/Vehicle). MIL-STD-881F A.4.13.1.1. WBS 1.12.1.1."""

    wbs_no: str = Field(default="1.12.1.1", description="WBS number per MIL-STD-881F.")


class CSE_TIME_Propulsion(Architecture):  # noqa: N801
    """Test and Measurement Equipment (Propulsion). MIL-STD-881F A.4.13.1.2. WBS 1.12.1.2."""

    wbs_no: str = Field(default="1.12.1.2", description="WBS number per MIL-STD-881F.")


class CSE_TIME_ElectronicsAvionics(Architecture):  # noqa: N801
    """Test and Measurement Equipment (Electronics/Avionics). MIL-STD-881F A.4.13.1.3. WBS 1.12.1.3."""

    wbs_no: str = Field(default="1.12.1.3", description="WBS number per MIL-STD-881F.")


class CSE_TIME_OtherMajorSubsystems(Architecture):  # noqa: N801
    """Test and Measurement Equipment (Other Major Subsystems). MIL-STD-881F A.4.13.1.4. WBS 1.12.1.4."""

    wbs_no: str = Field(default="1.12.1.4", description="WBS number per MIL-STD-881F.")


class CSE_SupportAndHandlingEquipment(Architecture):  # noqa: N801
    """Support and Handling Equipment. MIL-STD-881F A.4.13.2. WBS 1.12.2."""

    wbs_no: str = Field(default="1.12.2", description="WBS number per MIL-STD-881F.")
    support_and_handling_equipment_1: Optional[CSE_SHE_AirframeHullVehicle] = Field(
        default=None
    )
    support_and_handling_equipment_2: Optional[CSE_SHE_Propulsion] = Field(default=None)
    support_and_handling_equipment_3: Optional[CSE_SHE_ElectronicsAvionics] = Field(
        default=None
    )
    support_and_handling_equipment_4: Optional[CSE_SHE_OtherMajorSubsystems] = Field(
        default=None
    )


class CSE_SHE_AirframeHullVehicle(Architecture):  # noqa: N801
    """Support and Handling Equipment (Airframe/Hull/Vehicle). MIL-STD-881F A.4.13.2.1. WBS 1.12.2.1."""

    wbs_no: str = Field(default="1.12.2.1", description="WBS number per MIL-STD-881F.")


class CSE_SHE_Propulsion(Architecture):  # noqa: N801
    """Support and Handling Equipment (Propulsion). MIL-STD-881F A.4.13.2.2. WBS 1.12.2.2."""

    wbs_no: str = Field(default="1.12.2.2", description="WBS number per MIL-STD-881F.")


class CSE_SHE_ElectronicsAvionics(Architecture):  # noqa: N801
    """Support and Handling Equipment (Electronics/Avionics). MIL-STD-881F A.4.13.2.3. WBS 1.12.2.3."""

    wbs_no: str = Field(default="1.12.2.3", description="WBS number per MIL-STD-881F.")


class CSE_SHE_OtherMajorSubsystems(Architecture):  # noqa: N801
    """Support and Handling Equipment (Other Major Subsystems). MIL-STD-881F A.4.13.2.4. WBS 1.12.2.4."""

    wbs_no: str = Field(default="1.12.2.4", description="WBS number per MIL-STD-881F.")


class OperationalSiteActivation(Architecture):
    """Operational/Site Activation. MIL-STD-881F A.4.14. WBS 1.13."""

    wbs_no: str = Field(default="1.13", description="WBS number per MIL-STD-881F.")
    system_assembly_installation_and_checkout_on_site: Optional[
        SystemAssemblyInstallationAndCheckoutOnSite
    ] = Field(default=None)
    contractor_technical_support: Optional[ContractorTechnicalSupport] = Field(
        default=None
    )
    site_construction: Optional[SiteConstruction] = Field(default=None)
    site_ship_vehicle_conversion: Optional[SiteShipVehicleConversion] = Field(
        default=None
    )
    interim_contractor_support: Optional[InterimContractorSupport] = Field(default=None)


class SystemAssemblyInstallationAndCheckoutOnSite(Architecture):
    """System Assembly, Installation, and Checkout on Site. MIL-STD-881F A.4.14.1. WBS 1.13.1."""

    wbs_no: str = Field(default="1.13.1", description="WBS number per MIL-STD-881F.")


class ContractorTechnicalSupport(Architecture):
    """Contractor Technical Support. MIL-STD-881F A.4.14.2. WBS 1.13.2."""

    wbs_no: str = Field(default="1.13.2", description="WBS number per MIL-STD-881F.")


class SiteConstruction(Architecture):
    """Site Construction. MIL-STD-881F A.4.14.3. WBS 1.13.3."""

    wbs_no: str = Field(default="1.13.3", description="WBS number per MIL-STD-881F.")


class SiteShipVehicleConversion(Architecture):
    """Site/Ship/Vehicle Conversion. MIL-STD-881F A.4.14.4. WBS 1.13.4."""

    wbs_no: str = Field(default="1.13.4", description="WBS number per MIL-STD-881F.")


class InterimContractorSupport(Architecture):
    """Interim Contractor Support. MIL-STD-881F A.4.14.5. WBS 1.13.5."""

    wbs_no: str = Field(default="1.13.5", description="WBS number per MIL-STD-881F.")


class ContractorLogisticsSupport(Architecture):
    """Contractor Logistics Support. MIL-STD-881F A.4.15. WBS 1.14."""

    wbs_no: str = Field(default="1.14", description="WBS number per MIL-STD-881F.")


class IndustrialFacilities(Architecture):
    """Industrial Facilities. MIL-STD-881F A.4.16. WBS 1.15."""

    wbs_no: str = Field(default="1.15", description="WBS number per MIL-STD-881F.")
    construction_conversion_expansion: Optional[ConstructionConversionExpansion] = (
        Field(default=None)
    )
    equipment_acquisition_or_modernization: Optional[
        EquipmentAcquisitionOrModernization
    ] = Field(default=None)
    maintenance: Optional[MaintenanceIndustrialFacilities] = Field(default=None)


class ConstructionConversionExpansion(Architecture):
    """Construction/Conversion/Expansion. MIL-STD-881F A.4.16.1. WBS 1.15.1."""

    wbs_no: str = Field(default="1.15.1", description="WBS number per MIL-STD-881F.")


class EquipmentAcquisitionOrModernization(Architecture):
    """Equipment Acquisition or Modernization. MIL-STD-881F A.4.16.2. WBS 1.15.2."""

    wbs_no: str = Field(default="1.15.2", description="WBS number per MIL-STD-881F.")


class MaintenanceIndustrialFacilities(Architecture):
    """Maintenance (Industrial Facilities). MIL-STD-881F A.4.16.3. WBS 1.15.3."""

    wbs_no: str = Field(default="1.15.3", description="WBS number per MIL-STD-881F.")


class InitialSparesAndRepairParts(Architecture):
    """Initial Spares and Repair Parts. MIL-STD-881F A.4.17. WBS 1.16."""

    wbs_no: str = Field(default="1.16", description="WBS number per MIL-STD-881F.")


Airframe.model_rebuild()
VehicleSubsystems.model_rebuild()
Avionics.model_rebuild()
DevelopmentalTestAndEvaluation.model_rebuild()
OperationalTestAndEvaluation.model_rebuild()
TrainingEquipment.model_rebuild()
TrainingServices.model_rebuild()
PSE_TestAndMeasurementEquipment.model_rebuild()  # noqa: N801
PSE_SupportAndHandlingEquipment.model_rebuild()  # noqa: N801
CSE_TestAndMeasurementEquipment.model_rebuild()  # noqa: N801
CSE_SupportAndHandlingEquipment.model_rebuild()  # noqa: N801
AircraftSystem.model_rebuild()
AirVehicle.model_rebuild()
GroundHostSegment.model_rebuild()
PayloadMissionSystem.model_rebuild()
SystemsEngineering.model_rebuild()
ProgramManagement.model_rebuild()
SystemTestAndEvaluation.model_rebuild()
Training.model_rebuild()
Data.model_rebuild()
PeculiarSupportEquipment.model_rebuild()
CommonSupportEquipment.model_rebuild()
OperationalSiteActivation.model_rebuild()
IndustrialFacilities.model_rebuild()
