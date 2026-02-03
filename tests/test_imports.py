import pytest


class TestImports:
    def test_import_aircraft_data_hierarchy(self):
        try:
            from aircraft_data_hierarchy import (  # noqa: PLC0415
                Behavior,
                CommonBaseModel,
                DataExchange,
                Requirements,
            )

            assert Behavior is not None
            assert CommonBaseModel is not None
            assert DataExchange is not None
            assert Requirements is not None
        except ImportError as exc:
            pytest.fail(f"Failed to import from aircraft_data_hierarchy: {exc}")

    def test_import_work_breakdown_structure(self):
        try:
            from aircraft_data_hierarchy.work_breakdown_structure import (  # noqa: PLC0415
                AircraftSystem,
                Equipment,
            )

            assert AircraftSystem is not None
            assert Equipment is not None
        except ImportError as exc:
            pytest.fail(
                "Failed to import from aircraft_data_hierarchy.work_breakdown_structure: "
                f"{exc}"
            )

    def test_import_work_breakdown_structure_airframe(self):
        try:
            from aircraft_data_hierarchy.work_breakdown_structure.airframe import (  # noqa: PLC0415
                AerodynamicsData,
                Component,
                Loft,
            )

            assert AerodynamicsData is not None
            assert Component is not None
            assert Loft is not None
        except ImportError as exc:
            pytest.fail(
                "Failed to import from aircraft_data_hierarchy.work_breakdown_structure.airframe: "
                f"{exc}"
            )

    def test_import_work_breakdown_structure_propulsion(self):
        try:
            from aircraft_data_hierarchy.work_breakdown_structure.propulsion import (  # noqa: PLC0415
                Propulsion,
                PropulsionCycle,
                PropulsionGeometry,
            )

            assert Propulsion is not None
            assert PropulsionCycle is not None
            assert PropulsionGeometry is not None
        except ImportError as exc:
            pytest.fail(
                "Failed to import from aircraft_data_hierarchy.work_breakdown_structure.propulsion: "
                f"{exc}"
            )

    def test_import_work_breakdown_structure_systems(self):
        try:
            from aircraft_data_hierarchy.work_breakdown_structure.systems import (  # noqa: PLC0415
                System,
                SystemAttributes,
                create_system_diagram,
            )

            assert System is not None
            assert SystemAttributes is not None
            assert create_system_diagram is not None
        except ImportError as exc:
            pytest.fail(
                "Failed to import from aircraft_data_hierarchy.work_breakdown_structure.systems: "
                f"{exc}"
            )
