from units_calculator.derived_units import Milliseconds, Milligrams


def test_create_derived_unit() -> None:
    x = Milliseconds(4.0)
    assert repr(x) == "4.0ms"


def test_created_subderived_unit() -> None:
    x = Milligrams(6)
    assert repr(x) == "6.0mg"
    assert x.base_units_val == 6e-6
