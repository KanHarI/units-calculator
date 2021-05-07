from units_calculator.si_units import Seconds


def test_create_direct_unit():
    s = Seconds(5.0)
    assert repr(s) == "5.0s"
