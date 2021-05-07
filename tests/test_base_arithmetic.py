import pytest

from units_calculator.si_units import Seconds
from units_calculator.units_bases import Number


def test_create_unitless_number():
    n = Number(5.0)
    assert repr(n) == "5.0"


def test_create_direct_unit():
    s = Seconds(5.0)
    assert repr(s) == "5.0s"


def test_compare_units():
    s1 = Seconds(2.0)
    s2 = Seconds(7.0)
    assert s1 < s2
    assert s1 <= s2
    assert s2 <= s2
    assert s2 == s2
    assert s2 >= s2
    assert s2 >= s1
    assert s2 > s1


def test_add_units():
    s1 = Seconds(4.0)
    s2 = Seconds(3)
    s3 = Seconds(5)
    _sum = s1 + s2
    assert repr(_sum) == "7.0s"
    _sum += s3
    assert _sum.val == 12.0


def test_sub_units():
    s1 = Seconds(12.0)
    s2 = Seconds(3)
    s3 = Seconds(5)
    _sum = s1 - s2
    assert repr(_sum) == "9.0s"
    _sum -= s3
    assert _sum.val == 4.0


def test_add_unit_and_number():
    s = Seconds(1.0)
    n = Number(-3)
    with pytest.raises(AssertionError):
        n += s


def test_div_units():
    s1 = Seconds(7.0)
    s2 = Seconds(3.0)
    assert (s1 // s2).val == 2
    assert (s1 / s2).val == 7 / 3
