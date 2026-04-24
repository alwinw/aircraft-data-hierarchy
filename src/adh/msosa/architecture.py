"""
ADH Architecture (Arch) Models.

Architecture models describe the structural representation of systems, subsystems,
components, and their interconnection across all references.

The architecture parent nodes in the [ADH][1] are aligned with
[SAE SAWE RP A-8, 2015a Weight and Balance][2].

[1]: https://ntrs.nasa.gov/citations/20250007045
[2]: https://www.sawe.org/product/sawe-rp-a-8-2015a/
"""

from __future__ import annotations

import re
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator

from adh.msosa.behavior import Behaviors
from adh.msosa.metadata import NodeMetaMixin
from adh.msosa.performance import Performances
from adh.msosa.requirements import Requirements

_WBS_PATTERN = re.compile(r"^\d+(\.\d+)*$")


class Architecture(NodeMetaMixin, BaseModel):
    """Base model for all WBS architecture nodes."""

    wbs_no: str = ""

    @field_validator("wbs_no")
    @classmethod
    def validate_wbs_no(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not _WBS_PATTERN.match(value):
            raise ValueError(
                f"Invalid WBS number '{value}': must match pattern \\d+(\\.\\d+)*"
            )
        return value


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


class Metadata(BaseModel):
    """Key-value metadata for annotating architecture nodes."""

    # TODO: Rename or replace this value-annotation model.
    # It currently carries units/bounds/uncertainty metadata for helper fields and
    # may later be replaced by a Pint-based annotation type.

    key: str
    value: Any = None
    units: Optional[str] = Field(default=None, description="Units of measure")
    uncertainty: Optional[Any] = Field(default=None, description="Uncertainty value")
    lower_bounds: Optional[Union[int, float]] = Field(
        default=None, description="Lower bound"
    )
    upper_bounds: Optional[Union[int, float]] = Field(
        default=None, description="Upper bound"
    )

    model_config = ConfigDict(
        validate_assignment=True,
        arbitrary_types_allowed=True,
        extra="forbid",
        str_min_length=1,
        str_max_length=255,
        str_strip_whitespace=True,
    )


__all__ = ["Architecture", "MSoSAMixin", "Metadata"]
