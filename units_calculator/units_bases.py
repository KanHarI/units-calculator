"""A module containing metaclass for all unit classes"""

from __future__ import annotations

from typing import Any, Type, cast


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
            namespace["__dimensions__"] = list()
            result = cast(UnitsMeta, super().__new__(cls, name, bases, namespace))
            namespace["__dimensions__"].append((idx, 1, result))
            dimensions_dict[symbol] = idx, result
            idx_to_dimension[idx] = symbol, result
        else:
            result = cast(UnitsMeta, super().__new__(cls, name, bases, namespace))
        return result


dimensions_dict: dict[str, tuple[int, UnitsMeta]] = dict()
idx_to_dimension: dict[int, tuple[str, UnitsMeta]] = dict()

# A list of dimensions and their exponents
Dimensions = list[tuple[int, int, UnitsMeta]]


class Unit(metaclass=UnitsMeta):
    """A base class for all units"""

    def __init__(self, numerical_val: complex, dimensions: Dimensions):
        self._dimensions: Dimensions = dimensions
        self._numerical_val: complex = numerical_val * self.units_factor

    def _is_matching_dimensions(self, other: Unit) -> bool:
        if len(self._dimensions) != len(
            other._dimensions  # pylint: disable=protected-access
        ):
            return False
        for dimension1, dimension2 in zip(
            self._dimensions, other._dimensions  # pylint: disable=protected-access
        ):
            idx1, exp1, _ = dimension1
            idx2, exp2, _ = dimension2
            if (idx1, exp1) != (idx2, exp2):
                return False
        return True

    def _clone(self) -> Unit:
        return Unit(self._numerical_val, self._dimensions)

    @property
    def units_string(self) -> str:
        """Return string representation of units"""
        units_representation_parts: list[str] = list()
        for _, exp, unit in self._dimensions:
            units_representation_atom = unit.__symbol__  # type: ignore
            if exp != 1:
                units_representation_atom += (
                    f"^{str(exp) if exp > 0 else '(' + str(exp) + ')'}"
                )
            units_representation_parts.append(units_representation_atom)
        return "*".join(units_representation_parts)

    @property
    def units_factor(self) -> complex:
        """Get units factor to base unit"""
        units_factor = 1
        for _, exp, unit in self._dimensions:
            units_factor *= unit.__multiplier__ ** exp  # type: ignore
        return units_factor

    @property
    def val(self) -> complex:
        """Get current unit numerical value"""
        return self._numerical_val / self.units_factor

    @property
    def base_units_val(self):
        """Return value in base units"""
        return self._numerical_val

    def __repr__(self):
        numerical_representation = repr(self.val)
        units_representation = self.units_string
        return numerical_representation + units_representation

    def __iadd__(self, other: Unit) -> Unit:
        assert self._is_matching_dimensions(other)
        self._numerical_val += other._numerical_val
        return self

    def __add__(self, other: Unit) -> Unit:
        new_unit = self._clone()
        new_unit += other
        return new_unit


class BaseUnit(Unit):
    """A class for base units"""

    __dimensions__: Dimensions
    __symbol__: str
    __multiplier__: complex = 1

    def __init__(self, numerical_val: complex):
        super().__init__(numerical_val, self.__dimensions__)


class DerivedUnit(Unit):
    """A base class for derived units"""

    __base_unit__: Type[UnitsMeta]
    __symbol__: str
    __multiplier__: complex


class Number(Unit):
    """A class for unitless numbers"""

    __multiplier__: complex = 1

    def __init__(self, numerical_val: complex):
        super().__init__(numerical_val, list())
