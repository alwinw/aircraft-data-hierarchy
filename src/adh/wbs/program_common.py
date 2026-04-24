# Generated from scripts/taxonomy/program_common.yaml by scripts/gen_wbs_classes.py
# Re-run the generator if taxonomy/*.yaml files change.
# Hand edits to this file are preserved across --check runs,
# but class definitions, wbs_no defaults, and child fields will be
# overwritten if the generator is re-run in write mode.

from __future__ import annotations

from typing import Optional

from pydantic import Field

from adh.msosa.architecture import Architecture, MSoSAMixin


class AircraftSystemSoftwareRelease(MSoSAMixin, Architecture):
    """Aircraft System Software Release. MIL-STD-881F A.4.6. WBS 1.5."""

    wbs_no: str = Field(default="1.5", description="WBS number per MIL-STD-881F.")


class SystemsEngineering(MSoSAMixin, Architecture):
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


class SoftwareSystemsEngineering(MSoSAMixin, Architecture):
    """Software Systems Engineering. MIL-STD-881F A.4.7.1. WBS 1.6.1."""

    wbs_no: str = Field(default="1.6.1", description="WBS number per MIL-STD-881F.")


class IntegratedLogisticsSupportSystemsEngineering(MSoSAMixin, Architecture):
    """Integrated Logistics Support Systems Engineering. MIL-STD-881F A.4.7.2. WBS 1.6.2."""

    wbs_no: str = Field(default="1.6.2", description="WBS number per MIL-STD-881F.")


class CybersecuritySystemsEngineering(MSoSAMixin, Architecture):
    """Cybersecurity Systems Engineering. MIL-STD-881F A.4.7.3. WBS 1.6.3."""

    wbs_no: str = Field(default="1.6.3", description="WBS number per MIL-STD-881F.")


class CoreSystemsEngineering(MSoSAMixin, Architecture):
    """Core Systems Engineering. MIL-STD-881F A.4.7.4. WBS 1.6.4."""

    wbs_no: str = Field(default="1.6.4", description="WBS number per MIL-STD-881F.")


class OtherSystemsEngineering(MSoSAMixin, Architecture):
    """Other Systems Engineering. MIL-STD-881F A.4.7.5. WBS 1.6.5."""

    wbs_no: str = Field(default="1.6.5", description="WBS number per MIL-STD-881F.")


class ProgramManagement(MSoSAMixin, Architecture):
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


class SoftwareProgramManagement(MSoSAMixin, Architecture):
    """Software Program Management. MIL-STD-881F A.4.8.1. WBS 1.7.1."""

    wbs_no: str = Field(default="1.7.1", description="WBS number per MIL-STD-881F.")


class IntegratedLogisticsSupportProgramManagement(MSoSAMixin, Architecture):
    """Integrated Logistics Support Program Management. MIL-STD-881F A.4.8.2. WBS 1.7.2."""

    wbs_no: str = Field(default="1.7.2", description="WBS number per MIL-STD-881F.")


class CybersecurityManagement(MSoSAMixin, Architecture):
    """Cybersecurity Management. MIL-STD-881F A.4.8.3. WBS 1.7.3."""

    wbs_no: str = Field(default="1.7.3", description="WBS number per MIL-STD-881F.")


class CoreProgramManagement(MSoSAMixin, Architecture):
    """Core Program Management. MIL-STD-881F A.4.8.4. WBS 1.7.4."""

    wbs_no: str = Field(default="1.7.4", description="WBS number per MIL-STD-881F.")


class OtherProgramManagement(MSoSAMixin, Architecture):
    """Other Program Management. MIL-STD-881F A.4.8.5. WBS 1.7.5."""

    wbs_no: str = Field(default="1.7.5", description="WBS number per MIL-STD-881F.")


class SystemTestAndEvaluation(MSoSAMixin, Architecture):
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


class DevelopmentalTestAndEvaluation(MSoSAMixin, Architecture):
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


