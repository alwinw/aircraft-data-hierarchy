"""Define Pydantic `ping.Quantity`.

Derived works from pydantic-pint with modifications:

- Support validation of a list

[`pydantic-pint`](https://github.com/tylerh111/pydantic-pint) license:

MIT License

Copyright (c) 2024-2025 Tyler Hughes

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

from numbers import Number
from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from pydantic import GetCoreSchemaHandler

import pint
from pint._typing import UnitLike
from pint.facets.plain.quantity import PlainQuantity as Quantity
from pydantic_core import core_schema

__all__ = ("PintQuantity",)

_DEFAULT_UNIT_REGISTRY = pint.UnitRegistry()


class PintQuantity:
    """Pydantic Pint Quantity."""

    def __init__(
        self,
        _arg: UnitLike,
        /,
        *,
        ureg: Optional[pint.UnitRegistry] = None,
    ) -> None:
        """Initialise units and dimensions.

        Args:
            _arg (UnitLike):
                Either the units or dimensions to check the Pydantic field.
                For example, `"sec"`, `"[length]"`, or `{"[length]": 1, "[time]": -2}`
            ureg (Optional[pint.UnitRegistry]):
                A custom Pint unit registry
        """
        self.ureg = ureg if ureg else _DEFAULT_UNIT_REGISTRY
        self.dimensions = self.ureg.get_dimensionality(_arg)

    def validate(
        self,
        v: dict | str | Number | Quantity,
        info: core_schema.ValidationInfo | None = None,
    ) -> Quantity:
        """Validate a Pydantic Pint Quantity."""
        # Given a dict of {'magnitude': m, 'units': u} convert to a string for ureg()
        if isinstance(v, dict):
            try:
                # TODO: handle a list of magnitudes
                v = f"{v['magnitude']} {v.get('units', '')}"
            except KeyError as e:
                raise ValueError("no `magnitude` or `units` keys found.") from e

        # Either a dict converted to str or called on a string
        if isinstance(v, str):
            try:
                v = self.ureg(v)
            except pint.UndefinedUnitError as e:
                raise ValueError(e) from e

        # TODO: handle if v is a list

        try:
            return self._validate_dimensions(v)
        except pint.DimensionalityError as e:
            raise ValueError(e) from e
        except KeyError as e:
            # raise TypeError instead of KeyError
            raise TypeError(f"unknown unit registry context {e}.") from e
        except Exception as e:
            raise ValueError(f"unknown error: {v=} | {type(v)=}.") from e

    def _validate_dimensions(self, v: Union[Number, Quantity]):
        if isinstance(v, Number):
            raise ValueError("must specify units with dimension restriction")

        if isinstance(v, Quantity):
            if v.check(self.dimensions) or any(
                v.is_compatible_with(dim)
                for dim in self.ureg._cache.dimensional_equivalents.get(
                    self.dimensions, []
                )
            ):
                return v
            raise ValueError(f"cannot convert to dimension '{self.dimensions}'")

    def serialize(
        self,
        v: Quantity,
        info: core_schema.SerializationInfo | None = None,
    ) -> dict:
        """Serialise a Pydantic Pint Quantity."""
        return {
            "magnitude": v.magnitude,
            "units": f"{v.units}",
        }

    def __get_pydantic_core_schema__(
        self,
        source_type: Any,
        handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        """Gets the Pydantic core schema.

        Args:
            source_type:
                The source type.
            handler:
                The `GetCoreSchemaHandler` instance.

        Returns:
            The Pydantic core schema.
        """
        _from_typedict_schema = {
            "magnitude": core_schema.typed_dict_field(
                core_schema.str_schema(coerce_numbers_to_str=True),
            ),
            "units": core_schema.typed_dict_field(
                core_schema.str_schema(),
                required=False,
            ),
        }

        validate_schema = core_schema.chain_schema(
            [
                core_schema.union_schema(
                    [
                        core_schema.is_instance_schema(Quantity),
                        core_schema.str_schema(coerce_numbers_to_str=True),
                        core_schema.typed_dict_schema(_from_typedict_schema),
                    ]
                ),
                core_schema.with_info_plain_validator_function(self.validate),
            ]
        )

        validate_json_schema = core_schema.chain_schema(
            [
                core_schema.union_schema(
                    [
                        core_schema.str_schema(coerce_numbers_to_str=True),
                        core_schema.typed_dict_schema(_from_typedict_schema),
                    ]
                ),
                core_schema.no_info_plain_validator_function(self.validate),
            ]
        )

        serialize_schema = core_schema.plain_serializer_function_ser_schema(
            self.serialize,
            info_arg=True,
        )

        return core_schema.json_or_python_schema(
            json_schema=validate_json_schema,
            python_schema=validate_schema,
            serialization=serialize_schema,
        )
