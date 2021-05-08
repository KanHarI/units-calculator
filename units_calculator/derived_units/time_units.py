"""A module containing common derived time units"""

from units_calculator.si_units import Seconds
from units_calculator.units_bases import DerivedUnit


class Milliseconds(DerivedUnit):
    """Milliseconds"""

    __symbol__ = "ms"
    __base_units__ = [(Seconds, 1)]
    __multiplier__ = 1e-3


class Microseconds(DerivedUnit):
    """Microseconds"""

    __symbol__ = "us"
    __base_units__ = [(Milliseconds, 1)]
    __multiplier__ = 1e-3


class Nanoseconds(DerivedUnit):
    """Nanoseconds"""

    __symbol__ = "ns"
    __base_units__ = [(Microseconds, 1)]
    __multiplier__ = 1e-3


class Gigaseconds(DerivedUnit):
    """Gigaseconds"""

    __symbol__ = "Gs"
    __base_units__ = [(Seconds, 1)]
    __multiplier__ = 1e9


class Teraseconds(DerivedUnit):
    """Teraseconds"""

    __symbol__ = "Ts"
    __base_units__ = [(Gigaseconds, 1)]
    __multiplier__ = 1e3


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
