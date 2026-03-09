"""
MSoSA: Model-Based System-of-Systems Architecture.

 - Guidelines for developing and describing complex Systems-of-Systems.
"""

from adh.msosa.architecture import Architecture, Metadata
from adh.msosa.requirements import (
    Priority,
    ReqsCategories,
    Requirement,
    Requirements,
    RequirementStatus,
    VerificationMethod,
)

__all__ = [
    "Architecture",
    "Metadata",
    "Priority",
    "ReqsCategories",
    "Requirement",
    "Requirements",
    "RequirementStatus",
    "VerificationMethod",
]
