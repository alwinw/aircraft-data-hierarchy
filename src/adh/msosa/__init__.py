"""
MSoSA: Model-Based System-of-Systems Architecture.

 - Guidelines for developing and describing complex Systems-of-Systems.
"""

from adh.msosa.architecture import Architecture, Metadata, MSoSAMixin
from adh.msosa.behavior import Activity, ActivityState, Behavior, Behaviors
from adh.msosa.metadata import (
    Author,
    ExternalReference,
    FidelityLevel,
    NodeMetaMixin,
    SourceInfo,
)
from adh.msosa.performance import Discipline, PerfDisciplines, Performances
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
    "Author",
    "Behavior",
    "Behaviors",
    "Discipline",
    "ExternalReference",
    "FidelityLevel",
    "Metadata",
    "MSoSAMixin",
    "NodeMetaMixin",
    "PerfDisciplines",
    "Performances",
    "Priority",
    "ReqsCategories",
    "Requirement",
    "Requirements",
    "RequirementStatus",
    "SourceInfo",
    "VerificationMethod",
]
