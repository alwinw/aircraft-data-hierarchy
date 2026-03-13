"""
DaveML table primitives for ANSI/AIAA-S-119-2011.

Extracted from the DAVE-ML specification for simulation model exchange.
Covers variable definitions, breakpoint sets, gridded and ungridded tables,
function definitions, and verification check data.

[ANSI/AIAA-S-119-2011](https://arc.aiaa.org/doi/10.2514/4.867965.001)
"""

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field, ValidationInfo, field_validator


class ExtrapolateEnum(str, Enum):
    """Extrapolation method for table lookups."""

    NEITHER = "neither"
    MIN = "min"
    MAX = "max"
    BOTH = "both"


class InterpolateEnum(str, Enum):
    """Interpolation method for table lookups (ANSI/AIAA-S-119-2011)."""

    DISCRETE = "discrete"
    FLOOR = "floor"
    CEILING = "ceiling"
    LINEAR = "linear"
    QUADRATIC_SPLINE = "quadraticSpline"
    CUBIC_SPLINE = "cubicSpline"


class UncertaintyEffect(str, Enum):
    """Effect type for uncertainty specification."""

    ADDITIVE = "additive"
    MULTIPLICATIVE = "multiplicative"
    PERCENTAGE = "percentage"
    ABSOLUTE = "absolute"


class Description(BaseModel):
    """Textual description of an entity."""

    value: Optional[str] = Field(default=None, description="The description text")


class Calculation(BaseModel):
    """Calculation using MathML content markup."""

    math: Optional[str] = Field(
        default=None, description="The MathML content markup describing the calculation"
    )


class VariableRef(BaseModel):
    """Reference to a variable."""

    var_id: Optional[str] = Field(
        default=None, description="The ID of the referenced variable"
    )


class DataTable(BaseModel):
    """Data of a gridded table as whitespace- or comma-separated values."""

    value: Optional[str] = Field(
        default=None,
        description="The table data as a string of comma- or whitespace-separated values",
    )


class DataPoint(BaseModel):
    """Data point in an ungridded table."""

    mod_id: Optional[str] = Field(
        default=None,
        description="The ID of the modification record for this data point",
    )
    value: Optional[str] = Field(
        default=None, description="The values of the data point"
    )


class ConfidenceBound(BaseModel):
    """Confidence bound for table data."""

    value: Optional[float] = Field(
        default=None, description="The value of the confidence bound"
    )


class BpRef(BaseModel):
    """Reference to a breakpoint set."""

    bp_id: Optional[str] = Field(
        default=None, description="The ID of the referenced breakpoint set"
    )


class BreakpointDef(BaseModel):
    """Definition of a breakpoint set."""

    name: Optional[str] = Field(
        default=None, description="The name of the breakpoint set"
    )
    bp_id: Optional[str] = Field(
        default=None, description="The unique identifier for this breakpoint set"
    )
    units: Optional[str] = Field(
        default=None, description="The units of measure for the breakpoints"
    )
    description: Optional[Description] = Field(
        default=None, description="A description of the breakpoint set"
    )
    bp_vals: Optional[str] = Field(default=None, description="The breakpoint values")


class Correlation(BaseModel):
    """Correlation between variables."""

    var_id: Optional[str] = Field(
        default=None, description="The ID of the correlated variable"
    )
    corr_coef: Optional[float] = Field(
        default=None, description="The correlation coefficient"
    )


class CorrelatesWith(BaseModel):
    """Indicates correlation with another variable."""

    var_id: Optional[str] = Field(
        default=None, description="The ID of the correlated variable"
    )


class NormalPDF(BaseModel):
    """Normal probability distribution function."""

    num_sigmas: Optional[float] = Field(
        default=None, description="The number of standard deviations"
    )
    bounds: Optional[list[Bounds]] = Field(
        default=None, description="The bounds of the distribution"
    )
    correlates_with: Optional[list[CorrelatesWith]] = Field(
        default=None, description="Correlations with other variables"
    )
    correlation: Optional[list[Correlation]] = Field(
        default=None, description="Correlation coefficients"
    )


class UniformPDF(BaseModel):
    """Uniform probability distribution function."""

    bounds: Optional[list[Bounds]] = Field(
        default=None, min_length=1, description="The bounds of the distribution"
    )


class Bounds(BaseModel):
    """Statistical limits of a parameter."""

    value: Optional[Union[str, DataTable, VariableDef, VariableRef]] = Field(
        default=None, description="The bound value or reference"
    )


