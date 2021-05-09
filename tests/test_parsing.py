from units_calculator.all import parse_pure_units, Seconds, Kilograms, Meters


def test_parse_pure_units() -> None:
    test_str = "s^(-1)*kg*m/s"
    x = parse_pure_units(test_str)
    assert tuple(x) == ((Seconds, -2), (Kilograms, 1), (Meters, 1))
