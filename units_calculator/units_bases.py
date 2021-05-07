"""A module containing metaclass for all unit classes"""

from __future__ import annotations

from typing import Any, Type, cast

# A list of dimensions and their exponents
Dimensions = list[tuple[int, int]]


class UnitsMeta(type):
    """A metaclass for all unit classes"""

    def __new__(
        cls: Type[UnitsMeta], name: str, bases: tuple, namespace: dict[str, Any]
    ) -> UnitsMeta:
        """Check required attributes exists in unit class"""
        symbol = namespace["__symbol__"] if "__symbol__" in namespace else None
        is_base_unit = symbol is not None and BaseUnit in bases
        if symbol in dimensions_dict:
            raise RuntimeError(f"{symbol} defined twice!")
        if is_base_unit:
            idx = len(dimensions_dict)
            namespace["__dimensions__"] = [(idx, 1)]
            result = cast(UnitsMeta, super().__new__(cls, name, bases, namespace))
            dimensions_dict[symbol] = idx, result
            idx_to_dimension[idx] = symbol, result
        else:
            result = cast(UnitsMeta, super().__new__(cls, name, bases, namespace))
        return result


dimensions_dict: dict[str, tuple[int, UnitsMeta]] = dict()
idx_to_dimension: dict[int, tuple[str, UnitsMeta]] = dict()


class Unit(metaclass=UnitsMeta):
    """A base class for all units"""

    __dimensions__: Dimensions
    __symbol__: str

    def __init__(self, numerical_val: complex, dimensions: Dimensions):
        self._numerical_val: complex = numerical_val
        self._dimensions: Dimensions = dimensions

    def __repr__(self):
        return repr(self._numerical_val) + self.__symbol__


class BaseUnit(Unit):
    """A class for base units"""

    __base_unit__: bool = True

    def __init__(self, numerical_val: complex):
        super().__init__(numerical_val, self.__dimensions__)


class DerivedUnit(Unit):
    """A base class for derived units"""

    __base_unit__: bool = False
