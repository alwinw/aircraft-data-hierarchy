from pydantic import BaseModel

from adh.msosa.metadata import NodeMetaMixin


class PropulsionGeometry(NodeMetaMixin, BaseModel):
    """Propulsion geometry parameters. Content deferred to PLAN_6 (Fix #5)."""

    pass
