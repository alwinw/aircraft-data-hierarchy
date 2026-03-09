"""
MSoSA: Model-Based System-of-Systems Architecture.

 - Guidelines for developing and describing complex Systems-of-Systems.
"""

from adh.msosa.architecture import Architecture, Metadata
from adh.msosa.behavior import Activity, ActivityState, Behavior, Behaviors
from adh.msosa.requirements import (
    Priority,
    ReqsCategories,
    Requirement,
    Requirements,
    RequirementStatus,
    VerificationMethod,
)

__all__ = [
    "Activity",
    "ActivityState",
    "Architecture",
    "Behavior",
    "Behaviors",
    "Metadata",
    "Priority",
    "ReqsCategories",
    "Requirement",
    "Requirements",
    "RequirementStatus",
    "VerificationMethod",
]
