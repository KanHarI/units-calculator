"""A module containing metaclass for all unit classes"""

from __future__ import annotations

import copy
import math
from typing import Any, Optional, Type, Union, cast


class UnitsMeta(type):
    """A metaclass for all unit classes"""

    def __new__(
        cls: Type[UnitsMeta], name: str, bases: tuple, namespace: dict[str, Any]
    ) -> UnitsMeta:
        """Check required attributes exists in unit class"""
        symbol: Optional[str] = (
            namespace["__symbol__"] if "__symbol__" in namespace else None
        )
        if symbol is None:
            return cast(UnitsMeta, super().__new__(cls, name, bases, namespace))
        assert symbol.isalpha()
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
Dimension = tuple[int, int, UnitsMeta]
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
        return Unit(self._numerical_val, copy.deepcopy(self._dimensions))

    @property
    def units_string(self) -> str:
        """Return string representation of units"""
        units_representation_parts: list[str] = list()
        for _, exp, unit in self._dimensions[::-1]:  # start with least common units
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

    def __lt__(self, other: Unit) -> bool:
        assert self._is_matching_dimensions(other)
        return self._numerical_val < other._numerical_val  # type: ignore

    def __le__(self, other: Unit) -> bool:
        assert self._is_matching_dimensions(other)
        return self._numerical_val <= other._numerical_val  # type: ignore

    def __eq__(self, other: object) -> bool:
        assert isinstance(other, Unit)
        assert self._is_matching_dimensions(other)
        return self._numerical_val == other._numerical_val

    def __ge__(self, other: Unit) -> bool:
        assert self._is_matching_dimensions(other)
        return self._numerical_val >= other._numerical_val  # type: ignore

    def __gt__(self, other: Unit) -> bool:
        assert self._is_matching_dimensions(other)
        return self._numerical_val > other._numerical_val  # type: ignore

    def __iadd__(self, other: Unit) -> Unit:
        assert self._is_matching_dimensions(other)
        self._numerical_val += other._numerical_val
        return self

    def __add__(self, other: Unit) -> Unit:
        new_unit = self._clone()
        new_unit += other
        return new_unit

    def __neg__(self) -> Unit:
        self._numerical_val = -self._numerical_val
        return self

    def __sub__(self, other: Unit) -> Unit:
        return self + (-other)

    def __ifloordiv__(self, other: Unit) -> Unit:
        assert self._is_matching_dimensions(other)
        self._dimensions = list()
        self._numerical_val = math.floor(self._numerical_val / other._numerical_val)  # type: ignore
        return self

    def __floordiv__(self, other: Unit) -> Unit:
        new_unit = self._clone()
        new_unit //= other
        return new_unit

    def _itruediv_unit(self, other: Unit) -> Unit:
        it1, it2 = 0, 0
        result_dimensions: Dimensions = list()
        while it1 < len(
            self._dimensions  # pylint: disable=protected-access
        ) or it2 < len(
            other._dimensions  # pylint: disable=protected-access
        ):
            d1: Optional[Dimension] = None
            d2: Optional[Dimension] = None
            if it1 < len(self._dimensions):
                d1 = self._dimensions[it1]
            if it2 < len(other._dimensions):  # pylint: disable=protected-access
                d2 = other._dimensions[it2]  # pylint: disable=protected-access
            if d1 is not None and d2 is not None:
                if d1[0] == d2[0]:
                    if d1[1] != d2[1]:  # Remove dimensions with exponent 0
                        result_dimensions.append((d1[0], d1[1] - d2[1], d1[2]))
                    it1 += 1
                    it2 += 1
                elif d1[0] < d2[0]:
                    result_dimensions.append(d1)
                    it1 += 1
                else:
                    result_dimensions.append((d2[0], -d2[1], d2[2]))
                    it2 += 1
            elif d1 is not None:
                result_dimensions.append(d1)
                it1 += 1
            elif d2 is not None:
                result_dimensions.append((d2[0], -d2[1], d2[2]))
                it2 += 1
            else:
                raise RuntimeError("Bad dimensionality unit")
        self._dimensions = result_dimensions
        self._numerical_val /= other._numerical_val  # pylint: disable=protected-access
        return self

    def __itruediv__(self, other: Union[Unit, complex]) -> Unit:
        if isinstance(other, Unit):
            return self._itruediv_unit(other)
        else:
            self._numerical_val /= other
            return self

    def __truediv__(self, other: Union[Unit, complex]) -> Unit:
        new_unit = self._clone()
        new_unit /= other
        return new_unit

    def __rtruediv__(self, other: complex) -> Unit:
        return Number(other) / self

    def __imod__(self, other: Unit) -> Unit:
        assert self._is_matching_dimensions(other)
        self._numerical_val %= other._numerical_val  # type: ignore
        return self

    def __mod__(self, other: Unit) -> Unit:
        new_unit = self._clone()
        new_unit %= other
        return new_unit

    def _imul_unit(self, other: Unit) -> Unit:
        it1, it2 = 0, 0
        result_dimensions: Dimensions = list()
        while it1 < len(
            self._dimensions
        ) or it2 < len(  # pylint: disable=protected-access
            other._dimensions  # pylint: disable=protected-access
        ):
            d1: Optional[Dimension] = None
            d2: Optional[Dimension] = None
            if it1 < len(self._dimensions):
                d1 = self._dimensions[it1]
            if it2 < len(other._dimensions):  # pylint: disable=protected-access
                d2 = other._dimensions[it2]  # pylint: disable=protected-access
            if d1 is not None and d2 is not None:
                if d1[0] == d2[0]:
                    if d1[1] != -d2[1]:  # Remove dimensions with exponent 0
                        result_dimensions.append((d1[0], d1[1] + d2[1], d1[2]))
                    it1 += 1
                    it2 += 1
                elif d1[0] < d2[0]:
                    result_dimensions.append(d1)
                    it1 += 1
                else:
                    result_dimensions.append(d2)
                    it2 += 1
            elif d1 is not None:
                result_dimensions.append(d1)
                it1 += 1
            elif d2 is not None:
                result_dimensions.append(d2)
                it2 += 1
            else:
                raise RuntimeError("Bad dimensionality unit")
        self._dimensions = result_dimensions
        self._numerical_val *= other._numerical_val  # pylint: disable=protected-access
        return self

    def __imul__(self, other: Union[Unit, complex]):
        if isinstance(other, Unit):
            return self._imul_unit(other)
        else:
            self._numerical_val *= other
            return self

    def __mul__(self, other: Union[Unit, complex]) -> Unit:
        new_unit = self._clone()
        new_unit *= other
        return new_unit

    def __rmul__(self, other: complex) -> Unit:
        return Number(other) * self

    def _ipow_unit(self, other: Unit):
        # Exponent should be dimensionless
        assert len(other._dimensions) == 0  # pylint: disable=protected-access
        self **= other._numerical_val  # pylint: disable=protected-access
        return self

    def __ipow__(self, other: Union[Unit, complex]) -> Unit:
        if isinstance(other, Unit):
            return self._ipow_unit(other)
        else:
            if len(self._dimensions) > 0:
                exponent = int(math.floor(other))  # type: ignore
                assert exponent == other
            else:
                exponent = other  # type: ignore
            self._numerical_val **= exponent
            if len(self._dimensions) > 0:
                for i in range(len(self._dimensions)):
                    d: Dimension = self._dimensions[i]
                    d = (d[0], int(d[1] * exponent), d[2])
                    self._dimensions[i] = d
            return self

    def __pow__(self, other: Union[Unit, complex]) -> Unit:
        new_unit = self._clone()
        new_unit **= other
        return new_unit

    def __rpow__(self, other: complex) -> Unit:
        # Exponent must be dimensionless
        assert len(self._dimensions) == 0
        return Number(other) ** self


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