class SystemAcceptanceTest(MSoSAMixin, Architecture):
    """System Acceptance Test. MIL-STD-881F A.4.9.1.1. WBS 1.8.1.1."""

    wbs_no: str = Field(default="1.8.1.1", description="WBS number per MIL-STD-881F.")


class WindTunnelTests(MSoSAMixin, Architecture):
    """Wind Tunnel Tests. MIL-STD-881F A.4.9.1.2. WBS 1.8.1.2."""

    wbs_no: str = Field(default="1.8.1.2", description="WBS number per MIL-STD-881F.")


class StructuralTests(MSoSAMixin, Architecture):
    """Structural Tests. MIL-STD-881F A.4.9.1.3. WBS 1.8.1.3."""

    wbs_no: str = Field(default="1.8.1.3", description="WBS number per MIL-STD-881F.")


class DTE_FlightTests(MSoSAMixin, Architecture):  # noqa: N801
    """Flight Tests. MIL-STD-881F A.4.9.1.4. WBS 1.8.1.4."""

    wbs_no: str = Field(default="1.8.1.4", description="WBS number per MIL-STD-881F.")


class DTE_GroundTests(MSoSAMixin, Architecture):  # noqa: N801
    """Ground Tests. MIL-STD-881F A.4.9.1.5. WBS 1.8.1.5."""

    wbs_no: str = Field(default="1.8.1.5", description="WBS number per MIL-STD-881F.")


class DTE_CybersecurityTestAndEvaluation(MSoSAMixin, Architecture):  # noqa: N801
    """Cybersecurity Test and Evaluation. MIL-STD-881F A.4.9.1.6. WBS 1.8.1.6."""

    wbs_no: str = Field(default="1.8.1.6", description="WBS number per MIL-STD-881F.")


class OtherDTETests(MSoSAMixin, Architecture):
    """Other DT&E Tests. MIL-STD-881F A.4.9.1.7. WBS 1.8.1.7."""

    wbs_no: str = Field(default="1.8.1.7", description="WBS number per MIL-STD-881F.")


class OperationalTestAndEvaluation(MSoSAMixin, Architecture):
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


class LimitedUserEvaluation(MSoSAMixin, Architecture):
    """Limited User Evaluation. MIL-STD-881F A.4.9.2.1. WBS 1.8.2.1."""

    wbs_no: str = Field(default="1.8.2.1", description="WBS number per MIL-STD-881F.")


class InteroperabilityTesting(MSoSAMixin, Architecture):
    """Interoperability Testing. MIL-STD-881F A.4.9.2.2. WBS 1.8.2.2."""

    wbs_no: str = Field(default="1.8.2.2", description="WBS number per MIL-STD-881F.")


class OTE_FlightTests(MSoSAMixin, Architecture):  # noqa: N801
    """Flight Tests. MIL-STD-881F A.4.9.2.3. WBS 1.8.2.3."""

    wbs_no: str = Field(default="1.8.2.3", description="WBS number per MIL-STD-881F.")


class OTE_GroundTests(MSoSAMixin, Architecture):  # noqa: N801
    """Ground Tests. MIL-STD-881F A.4.9.2.4. WBS 1.8.2.4."""

    wbs_no: str = Field(default="1.8.2.4", description="WBS number per MIL-STD-881F.")


class OTE_CybersecurityTestAndEvaluation(MSoSAMixin, Architecture):  # noqa: N801
    """Cybersecurity Test and Evaluation. MIL-STD-881F A.4.9.2.5. WBS 1.8.2.5."""

    wbs_no: str = Field(default="1.8.2.5", description="WBS number per MIL-STD-881F.")


class OtherOTETests(MSoSAMixin, Architecture):
    """Other OT&E Tests. MIL-STD-881F A.4.9.2.6. WBS 1.8.2.6."""

    wbs_no: str = Field(default="1.8.2.6", description="WBS number per MIL-STD-881F.")


