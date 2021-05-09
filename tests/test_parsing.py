from units_calculator.si_units.si_units import Seconds, Kilograms, Meters
from units_calculator.all import parse_pure_units


def test_parse_pure_units() -> None:
    test_str = "s^(-1)*kg*m/s"
    x = parse_pure_units(test_str)
    assert tuple(x) == ((Seconds, -2), (Kilograms, 1), (Meters, 1))
