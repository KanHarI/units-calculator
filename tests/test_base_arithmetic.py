import pytest

from units_calculator.si_units import Seconds
from units_calculator.units_bases import Number


def test_create_unitless_number():
    n = Number(5.0)
    assert repr(n) == "5.0"


def test_create_direct_unit():
    s = Seconds(5.0)
    assert repr(s) == "5.0s"


def test_add_units():
    s1 = Seconds(4.0)
    s2 = Seconds(3)
    assert repr(s1 + s2) == "7.0s"


def test_add_unit_and_number():
    s = Seconds(1.0)
    n = Number(-3)
    with pytest.raises(AssertionError):
        n += s