class LiveFireTestAndEvaluation(MSoSAMixin, Architecture):
    """Live Fire Test and Evaluation. MIL-STD-881F A.4.9.3. WBS 1.8.3."""

    wbs_no: str = Field(default="1.8.3", description="WBS number per MIL-STD-881F.")


class MockupsSystemIntegrationLabs(MSoSAMixin, Architecture):
    """Mock-ups/System Integration Labs. MIL-STD-881F A.4.9.4. WBS 1.8.4."""

    wbs_no: str = Field(default="1.8.4", description="WBS number per MIL-STD-881F.")


class TestAndEvaluationSupport(MSoSAMixin, Architecture):
    """Test and Evaluation Support. MIL-STD-881F A.4.9.5. WBS 1.8.5."""

    wbs_no: str = Field(default="1.8.5", description="WBS number per MIL-STD-881F.")


class TestFacilities(MSoSAMixin, Architecture):
    """Test Facilities. MIL-STD-881F A.4.9.6. WBS 1.8.6."""

    wbs_no: str = Field(default="1.8.6", description="WBS number per MIL-STD-881F.")


class Training(MSoSAMixin, Architecture):
    """Training. MIL-STD-881F A.4.10. WBS 1.9."""

    wbs_no: str = Field(default="1.9", description="WBS number per MIL-STD-881F.")
    equipment: Optional[TrainingEquipment] = Field(default=None)
    services: Optional[TrainingServices] = Field(default=None)
    data: Optional[TrainingData] = Field(default=None)
    facilities: Optional[TrainingFacilities] = Field(default=None)


class TrainingEquipment(MSoSAMixin, Architecture):
    """Equipment. MIL-STD-881F A.4.10.1. WBS 1.9.1."""

    wbs_no: str = Field(default="1.9.1", description="WBS number per MIL-STD-881F.")
    operator_instructional_equipment: Optional[OperatorInstructionalEquipment] = Field(
        default=None
    )
    maintainer_instructional_equipment: Optional[MaintainerInstructionalEquipment] = (
        Field(default=None)
    )


class OperatorInstructionalEquipment(MSoSAMixin, Architecture):
    """Operator Instructional Equipment. MIL-STD-881F A.4.10.1.1. WBS 1.9.1.1."""

    wbs_no: str = Field(default="1.9.1.1", description="WBS number per MIL-STD-881F.")


class MaintainerInstructionalEquipment(MSoSAMixin, Architecture):
    """Maintainer Instructional Equipment. MIL-STD-881F A.4.10.1.2. WBS 1.9.1.2."""

    wbs_no: str = Field(default="1.9.1.2", description="WBS number per MIL-STD-881F.")


class TrainingServices(MSoSAMixin, Architecture):
    """Services. MIL-STD-881F A.4.10.2. WBS 1.9.2."""

    wbs_no: str = Field(default="1.9.2", description="WBS number per MIL-STD-881F.")
    operator_instructional_services: Optional[OperatorInstructionalServices] = Field(
        default=None
    )
    maintainer_instructional_services: Optional[MaintainerInstructionalServices] = (
        Field(default=None)
    )


class OperatorInstructionalServices(MSoSAMixin, Architecture):
    """Operator Instructional Services. MIL-STD-881F A.4.10.2.1. WBS 1.9.2.1."""

    wbs_no: str = Field(default="1.9.2.1", description="WBS number per MIL-STD-881F.")


class MaintainerInstructionalServices(MSoSAMixin, Architecture):
    """Maintainer Instructional Services. MIL-STD-881F A.4.10.2.2. WBS 1.9.2.2."""

    wbs_no: str = Field(default="1.9.2.2", description="WBS number per MIL-STD-881F.")


class TrainingData(MSoSAMixin, Architecture):
    """Data. MIL-STD-881F A.4.10.3. WBS 1.9.3."""

    wbs_no: str = Field(default="1.9.3", description="WBS number per MIL-STD-881F.")


class TrainingFacilities(MSoSAMixin, Architecture):
    """Facilities. MIL-STD-881F A.4.10.4. WBS 1.9.4."""

    wbs_no: str = Field(default="1.9.4", description="WBS number per MIL-STD-881F.")


