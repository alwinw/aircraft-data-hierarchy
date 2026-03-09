"""
ADH Source Information Models.

Shared metadata for all MSoSA views (Architecture, Requirements, Performance,
Behaviour). Captures authorship, creation/modification dates, version, and
references to external files or documents.

These models replace the DAVE-ML document-level metadata
(Author, FileHeader, Provenance, etc.) that was previously embedded in
``adh.tabular.tables``. By lifting metadata to the MSoSA view level, table
primitives stay focused on data structures while every view can record its own
source information uniformly.

[1]: https://ntrs.nasa.gov/citations/20250007045
"""

from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

__all__ = [
    "Author",
    "ExternalReference",
    "SourceInfo",
]


class Author(BaseModel):
    """Author or contributor to an ADH node."""

    name: str = Field(description="Full name of the author.")
    organisation: Optional[str] = Field(
        default=None, description="Organisation or affiliation."
    )
    email: Optional[str] = Field(default=None, description="Email address.")


class ExternalReference(BaseModel):
    """Reference to an external file or document.

    Use this to link an ADH node to supporting artefacts such as CAD geometry
    (STEP/IGES), CFD meshes, test reports, specification documents, or any
    other resource that informs the node's definition.
    """

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
    """Source and authorship metadata for an ADH node.

    Provides a uniform way to record who created or modified an ADH node, when,
    and what external resources informed it. Intended to be composed into every
    MSoSA view (Architecture, Requirement, Discipline, Behaviour) as an optional
    ``source_info`` field.
    """

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
