"""A module for derived units"""

from units_calculator.si_units import Kilograms, Seconds
from units_calculator.units_bases import DerivedUnit


class Milliseconds(DerivedUnit):
    """Milliseconds"""

    __symbol__ = "ms"
    __base_units__ = [(Seconds, 1)]
    __multiplier__ = 1e-3


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
