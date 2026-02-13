"""Common base pydantic models for the Aircraft Data Hierarchy schema."""

from typing import Any, ClassVar, Dict, Optional

import pint
from pydantic import BaseModel, ConfigDict, Field, field_validator

ureg = pint.UnitRegistry()


class KeyMixin(BaseModel):
    """Mix-in for normalised keys with max length."""

    model_config = ConfigDict(extra="forbid")

    key: str = Field(..., description="Key for the entry (max 255 chars).")

    @field_validator("key")
    @classmethod
    def _normalise_key(cls, v: str) -> str:
        v = v.strip()
        if len(v) >= 225:
            raise ValueError("key must be less than 255 characters long")
        if not v:
            raise ValueError("key must not be empty")
        if v.startswith("."):
            raise ValueError("key must not start with '.'")
        return v


class ExtraMetadataMixin(BaseModel):
    """Mix-in for attaching extra metadata to a model."""

    model_config = ConfigDict(extra="forbid")

    metadata: Optional[Dict[str, Any]] = Field(
        default=None, description="Extra metadata such as source."
    )


class UnitsMixin(BaseModel):
    """Mix-in for pint-backed unit handling."""

    model_config = ConfigDict(extra="forbid")

    dimensionality: ClassVar[Optional[str]] = None

    value: Any = Field(..., description="Magnitude of the quantity.")
    units: Optional[str] = Field(
        default=None,
        description="Units parsable by pint (default=None for dimensionless)",
    )

    @field_validator("units")
    @classmethod
    def _validate_units(cls, v: Optional[str]) -> Optional[str]:
        """Validate units and allow None for dimensionless."""
        if v is None:
            return None
        v = v.strip()
        if not v:
            raise ValueError("units must not be empty.")
        try:
            ureg.Unit(v)
        except Exception as e:
            raise ValueError(f"Invalid units: {v}") from e
        return v