class Data(MSoSAMixin, Architecture):
    """Data. MIL-STD-881F A.4.11. WBS 1.10."""

    wbs_no: str = Field(default="1.10", description="WBS number per MIL-STD-881F.")
    data_deliverables: Optional[DataDeliverables] = Field(default=None)
    data_repository: Optional[DataRepository] = Field(default=None)
    data_rights: Optional[DataRights] = Field(default=None)


class DataDeliverables(MSoSAMixin, Architecture):
    """Data Deliverables. MIL-STD-881F A.4.11.1. WBS 1.10.1."""

    wbs_no: str = Field(default="1.10.1", description="WBS number per MIL-STD-881F.")


class DataRepository(MSoSAMixin, Architecture):
    """Data Repository. MIL-STD-881F A.4.11.2. WBS 1.10.2."""

    wbs_no: str = Field(default="1.10.2", description="WBS number per MIL-STD-881F.")


class DataRights(MSoSAMixin, Architecture):
    """Data Rights. MIL-STD-881F A.4.11.3. WBS 1.10.3."""

    wbs_no: str = Field(default="1.10.3", description="WBS number per MIL-STD-881F.")


class PeculiarSupportEquipment(MSoSAMixin, Architecture):
    """Peculiar Support Equipment. MIL-STD-881F A.4.12. WBS 1.11."""

    wbs_no: str = Field(default="1.11", description="WBS number per MIL-STD-881F.")
    test_and_measurement_equipment: Optional[PSE_TestAndMeasurementEquipment] = Field(
        default=None
    )
    support_and_handling_equipment: Optional[PSE_SupportAndHandlingEquipment] = Field(
        default=None
    )


class PSE_TestAndMeasurementEquipment(MSoSAMixin, Architecture):  # noqa: N801
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


class TIME_AirframeHullVehicle(MSoSAMixin, Architecture):  # noqa: N801
    """Test and Measurement Equipment (Airframe/Hull/Vehicle). MIL-STD-881F A.4.12.1.1. WBS 1.11.1.1."""

    wbs_no: str = Field(default="1.11.1.1", description="WBS number per MIL-STD-881F.")


class TIME_Propulsion(MSoSAMixin, Architecture):  # noqa: N801
    """Test and Measurement Equipment (Propulsion). MIL-STD-881F A.4.12.1.2. WBS 1.11.1.2."""

    wbs_no: str = Field(default="1.11.1.2", description="WBS number per MIL-STD-881F.")


class TIME_ElectronicsAvionics(MSoSAMixin, Architecture):  # noqa: N801
    """Test and Measurement Equipment (Electronics/Avionics). MIL-STD-881F A.4.12.1.3. WBS 1.11.1.3."""

    wbs_no: str = Field(default="1.11.1.3", description="WBS number per MIL-STD-881F.")


class TIME_OtherMajorSubsystems(MSoSAMixin, Architecture):  # noqa: N801
    """Test and Measurement Equipment (Other Major Subsystems). MIL-STD-881F A.4.12.1.4. WBS 1.11.1.4."""

    wbs_no: str = Field(default="1.11.1.4", description="WBS number per MIL-STD-881F.")


class PSE_SupportAndHandlingEquipment(MSoSAMixin, Architecture):  # noqa: N801
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


class SHE_AirframeHullVehicle(MSoSAMixin, Architecture):  # noqa: N801
    """Support and Handling Equipment (Airframe/Hull/Vehicle). MIL-STD-881F A.4.12.2.1. WBS 1.11.2.1."""

    wbs_no: str = Field(default="1.11.2.1", description="WBS number per MIL-STD-881F.")


class SHE_Propulsion(MSoSAMixin, Architecture):  # noqa: N801
    """Support and Handling Equipment (Propulsion). MIL-STD-881F A.4.12.2.2. WBS 1.11.2.2."""

    wbs_no: str = Field(default="1.11.2.2", description="WBS number per MIL-STD-881F.")


