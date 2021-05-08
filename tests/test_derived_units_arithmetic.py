import math

from units_calculator.base_units.si_units import Meters, Seconds
from units_calculator.derived_units.area_units import SquaredMeters
from units_calculator.derived_units.mass_units import Milligrams
from units_calculator.derived_units.time_units import Milliseconds


def test_create_derived_unit() -> None:
    x = Milliseconds(4.0)
    assert repr(x) == "4.0ms"


def test_created_subderived_unit() -> None:
    x = Milligrams(6)
    assert repr(x) == "6.0mg"
    assert abs(x.base_units_val - 6e-6) < 1e-16


def test_add_mixed_units() -> None:
    s1 = Seconds(0.5)
    s2 = Milliseconds(100)
    assert repr(s1 + s2) == "0.6s"
    assert repr(s2 + s1) == "600.0ms"


def test_higher_dimensionality_units() -> None:
    a1 = SquaredMeters(2)
    l1 = Meters(4)
    assert repr(a1) == "2.0m2"
    assert repr(a1 / l1) == "0.5m"
