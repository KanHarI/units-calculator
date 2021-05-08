from units_calculator.derived_units.area_units import SquareCentimeters, SquareMeters
from units_calculator.derived_units.mass_units import Milligrams
from units_calculator.derived_units.time_units import Milliseconds
from units_calculator.derived_units.volume_units import (
    CubicCentimeters,
    CubicInches,
    Millilitres,
    USQuarts,
)
from units_calculator.si_units.si_units import Meters, Seconds


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
    a1 = SquareMeters(2)
    l1 = Meters(4)
    assert repr(a1) == "2.0m2"
    assert repr(a1 / l1) == "0.5m"


def test_high_dimensional_scaled_units() -> None:
    a1 = SquareCentimeters(50)
    assert repr(a1.as_base_units()) == "0.005m^2"


def test_multiple_pathways_to_same_unit() -> None:
    assert CubicCentimeters(5) == Millilitres(5)


def test_us_units() -> None:
    assert 57 < USQuarts(1) / CubicInches(1) < 58
