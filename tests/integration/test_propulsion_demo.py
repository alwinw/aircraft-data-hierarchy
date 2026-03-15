from __future__ import annotations

import json
from pathlib import Path

from adh.wbs.propulsion import Propulsion
from adh.wbs.propulsion.propulsion_cycle import Inlet, PropulsionCycle

STEP1_JSON = Path("demos/PropulsionDemo/output_files/step1_adh.json")


def test_propulsion_step1_fixture_parseable():
    """step1_adh.json is valid JSON with expected top-level structure."""
    data = json.loads(STEP1_JSON.read_text())
    assert "OuterNest" in data
    nest = data["OuterNest"]
    assert nest["name"] == "Engine"
    assert "cycle" in nest
    assert "design_point" in nest["cycle"]
    assert len(nest["cycle"]["design_point"]["elements"]) > 0


def test_propulsion_cycle_programmatic():
    """PropulsionCycle can be built programmatically with engine elements."""
    inlet = Inlet(name="inlet", type="inlet", mn=0.751, ram_recovery=0.999)
    cycle = PropulsionCycle(name="TestCycle", elements=[inlet])
    assert cycle.name == "TestCycle"
    assert len(cycle.elements) == 1


def test_propulsion_minimal():
    """Propulsion validates with name and description fields."""
    prop = Propulsion(name="Engine", description="Main engine component")
    assert prop.name == "Engine"
    assert prop.description == "Main engine component"
