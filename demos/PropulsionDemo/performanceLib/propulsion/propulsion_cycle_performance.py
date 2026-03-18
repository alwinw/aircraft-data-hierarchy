from typing import Optional

from pydantic import Field, field_validator

from adh.msosa.performance import ModelDescription


class PropulsionCyclePerformance(ModelDescription):
    """
    Contains the analysis inputs and Engine Deck for a propulsion cycle analysis.

    Attributes:
        name (str): The name of the engine cycle.
        design (bool): Whether the engine cycle is in design mode.
        thermo_method (str, optional): The thermodynamic method used in the engine cycle. Defaults to 'CEA'.
        thermo_data (str, optional): The thermodynamic data used in the engine cycle.
        solver_settings (dict, optional): The solver settings for the engine cycle.
    """

    name: str = Field(..., description="The name of the engine cycle analysis.")
    thermo_method: str = Field(
        "TABULAR", description="The thermodynamic method used in the engine cycle."
    )
    thermo_data: Optional[str] = Field(
        default=None, description="The thermodynamic data used in the engine cycle."
    )
    throttle_mode: str = Field(
        "T4",
        description="What quantity should be used to throttle engine for off-design cases.",
    )
    solver_settings: Optional[dict] = Field(
        default=None, description="The solver settings for the engine cycle."
    )

    @field_validator("thermo_method")
    def validate_thermo_method(cls, v):
        allowed_methods = ["CEA", "TABULAR"]
        if v not in allowed_methods:
            raise ValueError(f"Thermodynamic method must be one of {allowed_methods}")
        return v

    @field_validator("throttle_mode")
    def validate_throttle_mode(cls, v):
        allowed_methods = ["T4", "percent_thrust"]
        if v not in allowed_methods:
            raise ValueError(f"Throttle mode must be one of {allowed_methods}")
        return v
