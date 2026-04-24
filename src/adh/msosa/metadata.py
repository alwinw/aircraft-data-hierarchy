"""Shared node metadata, provenance, and fidelity models."""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import UUID4, BaseModel, ConfigDict, Field, field_validator


class Author(BaseModel):
    """Author or contributor to an ADH node."""

    name: str = Field(description="Full name of the author.")
    organisation: Optional[str] = Field(
        default=None, description="Organisation or affiliation."
    )
    email: Optional[str] = Field(default=None, description="Email address.")


class ExternalReference(BaseModel):
    """Reference to an external file or document."""

    title: str = Field(description="Title or name of the referenced resource.")
    path: Optional[str] = Field(
        default=None,
        description="File path or URI to the external resource.",
    )
    description: Optional[str] = Field(
        default=None,
        description="Description of the reference and its relevance.",
    )
    classification: Optional[str] = Field(
        default=None,
        description=(
            "Type classification of the reference "
            "(e.g. 'STEP file', 'CFD mesh', 'test report')."
        ),
    )


class SourceInfo(BaseModel):
    """Source and authorship metadata for an ADH node."""

    authors: Optional[list[Author]] = Field(
        default=None, description="Authors or contributors."
    )
    creation_date: Optional[date] = Field(
        default=None, description="Date this node was created."
    )
    modification_date: Optional[date] = Field(
        default=None, description="Date this node was last modified."
    )
    version: Optional[str] = Field(default=None, description="Version string.")
    references: Optional[list[ExternalReference]] = Field(
        default=None,
        description="References to external files or documents.",
    )


class FidelityLevel(str, Enum):
    """L0-L4 fidelity taxonomy for ADH domain blocks."""

    sketch = "L0"
    layout = "L1"
    detailed = "L2"
    high_fidelity = "L3"
    validated = "L4"


class NodeMetaMixin(BaseModel):
    """Shared top-level metadata for ADH node-like models."""

    name: Optional[str] = Field(default=None, description="A unique model name.")
    description: Optional[str] = Field(
        default=None, description="A brief description of the model."
    )
    source_info: Optional[SourceInfo] = Field(
        default=None, description="Source and authorship metadata."
    )
    uuid: Optional[UUID4] = Field(
        default=None, description="A globally unique identifier for the model."
    )

    model_config = ConfigDict(
        validate_assignment=True,
        extra="allow",
        str_strip_whitespace=True,
        str_min_length=1,
    )

    @field_validator("name", "description", mode="before")
    @classmethod
    def validate_non_empty(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not value.strip():
            raise ValueError("Name and description fields must not be empty.")
        return value


__all__ = [
    "Author",
    "ExternalReference",
    "FidelityLevel",
    "NodeMetaMixin",
    "SourceInfo",
]
