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

_WBS_PATTERN = re.compile(r"^\d+(\.\d+)*$")


class Architecture(BaseModel):
    """Base model for all WBS architecture nodes."""

    name: Optional[str] = None
    description: Optional[str] = None
    wbs_no: Optional[str] = None

    model_config = ConfigDict(extra="allow")

    @field_validator("wbs_no")
    @classmethod
    def validate_wbs_no(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not _WBS_PATTERN.match(value):
            raise ValueError(
                f"Invalid WBS number '{value}': must match pattern \\d+(\\.\\d+)*"
            )
        return value


class Metadata(BaseModel):
    """Key-value metadata for annotating architecture nodes."""

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
