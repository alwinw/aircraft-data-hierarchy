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

from enum import Enum

from pydantic import BaseModel, Field


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

    regulatory_compliance = "regularity and compliance"
    """Mandates adherence to laws, industry standards, safety codes, and legal policies."""

    non_functional = "non-functional"
    """A broad category for quality attributes not captured in specific performance or security buckets."""


class Test(BaseModel):
    """Test class"""

    name: str
    """The name of the test."""


class Requirement(BaseModel):
    """A single requirement including specification, tracking and validation."""

    name: str = Field(
        description="A unique name identifying the requirement.",
    )
    # description: str = Field(
    #     description="A detailed description of the requirement.",
    # )
    # category: ReqsCategories = Field(
    #     ...,
    #     description="The category of the requirement.",
    # )
