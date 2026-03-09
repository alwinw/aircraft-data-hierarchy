"""
DaveML table primitives for ANSI/AIAA-S-119-2011.

Extracted from the DAVE-ML specification for simulation model exchange.
Covers variable definitions, breakpoint sets, gridded and ungridded tables,
function definitions, and verification check data.

[ANSI/AIAA-S-119-2011](https://arc.aiaa.org/doi/10.2514/4.867965.001)
"""

from __future__ import annotations

from datetime import date
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


class ContactInfoType(str, Enum):
    """Type of contact information."""

    ADDRESS = "address"
    PHONE = "phone"
    FAX = "fax"
    EMAIL = "email"
    INAME = "iname"
    WEB = "web"


class ContactLocation(str, Enum):
    """Location context for contact information."""

    PROFESSIONAL = "professional"
    PERSONAL = "personal"
    MOBILE = "mobile"


class Description(BaseModel):
    """Textual description of an entity."""

    value: Optional[str] = Field(default=None, description="The description text")


class ContactInfo(BaseModel):
    """Contact information for an author."""

    value: Optional[str] = Field(
        default=None, description="The contact information value"
    )
    contact_info_type: Optional[ContactInfoType] = Field(
        default=None, description="The type of contact information"
    )
    contact_location: Optional[ContactLocation] = Field(
        default=None, description="The location associated with the contact information"
    )


class Author(BaseModel):
    """Author of a DAVE-ML document."""

    name: Optional[str] = Field(default=None, description="The name of the author")
    org: Optional[str] = Field(
        default=None, description="The organisation the author belongs to"
    )
    xns: Optional[str] = Field(
        default=None, description="The XNS identifier for the author"
    )
    email: Optional[str] = Field(
        default=None, description="The email address of the author"
    )
    address: Optional[list[str]] = Field(
        default=None, description="The physical address of the author"
    )
    contact_info: Optional[list[ContactInfo]] = Field(
        default=None, description="Additional contact information for the author"
    )


class CreationDate(BaseModel):
    """Creation date of a DAVE-ML document."""

    date: Optional[date] = None


class FileVersion(BaseModel):
    """Version of a DAVE-ML document."""

    value: Optional[str] = Field(default=None, description="The version string")


class Reference(BaseModel):
    """Reference to an external document."""

    ref_id: Optional[str] = Field(
        default=None, description="The unique identifier for this reference"
    )
    author: Optional[str] = Field(
        default=None, description="The author of the referenced document"
    )
    title: Optional[str] = Field(
        default=None, description="The title of the referenced document"
    )
    classification: Optional[str] = Field(
        default=None, description="The classification of the referenced document"
    )
    accession: Optional[str] = Field(
        default=None, description="The accession number of the referenced document"
    )
    date: Optional[date] = None
    href: Optional[str] = Field(
        default=None, description="The URL of the referenced document"
    )
    description: Optional[Description] = Field(
        default=None, description="A description of the referenced document"
    )


class ExtraDocRef(BaseModel):
    """Additional document reference."""

    ref_id: Optional[str] = Field(
        default=None, description="The reference ID of the additional document"
    )


class DocumentRef(BaseModel):
    """Reference to a document."""

    doc_id: Optional[str] = Field(
        default=None, description="The ID of the referenced document"
    )
    ref_id: Optional[str] = Field(
        default=None, description="The reference ID of the document"
    )


class ModificationRef(BaseModel):
    """Reference to a modification record."""

    mod_id: Optional[str] = Field(
        default=None, description="The ID of the referenced modification record"
    )


class ProvenanceRef(BaseModel):
    """Reference to a provenance record."""

    prov_id: Optional[str] = Field(
        default=None, description="The ID of the referenced provenance record"
    )


class ModificationRecord(BaseModel):
    """Modification record for a DAVE-ML document."""

    mod_id: Optional[str] = Field(
        default=None, description="The unique identifier for this modification record"
    )
    date: Optional[date] = None
    ref_id: Optional[str] = Field(
        default=None, description="The reference ID associated with this modification"
    )
    author: Optional[list[Author]] = Field(
        default=None, description="The authors of the modification"
    )
    description: Optional[Description] = Field(
        default=None, description="A description of the modification"
    )
    extra_doc_ref: Optional[list[ExtraDocRef]] = Field(
        default=None, description="Additional document references"
    )


