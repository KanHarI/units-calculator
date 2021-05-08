"""A module for volume units"""

from units_calculator.base_units.si_units import Meters
from units_calculator.derived_units.length_units import (
    Centimeters,
    Decimeters,
    Inches,
    Yards,
)
from units_calculator.engine.engine import DerivedUnit


class CubicMeters(DerivedUnit):
    """Cubic meters"""

    __symbol__ = "m3"
    __base_units__ = [(Meters, 3)]


class CubicCentimeters(DerivedUnit):
    """Cubic centimeters"""

    __symbol__ = "cc"
    __base_units__ = [(Centimeters, 3)]


class Litre(DerivedUnit):
    """Litres"""

    __symbol__ = "l"
    __base_units__ = [(Decimeters, 3)]


class Decilitres(DerivedUnit):
    """Decilitres"""

    __symbol__ = "dl"
    __base_units__ = [(Litre, 1)]
    __multiplier__ = 1e-1


class Centilitres(DerivedUnit):
    """Centilitres"""

    __symbol__ = "cl"
    __base_units__ = [(Litre, 1)]
    __multiplier__ = 1e-2


class Millilitres(DerivedUnit):
    """Millilitres"""

    __symbol__ = "ml"
    __base_units__ = [(Litre, 1)]
    __multiplier__ = 1e-3


class Microlitres(DerivedUnit):
    """Microlitres"""

    __symbol__ = "ul"
    __base_units__ = [(Millilitres, 1)]
    __multiplier__ = 1e-3


class Kilolitres(DerivedUnit):
    """Kilolitres"""

    __symbol__ = "kl"
    __base_units__ = [(Litre, 1)]
    __multiplier__ = 1e3


class Megalitres(DerivedUnit):
    """Megalitres"""

    __symbol__ = "Ml"
    __base_units__ = [(Kilolitres, 1)]
    __multiplier__ = 1e3


class CubicInches(DerivedUnit):
    """Cubic inches"""

    __symbol__ = "in3"
    __base_units__ = [(Inches, 3)]


class CubicYard(DerivedUnit):
    """Cubic yard"""

    __symbol__ = "yd3"
    __base_units__ = [(Yards, 3)]


class ImperialFluidOunces(DerivedUnit):
    """Imperial fluid ounces"""

    __symbol__ = "imp_fl_oz"
    __base_units__ = [(Millilitres, 1)]
    __multiplier__ = 28.41306


class USFluidOunces(DerivedUnit):
    """US fluid ounces"""

    __symbol__ = "US_fl_oz"
    __base_units__ = [(Millilitres, 1)]
    __multiplier__ = 29.5735295625


class ImperialGallon(DerivedUnit):
    """Imperial gallons"""

    __symbol__ = "imp_gal"
    __base_units__ = [(Litre, 1)]
    __multiplier__ = 4.54609


class USGallons(DerivedUnit):
    """US gallons"""

    __symbol__ = "US_gal"
    __base_units__ = [(Litre, 1)]
    __multiplier__ = 3.785411784


class USDryGallons(DerivedUnit):
    """US dry gallons"""

    __symbol__ = "US_dry_gal"
    __base_units__ = [(Litre, 1)]
    __multiplier__ = 4.40488377086


class ImperialQuarts(DerivedUnit):
    """Imperial quarts"""

    __symbol__ = "imp_qt"
    __base_units__ = [(Litre, 1)]
    __multiplier__ = 1.13652


class USQuarts(DerivedUnit):
    """US quarts"""

    __symbol__ = "US_qt"
    __base_units__ = [(Litre, 1)]
    __multiplier__ = 0.9463529460


class USDryQuarts(DerivedUnit):
    """US dry quarts"""

    __symbol__ = "US_dry_qt"
    __base_units__ = [(Litre, 1)]
    __multiplier__ = 1.101220942715


class ImperialPints(DerivedUnit):
    """Imperial pints"""

    __symbol__ = "imp_pt"
    __base_units__ = [(Millilitres, 1)]
    __multiplier__ = 568.26125


class USPints(DerivedUnit):
    """US pints"""

    __symbol__ = "US_pt"
    __base_units__ = [(Millilitres, 1)]
    __multiplier__ = 473.176473


class USDryPints(DerivedUnit):
    """US dry pints"""

    __symbol__ = "US_dry_pt"
    __base_units__ = [(Millilitres, 1)]
    __multiplier__ = 550.610471
