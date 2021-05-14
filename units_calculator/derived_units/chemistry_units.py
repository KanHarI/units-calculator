"""A module for chemistry units"""

from units_calculator.derived_units.volume_units import Litre
from units_calculator.engine.engine import DerivedUnit
from units_calculator.si_units.si_units import Mols


class Molars(DerivedUnit):
    """Molars"""

    __symbol__ = "M"
    __base_units__ = [(Mols, 1), (Litre, -1)]


class Millimolars(DerivedUnit):
    """Millimolars"""

    __symbol__ = "mM"
    __base_units__ = [(Molars, 1)]
    __multiplier__ = 1e-3
