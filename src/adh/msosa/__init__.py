"""
MSoSA: Model-Based System-of-Systems Architecture.

 - Guidelines for developing and describing complex Systems-of-Systems.
"""

from adh.msosa.architecture import Architecture, Metadata
from adh.msosa.behavior import Activity, ActivityState, Behavior, Behaviors
from adh.msosa.performance import Discipline, PerfDisciplines, Performances
from adh.msosa.requirements import (
    Priority,
    ReqsCategories,
    Requirement,
    Requirements,
    RequirementStatus,
    VerificationMethod,
)
from adh.msosa.source_info import Author, ExternalReference, SourceInfo

__all__ = [
    "Activity",
    "ActivityState",
    "Architecture",
    "Author",
    "Behavior",
    "Behaviors",
    "Discipline",
    "ExternalReference",
    "Metadata",
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
