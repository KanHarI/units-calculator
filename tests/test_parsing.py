from units_calculator.all import (
    Kilograms,
    Meters,
    Milliseconds,
    Seconds,
    parse,
    parse_pure_units,
)


def test_parse_pure_units() -> None:
    test_str = "s^(-1)*kg*m/s"
    x = parse_pure_units(test_str)
    assert tuple(x) == ((Seconds, -2), (Kilograms, 1), (Meters, 1))
    assert tuple(parse_pure_units("")) == ()


def test_prase_int_units() -> None:
    _5m = parse("5m")
    _25m2 = parse("25m^2")
    assert repr(_5m) == "5.0m"
    assert _5m * _5m == _25m2


def test_parse_vloat_units() -> None:
    _2500ms = parse("2.5s")
    assert _2500ms == Milliseconds(2500)


def test_parse_complex_units() -> None:
    _jA = parse("jA")
    assert repr(_jA) == "1jA"
    _3p2jA = parse("(3+2.5j)A")
    assert repr(_3p2jA) == "(3+2.5j)A"
