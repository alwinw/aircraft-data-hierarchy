"""Shared recursive child views for architecture nodes."""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from adh.msosa.behavior import Behaviors
from adh.msosa.performance import Performances
from adh.msosa.requirements import Requirements


class MSoSAMixin(BaseModel):
    """Add recursive MSoSA child views to a true architecture node."""

    requirements: Optional[Requirements] = Field(
        default=None,
        description="Requirements child view for this architecture node.",
    )
    performance: Optional[Performances] = Field(
        default=None,
        description="Performance child view for this architecture node.",
    )
    behavior: Optional[Behaviors] = Field(
        default=None,
        description="Behavior child view for this architecture node.",
    )


__all__ = ["MSoSAMixin"]