class SHE_ElectronicsAvionics(MSoSAMixin, Architecture):  # noqa: N801
    """Support and Handling Equipment (Electronics/Avionics). MIL-STD-881F A.4.12.2.3. WBS 1.11.2.3."""

    wbs_no: str = Field(default="1.11.2.3", description="WBS number per MIL-STD-881F.")


class SHE_OtherMajorSubsystems(MSoSAMixin, Architecture):  # noqa: N801
    """Support and Handling Equipment (Other Major Subsystems). MIL-STD-881F A.4.12.2.4. WBS 1.11.2.4."""

    wbs_no: str = Field(default="1.11.2.4", description="WBS number per MIL-STD-881F.")


class CommonSupportEquipment(MSoSAMixin, Architecture):
    """Common Support Equipment. MIL-STD-881F A.4.13. WBS 1.12."""

    wbs_no: str = Field(default="1.12", description="WBS number per MIL-STD-881F.")
    test_and_measurement_equipment: Optional[CSE_TestAndMeasurementEquipment] = Field(
        default=None
    )
    support_and_handling_equipment: Optional[CSE_SupportAndHandlingEquipment] = Field(
        default=None
    )


class CSE_TestAndMeasurementEquipment(MSoSAMixin, Architecture):  # noqa: N801
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


class CSE_TIME_AirframeHullVehicle(MSoSAMixin, Architecture):  # noqa: N801
    """Test and Measurement Equipment (Airframe/Hull/Vehicle). MIL-STD-881F A.4.13.1.1. WBS 1.12.1.1."""

    wbs_no: str = Field(default="1.12.1.1", description="WBS number per MIL-STD-881F.")


class CSE_TIME_Propulsion(MSoSAMixin, Architecture):  # noqa: N801
    """Test and Measurement Equipment (Propulsion). MIL-STD-881F A.4.13.1.2. WBS 1.12.1.2."""

    wbs_no: str = Field(default="1.12.1.2", description="WBS number per MIL-STD-881F.")


class CSE_TIME_ElectronicsAvionics(MSoSAMixin, Architecture):  # noqa: N801
    """Test and Measurement Equipment (Electronics/Avionics). MIL-STD-881F A.4.13.1.3. WBS 1.12.1.3."""

    wbs_no: str = Field(default="1.12.1.3", description="WBS number per MIL-STD-881F.")


class CSE_TIME_OtherMajorSubsystems(MSoSAMixin, Architecture):  # noqa: N801
    """Test and Measurement Equipment (Other Major Subsystems). MIL-STD-881F A.4.13.1.4. WBS 1.12.1.4."""

    wbs_no: str = Field(default="1.12.1.4", description="WBS number per MIL-STD-881F.")


class CSE_SupportAndHandlingEquipment(MSoSAMixin, Architecture):  # noqa: N801
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


class CSE_SHE_AirframeHullVehicle(MSoSAMixin, Architecture):  # noqa: N801
    """Support and Handling Equipment (Airframe/Hull/Vehicle). MIL-STD-881F A.4.13.2.1. WBS 1.12.2.1."""

    wbs_no: str = Field(default="1.12.2.1", description="WBS number per MIL-STD-881F.")


class CSE_SHE_Propulsion(MSoSAMixin, Architecture):  # noqa: N801
    """Support and Handling Equipment (Propulsion). MIL-STD-881F A.4.13.2.2. WBS 1.12.2.2."""

    wbs_no: str = Field(default="1.12.2.2", description="WBS number per MIL-STD-881F.")


class CSE_SHE_ElectronicsAvionics(MSoSAMixin, Architecture):  # noqa: N801
    """Support and Handling Equipment (Electronics/Avionics). MIL-STD-881F A.4.13.2.3. WBS 1.12.2.3."""

    wbs_no: str = Field(default="1.12.2.3", description="WBS number per MIL-STD-881F.")