class Uncertainty(BaseModel):
    """Uncertainty of a function or parameter value."""

    effect: Optional[UncertaintyEffect] = Field(
        default=None, description="The effect of the uncertainty"
    )
    normal_pdf: Optional[NormalPDF] = Field(
        default=None, description="The normal probability distribution function"
    )
    uniform_pdf: Optional[UniformPDF] = Field(
        default=None, description="The uniform probability distribution function"
    )

    @field_validator("uniform_pdf")
    @classmethod
    def validate_pdf(
        cls, v: Optional[UniformPDF], info: ValidationInfo
    ) -> Optional[UniformPDF]:
        if v is not None and info.data.get("normal_pdf") is not None:
            raise ValueError("Only one of normal_pdf or uniform_pdf can be specified")
        return v


class VariableDef(BaseModel):
    """Definition of a variable."""

    name: Optional[str] = Field(default=None, description="The name of the variable")
    var_id: Optional[str] = Field(
        default=None, description="The unique identifier for this variable"
    )
    units: Optional[str] = Field(
        default=None, description="The units of measure for the variable"
    )
    axis_system: Optional[str] = Field(
        default=None, description="The axis system for the variable"
    )
    sign: Optional[str] = Field(
        default=None, description="The sign convention for the variable"
    )
    alias: Optional[str] = Field(default=None, description="An alias for the variable")
    symbol: Optional[str] = Field(
        default=None, description="A symbol representing the variable"
    )
    initial_value: Optional[float] = Field(
        default=None, description="The initial value of the variable"
    )
    min_value: Optional[float] = Field(
        default=None, description="The minimum allowed value of the variable"
    )
    max_value: Optional[float] = Field(
        default=None, description="The maximum allowed value of the variable"
    )
    description: Optional[Description] = Field(
        default=None, description="A description of the variable"
    )
    calculation: Optional[Calculation] = Field(
        default=None, description="The calculation for deriving the variable's value"
    )
    is_input: Optional[bool] = Field(
        default=None, description="Indicates if the variable is an input"
    )
    is_control: Optional[bool] = Field(
        default=None, description="Indicates if the variable is a control parameter"
    )
    is_disturbance: Optional[bool] = Field(
        default=None, description="Indicates if the variable is a disturbance input"
    )
    is_state: Optional[bool] = Field(
        default=None, description="Indicates if the variable is a state variable"
    )
    is_state_deriv: Optional[bool] = Field(
        default=None, description="Indicates if the variable is a state derivative"
    )
    is_output: Optional[bool] = Field(
        default=None, description="Indicates if the variable is an output"
    )
    is_std_aiaa: Optional[bool] = Field(
        default=None,
        description="Indicates if the variable is a standard AIAA variable",
    )
    uncertainty: Optional[Uncertainty] = Field(
        default=None, description="The uncertainty associated with the variable"
    )


class GriddedTableDef(BaseModel):
    """Definition of a gridded table."""

    name: Optional[str] = Field(
        default=None, description="The name of the gridded table"
    )
    gt_id: Optional[str] = Field(
        default=None, description="The unique identifier for this gridded table"
    )
    units: Optional[str] = Field(
        default=None, description="The units of measure for the table values"
    )
    description: Optional[Description] = Field(
        default=None, description="A description of the gridded table"
    )
    breakpoint_refs: Optional[list[BpRef]] = Field(
        default=None, description="References to the breakpoint sets used in this table"
    )
    uncertainty: Optional[Uncertainty] = Field(
        default=None, description="The uncertainty associated with the table values"
    )
    data_table: Optional[DataTable] = Field(
        default=None, description="The actual data of the gridded table"
    )


class UngriddedTableDef(BaseModel):
    """Definition of an ungridded table."""

    name: Optional[str] = Field(
        default=None, description="The name of the ungridded table"
    )
    ut_id: Optional[str] = Field(
        default=None, description="The unique identifier for this ungridded table"
    )
    units: Optional[str] = Field(
        default=None, description="The units of measure for the table values"
    )
    description: Optional[Description] = Field(
        default=None, description="A description of the ungridded table"
    )
    uncertainty: Optional[Uncertainty] = Field(
        default=None, description="The uncertainty associated with the table values"
    )
    data_point: Optional[list[DataPoint]] = Field(
        default=None, description="The data points of the ungridded table"
    )


class GriddedTableRef(BaseModel):
    """Reference to a gridded table."""

    gt_id: Optional[str] = Field(
        default=None, description="The ID of the referenced gridded table"
    )


