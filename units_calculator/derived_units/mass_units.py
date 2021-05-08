"""A module containing weight unit definitions"""

from units_calculator.base_units.si_units import Kilograms
from units_calculator.engine.engine import DerivedUnit


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


class Megatonnes(DerivedUnit):
    """Megatonnes"""

    __symbol__ = "Mt"
    __base_units__ = [(Tonnes, 1)]
    __multiplier__ = 1e6


class Gigatonnes(DerivedUnit):
    """Gigatonnes"""

    __symbol__ = "Gt"
    __base_units__ = [(Megatonnes, 1)]
    __multiplier__ = 1e3


class Daltons(DerivedUnit):
    """Daltons"""

    __symbol__ = "Da"
    __base_units__ = [(Kilograms, 1)]
    __multiplier__ = 1.66053906606050e-27


class Slugs(DerivedUnit):
    """Slugs"""

    __symbol__ = "sl"
    __base_units__ = [(Kilograms, 1)]
    __multiplier__ = 14.59390


class Pounds(DerivedUnit):
    """Pounds"""

    __symbol__ = "lb"
    __base_units__ = [(Kilograms, 1)]
    __multiplier__ = 0.45359237


class SolarMasses(DerivedUnit):
    """Solar masses"""

    __symbol__ = "M☉"
    __base_units__ = [(Kilograms, 1)]
    __multiplier__ = 1.98847e30
