"""A module containing area units definitions"""

from units_calculator.base_units.si_units import Meters
from units_calculator.engine.engine import DerivedUnit


class SquaredMeters(DerivedUnit):
    """Squared meters"""

    __symbol__ = "m2"
    __base_units__ = [(Meters, 2)]