class CSE_SHE_OtherMajorSubsystems(MSoSAMixin, Architecture):  # noqa: N801
    """Support and Handling Equipment (Other Major Subsystems). MIL-STD-881F A.4.13.2.4. WBS 1.12.2.4."""

    wbs_no: str = Field(default="1.12.2.4", description="WBS number per MIL-STD-881F.")


class OperationalSiteActivation(MSoSAMixin, Architecture):
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


class SystemAssemblyInstallationAndCheckoutOnSite(MSoSAMixin, Architecture):
    """System Assembly, Installation, and Checkout on Site. MIL-STD-881F A.4.14.1. WBS 1.13.1."""

    wbs_no: str = Field(default="1.13.1", description="WBS number per MIL-STD-881F.")


class ContractorTechnicalSupport(MSoSAMixin, Architecture):
    """Contractor Technical Support. MIL-STD-881F A.4.14.2. WBS 1.13.2."""

    wbs_no: str = Field(default="1.13.2", description="WBS number per MIL-STD-881F.")


class SiteConstruction(MSoSAMixin, Architecture):
    """Site Construction. MIL-STD-881F A.4.14.3. WBS 1.13.3."""

    wbs_no: str = Field(default="1.13.3", description="WBS number per MIL-STD-881F.")


class SiteShipVehicleConversion(MSoSAMixin, Architecture):
    """Site/Ship/Vehicle Conversion. MIL-STD-881F A.4.14.4. WBS 1.13.4."""

    wbs_no: str = Field(default="1.13.4", description="WBS number per MIL-STD-881F.")


class InterimContractorSupport(MSoSAMixin, Architecture):
    """Interim Contractor Support. MIL-STD-881F A.4.14.5. WBS 1.13.5."""

    wbs_no: str = Field(default="1.13.5", description="WBS number per MIL-STD-881F.")


class ContractorLogisticsSupport(MSoSAMixin, Architecture):
    """Contractor Logistics Support. MIL-STD-881F A.4.15. WBS 1.14."""

    wbs_no: str = Field(default="1.14", description="WBS number per MIL-STD-881F.")


class IndustrialFacilities(MSoSAMixin, Architecture):
    """Industrial Facilities. MIL-STD-881F A.4.16. WBS 1.15."""

    wbs_no: str = Field(default="1.15", description="WBS number per MIL-STD-881F.")
    construction_conversion_expansion: Optional[ConstructionConversionExpansion] = (
        Field(default=None)
    )
    equipment_acquisition_or_modernization: Optional[
        EquipmentAcquisitionOrModernization
    ] = Field(default=None)
    maintenance: Optional[MaintenanceIndustrialFacilities] = Field(default=None)


class ConstructionConversionExpansion(MSoSAMixin, Architecture):
    """Construction/Conversion/Expansion. MIL-STD-881F A.4.16.1. WBS 1.15.1."""

    wbs_no: str = Field(default="1.15.1", description="WBS number per MIL-STD-881F.")


class EquipmentAcquisitionOrModernization(MSoSAMixin, Architecture):
    """Equipment Acquisition or Modernization. MIL-STD-881F A.4.16.2. WBS 1.15.2."""

    wbs_no: str = Field(default="1.15.2", description="WBS number per MIL-STD-881F.")


class MaintenanceIndustrialFacilities(MSoSAMixin, Architecture):
    """Maintenance (Industrial Facilities). MIL-STD-881F A.4.16.3. WBS 1.15.3."""

    wbs_no: str = Field(default="1.15.3", description="WBS number per MIL-STD-881F.")


class InitialSparesAndRepairParts(MSoSAMixin, Architecture):
    """Initial Spares and Repair Parts. MIL-STD-881F A.4.17. WBS 1.16."""

    wbs_no: str = Field(default="1.16", description="WBS number per MIL-STD-881F.")


