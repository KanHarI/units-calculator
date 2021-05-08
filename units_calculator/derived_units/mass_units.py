"""A module containing weight unit definitions"""

from units_calculator.si_units import Kilograms
from units_calculator.units_bases import DerivedUnit


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
