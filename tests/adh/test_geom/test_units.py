from __future__ import annotations

from typing import Annotated, cast

from pydantic import BaseModel

from adh.geom.units import PintAnno, PintQty, Quantity, get_registry

UREG = get_registry()


def test_construct_from_string_to_unit():

    class TestModel(BaseModel):
        value: Annotated[PintQty, PintAnno("m")]

    x = TestModel(value="1m")
    value = cast(Quantity, x.value)
    assert value.m == 1
    assert value.u == UREG.Unit("m")
    assert value == UREG("1m")


def test_construct_from_string_to_1d():

    class TestModel(BaseModel):
        value: Annotated[PintQty, PintAnno("[length]")]

    x = TestModel(value="1m")
    value = cast(Quantity, x.value)
    assert value.m == 1
    assert value.u == UREG.Unit("m")
    assert value == UREG("1m")


def test_construct_from_string_to_2d():

    class TestModel(BaseModel):
        value: Annotated[PintQty, PintAnno({"[length]": 2})]

    x = TestModel(value="1m**2")
    value = cast(Quantity, x.value)
    assert value.m == 1
    assert value.u == UREG.Unit("m**2")
    assert value == UREG("1m**2")

    print(x)
    print(f"{x!r}")
    print(x.model_dump())
    print(x.model_dump_json())
    print(TestModel.model_json_schema())


def test_construct_from_quantity_to_unit():
    class TestModel(BaseModel):
        value: Annotated[Quantity, PintAnno("m")]

    x = TestModel(value=1 * UREG.meter)
    assert x.value.m == 1
    assert x.value.u == UREG.Unit("m")
    assert x.value == UREG("1m")


def test_construct_from_quantity_to_1d():
    class TestModel(BaseModel):
        value: Annotated[Quantity, PintAnno("[length]")]

    x = TestModel(value=1 * UREG.meter)
    assert x.value.m == 1
    assert x.value.u == UREG.Unit("m")
    assert x.value == UREG("1m")


def test_construct_from_quantity_to_2d():
    class TestModel(BaseModel):
        value: Annotated[Quantity, PintAnno("[area]")]

    x = TestModel(value=1 * UREG.meter**2)
    assert x.value.m == 1
    assert x.value.u == UREG.Unit("m**2")
    assert x.value == UREG("1m**2")
