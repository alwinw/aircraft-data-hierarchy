from __future__ import annotations

import json
from pathlib import Path

from adh.wbs import AircraftSystem

FIXTURE = Path("demos/NacelleDemo/aircraft_system.json")


def test_nacelle_demo_loads():
    """Smoke test: NacelleDemo JSON loads without error."""
    data = json.loads(FIXTURE.read_text())
    system = AircraftSystem.model_validate(data["AircraftSystem"])
    assert system.wbs_no == "1.0"


def test_nacelle_demo_nacelle_in_extra():
    """Nacelle data accessible via model_extra (fixture uses PascalCase keys)."""
    data = json.loads(FIXTURE.read_text())
    system = AircraftSystem.model_validate(data["AircraftSystem"])
    # JSON uses PascalCase field names so all children land in model_extra
    airframe = system.model_extra["AirVehicle"]["Airframe"]
    nacelle = airframe["Nacelle"]
    assert nacelle["wbs_no"] == "1.2.2.5"
    assert "geometry" in nacelle
