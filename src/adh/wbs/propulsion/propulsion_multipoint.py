"""Multi-point propulsion cycle containers (analysis containers, not WBS nodes)."""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from adh.msosa.metadata import NodeMetaMixin
from adh.wbs.propulsion.propulsion_cycle import PropulsionCycle


class FlightConditions(NodeMetaMixin, BaseModel):
    """Flight conditions for an off-design point."""

    mn: Optional[list[float]] = None
    alt: Optional[list[float]] = None
    d_ts: Optional[float] = None
    W: Optional[list[float]] = None


class OffDesignPoint(NodeMetaMixin, BaseModel):
    """A single off-design operating point."""

    flight_conditions_od: Optional[FlightConditions] = None
    PC: Optional[list[float]] = None
    throttle_mode: str = Field(default="T4")


class MultiPointCycle(NodeMetaMixin, BaseModel):
    """Engine cycle with a design point and one or more off-design points."""

    design_point: PropulsionCycle
    od_points: list[OffDesignPoint]
    global_des_od_connections: Optional[dict] = None
    design_constants: Optional[dict] = None
    seq_points: Optional[list[str]] = None
