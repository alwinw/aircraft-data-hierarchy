"""
ADH Requirements (Reqs) Models.

Requirements models describe the capturing of system needs, ensuring traceability and
validation in each framework.

The requirements child nodes in the [ADH][1] are aligned with
[ISO/IEC/IEEE 29148:2018][2] and
[INCOSE][3]

[1]: https://ntrs.nasa.gov/citations/20250007045
[2]: https://www.iso.org/standard/72089.html
[3]: https://www.incose.org/resources-publications/technical-publications/se-handbook/
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from adh.msosa.metadata import SourceInfo


class ReqsCategories(str, Enum):
    """
    Taxonomy for system requirements based on ISO/IEC/IEEE 29148 and
    INCOSE's Guide to Writing Requirements.
    """

    functional = "functional"
    """Defines the essential capabilities, behaviors, and tasks the system must perform."""

    performance = "performance"
    """Specifies measurable benchmarks such as speed, throughput, capacity, and timing."""

    quality_reliability = "quality and reliability"
    """Defines system 'ilities' including reliability, availability, maintainability, and usability."""

    security_cyber = "security and cyber security"
    """Specifies protection of the system, data, and users from unauthorized access or harm."""

    interface = "interface"
    """Defines the logical and physical connection points with external systems, hardware, or users."""

    constraints = "constraints"
    """Restricts the design space, including physical (SWaP), material, or architectural limits."""

    regulatory_compliance = "regulatory and compliance"
    """Mandates adherence to laws, industry standards, safety codes, and legal policies."""

    non_functional = "non-functional"
    """A broad category for quality attributes not captured in specific performance or security buckets."""


class VerificationMethod(str, Enum):
    """Verification methods per ISO/IEC/IEEE 15288:2023."""

    test = "test"
    """Verification by executing the system under controlled conditions."""

    analysis = "analysis"
    """Verification by mathematical or logical examination of models or data."""

    inspection = "inspection"
    """Verification by visual or physical examination of the system."""

    demonstration = "demonstration"
    """Verification by operating the system and observing its behaviour."""


class Priority(str, Enum):
    """Requirement priority levels per INCOSE guidance."""

    critical = "critical"
    high = "high"
    medium = "medium"
    low = "low"


class RequirementStatus(str, Enum):
    """Lifecycle status of a requirement."""

    draft = "draft"
    approved = "approved"
    implemented = "implemented"
    verified = "verified"
    obsolete = "obsolete"


class Requirement(BaseModel):
    """A single requirement including specification, tracking and validation."""

    name: str = Field(description="A unique name identifying the requirement.")
    description: Optional[str] = Field(
        default=None, description="A detailed description of the requirement."
    )
    category: Optional[ReqsCategories] = Field(
        default=None, description="The category of the requirement."
    )
    priority: Optional[Priority] = Field(
        default=None, description="The priority of the requirement."
    )
    verification_method: Optional[VerificationMethod] = Field(
        default=None, description="How the requirement will be verified."
    )
    status: Optional[RequirementStatus] = Field(
        default=None, description="The current lifecycle status of the requirement."
    )
    source: Optional[str] = Field(
        default=None, description="The originating document or stakeholder."
    )
    acceptance_criteria: Optional[str] = Field(
        default=None,
        description="Conditions that must be met for the requirement to be satisfied.",
    )
    target_component: Optional[str] = Field(
        default=None,
        description="The component or subsystem this requirement applies to.",
    )
    risk: Optional[str] = Field(
        default=None, description="Known risks associated with this requirement."
    )
    verification_evidence: Optional[str] = Field(
        default=None, description="Evidence or artefacts confirming verification."
    )
    source_info: Optional[SourceInfo] = Field(
        default=None, description="Source and authorship metadata."
    )


class Requirements(BaseModel):
    """Container for a list of requirements."""

    requirements: Optional[list[Requirement]] = None
