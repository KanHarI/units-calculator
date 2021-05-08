import pytest

from units_calculator.si_units import Meters, Seconds
from units_calculator.units_bases import Number


def test_create_unitless_number() -> None:
    n = Number(5.0)
    assert repr(n) == "5.0"


def test_create_direct_unit() -> None:
    s = Seconds(5.0)
    assert repr(s) == "5.0s"


def test_compare_units() -> None:
    s1 = Seconds(2.0)
    s2 = Seconds(7.0)
    assert s1 < s2
    assert s1 <= s2
    assert s2 <= s2
    assert s2 == s2
    assert s2 >= s2
    assert s2 >= s1
    assert s2 > s1


def test_add_units() -> None:
    s1 = Seconds(4.0)
    s2 = Seconds(3)
    s3 = Seconds(5)
    _sum = s1 + s2
    assert repr(_sum) == "7.0s"
    _sum += s3
    assert _sum.val == 12.0


def test_sub_units() -> None:
    s1 = Seconds(12.0)
    s2 = Seconds(3)
    s3 = Seconds(5)
    _sum = s1 - s2
    assert repr(_sum) == "9.0s"
    _sum -= s3
    assert _sum.val == 4.0


def test_add_unit_and_number() -> None:
    s = Seconds(1.0)
    n = Number(-3)
    with pytest.raises(AssertionError):
        n += s  # type: ignore


def test_div_units() -> None:
    s1 = Seconds(7.0)
    s2 = Seconds(3.0)
    assert (s1 // s2).val == 2
    assert repr(s1 // s2) == "2.0"
    assert (s1 / s2).val == 7 / 3
    assert repr(s1 / s2) == repr(7 / 3)


def test_div_mixed() -> None:
    s1 = Seconds(7.0)
    assert (s1 / 2).val == 7.0 / 2
    m1 = Meters(3.0)
    assert repr(m1 / s1) == repr(3 / 7) + "m*s^(-1)"
    assert repr(s1 / m1) == repr(7 / 3) + "m^(-1)*s"
    assert repr(14 / s1) == "2.0s^(-1)"


def test_mod_units() -> None:
    s1 = Seconds(7.0)
    s2 = Seconds(5.0)
    assert repr(s1 % s2) == "2.0s"


def test_mul_units() -> None:
    s1 = Seconds(2.0)
    assert repr(s1 * s1) == "4.0s^2"
    m1 = Meters(7)
    assert repr(s1 * m1) == "14.0m*s"
    assert repr(3 * m1) == "21.0m"


def test_pow_units() -> None:
    s1 = Seconds(2.0)
    n = Number(2)
    assert repr(s1 ** 2) == "4.0s^2"
    assert repr(s1 ** n) == "4.0s^2"
    assert repr(2 ** n) == "4.0"