class Provenance(BaseModel):
    """Provenance of a DAVE-ML document or element."""

    prov_id: Optional[str] = Field(
        default=None, description="The unique identifier for this provenance record"
    )
    author: Optional[list[Author]] = Field(
        default=None, description="The authors associated with this provenance"
    )
    creation_date: Optional[CreationDate] = Field(
        default=None, description="The creation date of the associated element"
    )
    document_ref: Optional[list[DocumentRef]] = Field(
        default=None, description="References to related documents"
    )
    modification_ref: Optional[list[ModificationRef]] = Field(
        default=None, description="References to related modifications"
    )
    description: Optional[Description] = Field(
        default=None, description="A description of the provenance"
    )


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
    provenance: Optional[Provenance] = Field(
        default=None, description="The provenance of the variable"
    )
    provenance_ref: Optional[ProvenanceRef] = Field(
        default=None, description="A reference to the provenance of the variable"
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
    provenance: Optional[Provenance] = Field(
        default=None, description="The provenance of the gridded table"
    )
    provenance_ref: Optional[ProvenanceRef] = Field(
        default=None, description="A reference to the provenance of the gridded table"
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
    provenance: Optional[Provenance] = Field(
        default=None, description="The provenance of the ungridded table"
    )
    provenance_ref: Optional[ProvenanceRef] = Field(
        default=None, description="A reference to the provenance of the ungridded table"
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
    provenance: Optional[Provenance] = Field(
        default=None, description="The provenance of the function"
    )
    provenance_ref: Optional[ProvenanceRef] = Field(
        default=None, description="A reference to the provenance of the function"
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
    provenance: Optional[Provenance] = Field(
        default=None, description="The provenance of the static shot"
    )
    provenance_ref: Optional[ProvenanceRef] = Field(
        default=None, description="A reference to the provenance of the static shot"
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

    provenance: Optional[Provenance] = Field(
        default=None, description="The provenance of the check data"
    )
    provenance_ref: Optional[ProvenanceRef] = Field(
        default=None, description="A reference to the provenance of the check data"
    )
    static_shot: Optional[list[StaticShot]] = Field(
        default=None, description="Static check cases"
    )


class FileHeader(BaseModel):
    """Header information for a DAVE-ML document."""

    name: Optional[str] = Field(
        default=None, description="The name of the DAVE-ML document"
    )
    author: Optional[list[Author]] = Field(
        default=None, description="The authors of the document"
    )
    creation_date: Optional[CreationDate] = Field(
        default=None, description="The creation date of the document"
    )
    file_version: Optional[FileVersion] = Field(
        default=None, description="The version of the document"
    )
    description: Optional[Description] = Field(
        default=None, description="A description of the document"
    )
    reference: Optional[list[Reference]] = Field(
        default=None, description="References to external documents"
    )
    modification_record: Optional[list[ModificationRecord]] = Field(
        default=None, description="Records of modifications to the document"
    )
    provenance: Optional[list[Provenance]] = Field(
        default=None, description="Provenance information for the document"
    )


class DAVEfunc(BaseModel):
    """Root element of a DAVE-ML document."""

    file_header: Optional[FileHeader] = Field(
        default=None, description="The header information for the DAVE-ML document"
    )
    variable_def: Optional[list[VariableDef]] = Field(
        default=None, description="The variable definitions in the document"
    )
    breakpoint_def: Optional[list[BreakpointDef]] = Field(
        default=None, description="The breakpoint set definitions in the document"
    )
    gridded_table_def: Optional[list[GriddedTableDef]] = Field(
        default=None, description="The gridded table definitions in the document"
    )
    ungridded_table_def: Optional[list[UngriddedTableDef]] = Field(
        default=None, description="The ungridded table definitions in the document"
    )
    function: Optional[list[Function]] = Field(
        default=None, description="The function definitions in the document"
    )
    check_data: Optional[CheckData] = Field(
        default=None, description="The check data for model verification"
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
Author.model_rebuild()
Provenance.model_rebuild()
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
DAVEfunc.model_rebuild()
