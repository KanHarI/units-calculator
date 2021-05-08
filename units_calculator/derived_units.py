"""A module for derived units"""

from units_calculator.si_units import Kilograms, Seconds
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


class Grams(DerivedUnit):
    """Grams"""

    __symbol__ = "g"
    __base_units__ = [(Kilograms, 1)]
    __multiplier__ = 1e-3


#
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
