"""A module for derived units"""

from units_calculator.si_units import Kilograms, Seconds, Meters
from units_calculator.units_bases import DerivedUnit


# Time units
class Milliseconds(DerivedUnit):
    """Milliseconds"""

    __symbol__ = "ms"
    __base_units__ = [(Seconds, 1)]
    __multiplier__ = 1e-3


class Minutes(DerivedUnit):
    """Minutes"""

    __symbol__ = "min"
    __base_units__ = [(Seconds, 1)]
    __multiplier__ = 60


class Hours(DerivedUnit):
    """Hours"""

    __symbol__ = "h"
    __base_units__ = [(Minutes, 1)]
    __multiplier__ = 60


class Days(DerivedUnit):
    """Days"""

    __symbol__ = "d"
    __base_units__ = [(Hours, 1)]
    __multiplier__ = 24


class Weeks(DerivedUnit):
    """Weeks"""

    __symbol__ = "weeks"
    __base_units__ = [(Days, 1)]
    __multiplier__ = 7


class JulianYear(DerivedUnit):
    """Julian years"""

    __symbol__ = "a"
    __base_units__ = [(Days, 1)]
    __multiplier__ = 365.25


# Length units
class Decimeters(DerivedUnit):
    """Decimeters"""

    __symbol__ = "dm"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1e-1


class Centimeters(DerivedUnit):
    """Centimeters"""

    __symbol__ = "cm"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1e-2


class Millimeters(DerivedUnit):
    """Millimeters"""

    __symbol__ = "mm"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1e-3


class Micrometers(DerivedUnit):
    """Micrometers"""

    __symbol__ = "um"
    __base_units__ = [(Millimeters, 1)]
    __multiplier__ = 1e-3


class Nanometers(DerivedUnit):
    """Nanometers"""

    __symbol__ = "nm"
    __base_units__ = [(Micrometers, 1)]
    __multiplier__ = 1e-3


class Angstroms(DerivedUnit):
    """Angstroms"""

    __symbol__ = "Å"
    __base_units__ = [(Nanometers, 1)]
    __multiplier__ = 1e-10


class Picometers(DerivedUnit):
    """Picometers"""

    __symbol__ = "pm"
    __base_units__ = [(Nanometers, 1)]
    __multiplier__ = 1e-3


class Kilometers(DerivedUnit):
    """Kilometers"""

    __symbol__ = "km"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1e3


class Inches(DerivedUnit):
    """Inches"""

    __symbol__ = "in"
    __base_units__ = [(Millimeters, 1)]
    __multiplier__ = 25.4


class Feet(DerivedUnit):
    """Feet"""

    __symbol__ = "ft"
    __base_units__ = [(Inches, 1)]
    __multiplier__ = 12


class Yards(DerivedUnit):
    """Yards"""

    __symbol__ = "yd"
    __base_units__ = [(Feet, 1)]
    __multiplier__ = 3


class Miles(DerivedUnit):
    """Terrestrial miles"""

    __symbol__ = "mi"
    __base_units__ = [(Yards, 1)]
    __multiplier__ = 1760


class NauticalMiles(DerivedUnit):
    """Nautical miles"""

    __symbol__ = "nmi"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1852


class EarthRadii(DerivedUnit):
    """Earth radii"""

    __symbol__ = "R⊕"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 6.3781e6


class LunarDistances(DerivedUnit):
    """Lunar distances"""

    __symbol__ = "LD"
    __base_units__ = [(Kilometers, 1)]
    __multiplier__ = 384402


class AstronomicalUnits(DerivedUnit):
    """Astronomical units"""

    __symbol__ = "au"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 1.495978707e11


class LightYears(DerivedUnit):
    """Light years"""

    __symbol__ = "ly"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 9.4607e15


class Parsec(DerivedUnit):
    """Parsecs"""

    __symbol__ = "pc"
    __base_units__ = [(Meters, 1)]
    __multiplier__ = 3.0857e16


# Weight units
class Grams(DerivedUnit):
    """Grams"""

    __symbol__ = "g"
    __base_units__ = [(Kilograms, 1)]
    __multiplier__ = 1e-3


class Milligrams(DerivedUnit):
    """Milligrams"""

    __symbol__ = "mg"
    __base_units__ = [(Grams, 1)]
    __multiplier__ = 1e-3


class Micrograms(DerivedUnit):
    """Micrograms"""

    __symbol__ = "ug"
    __base_units__ = [(Milligrams, 1)]
    __multiplier__ = 1e-3


class Nanograms(DerivedUnit):
    """Nanograms"""

    __symbol__ = "ng"
    __base_units__ = [(Milligrams, 1)]
    __multiplier__ = 1e-3


class Tonnes(DerivedUnit):
    """Metric tonne"""

    __symbol__ = "t"
    __base_units__ = [(Kilograms, 1)]
    __multiplier__ = 1e3
