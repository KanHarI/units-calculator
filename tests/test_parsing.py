from units_calculator.all import Kilograms, Meters, Seconds, parse, parse_pure_units


def test_parse_pure_units() -> None:
    test_str = "s^(-1)*kg*m/s"
    x = parse_pure_units(test_str)
    assert tuple(x) == ((Seconds, -2), (Kilograms, 1), (Meters, 1))
    assert tuple(parse_pure_units("")) == ()


def test_prase_units() -> None:
    _5m = parse("5m")
    _25m2 = parse("25m^2")
    assert repr(_5m) == "5.0m"
    assert _5m * _5m == _25m2
