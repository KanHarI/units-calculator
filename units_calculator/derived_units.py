"""A module for derived units"""

from units_calculator.si_units import Seconds
from units_calculator.units_bases import DerivedUnit


class MilliSeconds(DerivedUnit):
    """Milliseconds"""

    __symbol__ = "ms"
    __base_units__ = [(Seconds, 1)]
    __multiplier__ = 1e-3
