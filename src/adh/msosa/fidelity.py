"""
ADH Fidelity Level taxonomy.

Defines the canonical L0-L4 fidelity levels used across performance and behaviour
nodes in an ADH fragment. Levels are additive: an L2 fragment is a valid L1 and L0
fragment with additional fields populated.

Design phase alignment follows NASA NPR 7120.5 (Phase A/B/C). Equivalent DoD/contractor
phases: Conceptual -> PDR (Phase B early) -> CDR (Phase C).

Reference: Di Pietro, D.A. (2015), NTRS 20150018331.
"""

from __future__ import annotations

from enum import Enum


class FidelityLevel(str, Enum):
    """L0-L4 fidelity taxonomy for ADH domain blocks.

    Each level defines the analysis approach and admissible tools for a given
    discipline. A design point declares a level per domain; levels are orthogonal
    across domains (e.g. L2 geometry with L0 aerodynamics is valid).
    """

    sketch = "L0"
    """Exploratory / Pre-Phase A. Parametric and empirical equations only.
    Order-of-magnitude sizing; no physical layout required."""

    layout = "L1"
    """Conceptual / Phase A. Major components parameterised.
    W&B, basic performance, and trade studies admissible."""

    detailed = "L2"
    """Preliminary / Phase B (early). All geometry modelled.
    Multi-discipline analysis at selected conditions; 3-DOF dynamics."""

    high_fidelity = "L3"
    """Preliminary / Phase B (late). Non-linear physics; full envelope coverage.
    3D FEM / RANS CFD; detailed subsystem sizing."""

    validated = "L4"
    """Detailed / Phase C and certification. Physical test correlation.
    Full-physics simulation (LES/DNS). Outside MAGPIE scope; included to define
    the upper boundary."""


__all__ = ["FidelityLevel"]
