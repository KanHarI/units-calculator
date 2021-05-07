"""A base class for all units classes"""

from units_calculator.units_meta import UnitsMeta


class BaseUnit(metaclass=UnitsMeta):
    """A class for base units"""

    __base_unit__: bool = True