class GriddedTable(BaseModel):
    """Inline gridded table."""

    name: Optional[str] = Field(
        default=None, description="The name of the gridded table"
    )
    breakpoint_refs: Optional[list[BpRef]] = Field(
        default=None, description="References to the breakpoint sets used in this table"
    )
    confidence_bound: Optional[ConfidenceBound] = Field(
        default=None, description="The confidence bound for the table data"
    )
    data_table: Optional[DataTable] = Field(
        default=None, description="The actual data of the gridded table"
    )


class UngriddedTableRef(BaseModel):
    """Reference to an ungridded table."""

    ut_id: Optional[str] = Field(
        default=None, description="The ID of the referenced ungridded table"
    )


class UngriddedTable(BaseModel):
    """Inline ungridded table."""

    name: Optional[str] = Field(
        default=None, description="The name of the ungridded table"
    )
    confidence_bound: Optional[ConfidenceBound] = Field(
        default=None, description="The confidence bound for the table data"
    )
    data_point: Optional[list[DataPoint]] = Field(
        default=None, description="The data points of the ungridded table"
    )


class FunctionDefn(BaseModel):
    """Definition of a complex function (table-based lookup)."""

    name: Optional[str] = Field(
        default=None, description="The name of the function definition"
    )
    gridded_table_ref: Optional[GriddedTableRef] = Field(
        default=None, description="A reference to a gridded table"
    )
    gridded_table_def: Optional[GriddedTableDef] = Field(
        default=None, description="A gridded table definition"
    )
    gridded_table: Optional[GriddedTable] = Field(
        default=None, description="A gridded table"
    )
    ungridded_table_ref: Optional[UngriddedTableRef] = Field(
        default=None, description="A reference to an ungridded table"
    )
    ungridded_table_def: Optional[UngriddedTableDef] = Field(
        default=None, description="An ungridded table definition"
    )
    ungridded_table: Optional[UngriddedTable] = Field(
        default=None, description="An ungridded table"
    )

    @field_validator(
        "gridded_table_ref",
        "gridded_table_def",
        "gridded_table",
        "ungridded_table_ref",
        "ungridded_table_def",
        "ungridded_table",
    )
    @classmethod
    def validate_table_type(cls, v: object, info: ValidationInfo) -> object:
        if v is not None:
            table_fields = [
                "gridded_table_ref",
                "gridded_table_def",
                "gridded_table",
                "ungridded_table_ref",
                "ungridded_table_def",
                "ungridded_table",
            ]
            if sum(1 for field in table_fields if info.data.get(field) is not None) > 1:
                raise ValueError(
                    "Only one table type can be specified in a function definition"
                )
        return v


class IndependentVarPts(BaseModel):
    """Independent variable points for a simple function."""

    var_id: Optional[str] = Field(
        default=None, description="The ID of the referenced variable"
    )
    name: Optional[str] = Field(
        default=None, description="The name of the independent variable"
    )
    units: Optional[str] = Field(
        default=None, description="The units of the independent variable"
    )
    sign: Optional[str] = Field(
        default=None, description="The sign convention for the independent variable"
    )
    extrapolate: Optional[ExtrapolateEnum] = Field(
        default=None, description="The extrapolation method"
    )
    interpolate: Optional[InterpolateEnum] = Field(
        default=None, description="The interpolation method"
    )
    value: Optional[str] = Field(
        default=None, description="The values of the independent variable points"
    )


class DependentVarPts(BaseModel):
    """Dependent variable points for a simple function."""

    var_id: Optional[str] = Field(
        default=None, description="The ID of the referenced variable"
    )
    name: Optional[str] = Field(
        default=None, description="The name of the dependent variable"
    )
    units: Optional[str] = Field(
        default=None, description="The units of the dependent variable"
    )
    sign: Optional[str] = Field(
        default=None, description="The sign convention for the dependent variable"
    )
    value: Optional[str] = Field(
        default=None, description="The values of the dependent variable points"
    )


class IndependentVarRef(BaseModel):
    """Reference to an independent variable for a complex function."""

    var_id: Optional[str] = Field(
        default=None, description="The ID of the referenced variable"
    )
    min: Optional[float] = Field(
        default=None, description="The minimum value of the independent variable"
    )
    max: Optional[float] = Field(
        default=None, description="The maximum value of the independent variable"
    )
    extrapolate: Optional[ExtrapolateEnum] = Field(
        default=None, description="The extrapolation method"
    )
    interpolate: Optional[InterpolateEnum] = Field(
        default=None, description="The interpolation method"
    )


class DependentVarRef(BaseModel):
    """Reference to a dependent variable for a complex function."""

    var_id: Optional[str] = Field(
        default=None, description="The ID of the referenced variable"
    )