DevelopmentalTestAndEvaluation.model_rebuild()
OperationalTestAndEvaluation.model_rebuild()
TrainingEquipment.model_rebuild()
TrainingServices.model_rebuild()
PSE_TestAndMeasurementEquipment.model_rebuild()  # noqa: N801
PSE_SupportAndHandlingEquipment.model_rebuild()  # noqa: N801
CSE_TestAndMeasurementEquipment.model_rebuild()  # noqa: N801
CSE_SupportAndHandlingEquipment.model_rebuild()  # noqa: N801
SystemsEngineering.model_rebuild()
ProgramManagement.model_rebuild()
SystemTestAndEvaluation.model_rebuild()
Training.model_rebuild()
Data.model_rebuild()
PeculiarSupportEquipment.model_rebuild()
CommonSupportEquipment.model_rebuild()
OperationalSiteActivation.model_rebuild()
IndustrialFacilities.model_rebuild()

__all__ = [
    "AircraftSystemSoftwareRelease",
    "CommonSupportEquipment",
    "ConstructionConversionExpansion",
    "ContractorLogisticsSupport",
    "ContractorTechnicalSupport",
    "CoreProgramManagement",
    "CoreSystemsEngineering",
    "CSE_SHE_AirframeHullVehicle",
    "CSE_SHE_ElectronicsAvionics",
    "CSE_SHE_OtherMajorSubsystems",
    "CSE_SHE_Propulsion",
    "CSE_SupportAndHandlingEquipment",
    "CSE_TestAndMeasurementEquipment",
    "CSE_TIME_AirframeHullVehicle",
    "CSE_TIME_ElectronicsAvionics",
    "CSE_TIME_OtherMajorSubsystems",
    "CSE_TIME_Propulsion",
    "CybersecurityManagement",
    "CybersecuritySystemsEngineering",
    "Data",
    "DataDeliverables",
    "DataRepository",
    "DataRights",
    "DevelopmentalTestAndEvaluation",
    "DTE_CybersecurityTestAndEvaluation",
    "DTE_FlightTests",
    "DTE_GroundTests",
    "EquipmentAcquisitionOrModernization",
    "IndustrialFacilities",
    "InitialSparesAndRepairParts",
    "IntegratedLogisticsSupportProgramManagement",
    "IntegratedLogisticsSupportSystemsEngineering",
    "InterimContractorSupport",
    "InteroperabilityTesting",
    "LimitedUserEvaluation",
    "LiveFireTestAndEvaluation",
    "MaintainerInstructionalEquipment",
    "MaintainerInstructionalServices",
    "MaintenanceIndustrialFacilities",
    "MockupsSystemIntegrationLabs",
    "OperationalSiteActivation",
    "OperationalTestAndEvaluation",
    "OperatorInstructionalEquipment",
    "OperatorInstructionalServices",
    "OTE_CybersecurityTestAndEvaluation",
    "OTE_FlightTests",
    "OTE_GroundTests",
    "OtherDTETests",
    "OtherOTETests",
    "OtherProgramManagement",
    "OtherSystemsEngineering",
    "PeculiarSupportEquipment",
    "ProgramManagement",
    "PSE_SupportAndHandlingEquipment",
    "PSE_TestAndMeasurementEquipment",
    "SHE_AirframeHullVehicle",
    "SHE_ElectronicsAvionics",
    "SHE_OtherMajorSubsystems",
    "SHE_Propulsion",
    "SiteConstruction",
    "SiteShipVehicleConversion",
    "SoftwareProgramManagement",
    "SoftwareSystemsEngineering",
    "StructuralTests",
    "SystemAcceptanceTest",
    "SystemAssemblyInstallationAndCheckoutOnSite",
    "SystemsEngineering",
    "SystemTestAndEvaluation",
    "TestAndEvaluationSupport",
    "TestFacilities",
    "TIME_AirframeHullVehicle",
    "TIME_ElectronicsAvionics",
    "TIME_OtherMajorSubsystems",
    "TIME_Propulsion",
    "Training",
    "TrainingData",
    "TrainingEquipment",
    "TrainingFacilities",
    "TrainingServices",
    "WindTunnelTests",
]
