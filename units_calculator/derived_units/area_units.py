"""A module containing area units definitions"""

from units_calculator.base_units.si_units import Meters
from units_calculator.derived_units.length_units import Centimeters, Millimeters, Kilometers, Feet, Yards, Miles
from units_calculator.engine.engine import DerivedUnit


class SquareMeters(DerivedUnit):
    """Square meters"""

    __symbol__ = "m2"
    __base_units__ = [(Meters, 2)]


class SquareCentimeters(DerivedUnit):
    """Square centimeters"""

    __symbol__ = "cm2"
    __base_units__ = [(Centimeters, 2)]


class SquareMillimeters(DerivedUnit):
    """Square millimeters"""

    __symbol__ = "mm2"
    __base_units__ = [(Millimeters, 2)]


class SquareKilometers(DerivedUnit):
    """Square kilometers"""

    __symbol__ = "km2"
    __base_units__ = [(Kilometers, 2)]


class SquareFeet(DerivedUnit):
    """Square feet"""

    __symbol__ = "ft2"
    __base_units__ = [(Feet, 2)]


class SquareYards(DerivedUnit):
    """Square yards"""

    __symbol__ = "yd2"
    __base_units__ = [(Yards, 2)]


class SquareMiles(DerivedUnit):
    """Square miles"""

    __symbol__ = "mi2"
    __base_units__ = [(Miles, 2)]


class Acres(DerivedUnit):
    """Acres"""

    __symbol__ = "ac"
    __base_units__ = [(Meters, 2)]
    __multiplier__ = 4064.9


class Hectares(DerivedUnit):
    """Hectares"""

    __symbol__ = "ha"
    __base_units__ = [(Meters, 2)]
    __multiplier__ = 1e4


class Barn(DerivedUnit):
    """Barns"""

    __symbol__ = "b"
    __base_units__ = [(Meters, 2)]
    __multiplier__ = 1e-28