class Function(BaseModel):
    """A DAVE-ML function relating independent variables to a dependent variable."""

    name: Optional[str] = Field(default=None, description="The name of the function")
    description: Optional[Description] = Field(
        default=None, description="A description of the function"
    )
    independent_var_pts: Optional[list[IndependentVarPts]] = Field(
        default=None, description="The independent variable points for simple functions"
    )
    dependent_var_pts: Optional[DependentVarPts] = Field(
        default=None, description="The dependent variable points for simple functions"
    )
    independent_var_ref: Optional[list[IndependentVarRef]] = Field(
        default=None,
        description="References to independent variables for complex functions",
    )
    dependent_var_ref: Optional[list[DependentVarRef]] = Field(
        default=None,
        description="Reference to the dependent variable for complex functions",
    )
    function_defn: Optional[FunctionDefn] = Field(
        default=None, description="The function definition for complex functions"
    )

    @field_validator("dependent_var_pts", "dependent_var_ref", "function_defn")
    @classmethod
    def validate_function_type(cls, v: object, info: ValidationInfo) -> object:
        if (
            v is not None
            and info.data.get("independent_var_pts")
            and info.data.get("independent_var_ref")
        ):
            raise ValueError(
                "Function can't have both simple and complex representations"
            )
        return v


class Signal(BaseModel):
    """Signal (input, internal, or output) in a check case."""

    signal_name: Optional[str] = Field(
        default=None, description="The name of the signal"
    )
    signal_units: Optional[str] = Field(
        default=None, description="The units of the signal"
    )
    var_id: Optional[str] = Field(
        default=None, description="The ID of the variable associated with this signal"
    )
    signal_value: Optional[str] = Field(
        default=None, description="The value of the signal"
    )
    tol: Optional[str] = Field(
        default=None, description="The tolerance for this signal's value"
    )


class CheckInputs(BaseModel):
    """Input values for a check case."""

    signal: Optional[list[Signal]] = Field(
        default=None, description="The input signals for this check case"
    )


class InternalValues(BaseModel):
    """Internal variable values for a check case."""

    signal: Optional[list[Signal]] = Field(
        default=None, description="The internal signals for this check case"
    )


class CheckOutputs(BaseModel):
    """Expected output values for a check case."""

    signal: Optional[list[Signal]] = Field(
        default=None, description="The output signals for this check case"
    )


class StaticShot(BaseModel):
    """Static check case for model verification."""

    name: Optional[str] = Field(default=None, description="The name of the static shot")
    ref_id: Optional[str] = Field(
        default=None, description="The reference ID for this static shot"
    )
    description: Optional[Description] = Field(
        default=None, description="A description of the static shot"
    )
    check_inputs: Optional[CheckInputs] = Field(
        default=None, description="The input values for this check case"
    )
    internal_values: Optional[InternalValues] = Field(
        default=None, description="The internal variable values for this check case"
    )
    check_outputs: Optional[CheckOutputs] = Field(
        default=None, description="The expected output values for this check case"
    )


class CheckData(BaseModel):
    """Check data for model verification."""

    static_shot: Optional[list[StaticShot]] = Field(
        default=None, description="Static check cases"
    )


class TablesMixin(BaseModel):
    """Mixin that adds optional DaveML table fields for composing into Behavior/Discipline."""

    variable_defs: Optional[list[VariableDef]] = Field(
        default=None, description="Variable definitions"
    )
    breakpoint_defs: Optional[list[BreakpointDef]] = Field(
        default=None, description="Breakpoint set definitions"
    )
    gridded_table_defs: Optional[list[GriddedTableDef]] = Field(
        default=None, description="Gridded table definitions"
    )
    ungridded_table_defs: Optional[list[UngriddedTableDef]] = Field(
        default=None, description="Ungridded table definitions"
    )
    functions: Optional[list[Function]] = Field(
        default=None, description="Function definitions"
    )
    check_data: Optional[CheckData] = Field(
        default=None, description="Verification check data"
    )


# Rebuild models with forward references
NormalPDF.model_rebuild()
UniformPDF.model_rebuild()
Bounds.model_rebuild()
VariableDef.model_rebuild()
FunctionDefn.model_rebuild()
GriddedTableDef.model_rebuild()
UngriddedTableDef.model_rebuild()
Function.model_rebuild()
GriddedTable.model_rebuild()
UngriddedTable.model_rebuild()
CheckData.model_rebuild()
StaticShot.model_rebuild()
