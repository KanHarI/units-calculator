from units_calculator.derived_units import MilliSeconds


def test_create_derived_unit():
    x = MilliSeconds(4.0)
    assert repr(x) == "4.0ms"
