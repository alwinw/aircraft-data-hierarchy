"""A Python module for Aircraft Data Hierarchy.

The public API is not re-exported at the top level while the module structure
is being designed. Import directly from submodules, e.g.:

    from adh.wbs import AircraftSystem
    from adh.msosa.architecture import Architecture
"""

from adh.__version__ import __version__

__all__ = ["__version__"]
