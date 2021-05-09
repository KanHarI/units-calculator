"""A module containing metaclass for all unit classes"""

from __future__ import annotations

import copy
import math
from typing import Any, Optional, Type, Union, cast

from ordered_set import OrderedSet  # type: ignore

UNITS_CHARACTERS_BLACKLIST = "*/ "
UNITS_START_CHARACTERS_BLACKLIST = "0123456789e+-^(-)" + UNITS_CHARACTERS_BLACKLIST


class UnitsMeta(type):
    """A metaclass for all unit classes"""

    __acc_multiplier__: complex
    __dimensions__: Dimensions
    __symbol__: str

    def __new__(
        cls: Type[UnitsMeta],
        name: str,
        bases: tuple,  # type: ignore
        namespace: dict[str, Any],
    ) -> UnitsMeta:
        """Check required attributes exists in unit class"""
        # pylint: disable=too-many-locals
        symbol: Optional[str] = (
            namespace["__symbol__"] if "__symbol__" in namespace else None
        )
        if symbol is None:
            return cast(UnitsMeta, super().__new__(cls, name, bases, namespace))
        assert symbol[0] not in UNITS_START_CHARACTERS_BLACKLIST
        assert all(character not in UNITS_CHARACTERS_BLACKLIST for character in symbol)
        is_base_unit = symbol is not None and BaseUnit in bases
        is_derived_unit = symbol is not None and DerivedUnit in bases
        if symbol in dimensions_dict:
            raise RuntimeError(f"{symbol} defined twice!")
        if is_base_unit:
            idx = len(dimensions_dict)
            dimensions: Dimensions = list()
            namespace["__dimensions__"] = dimensions
            namespace["__acc_multiplier__"] = 1
            result = cast(UnitsMeta, super().__new__(cls, name, bases, namespace))
            dimensions.append((idx, 1, result))
            dimensions_dict[symbol] = idx, result
            idx_to_dimension[idx] = symbol, result
        elif is_derived_unit:
            src_dimensions: list[tuple[UnitsMeta, int]] = namespace["__base_units__"]
            dimensions = list()
            namespace["__dimensions__"] = dimensions
            multiplier: complex = namespace.get("__multiplier__", 1)
            dimensions_idx_dict: dict[int, Dimension] = dict()
            for src_dimension in src_dimensions:
                src_unit, derived_exp = src_dimension
                src_unit_dimensions: Dimensions = src_unit.__dimensions__
                for idx, source_exp, base_unit in src_unit_dimensions:
                    existing_dimension = dimensions_idx_dict.get(
                        idx, (idx, 0, base_unit)
                    )
                    existing_dimension = (
                        existing_dimension[0],
                        existing_dimension[1] + source_exp * derived_exp,
                        existing_dimension[2],
                    )
                    multiplier *= src_unit.__acc_multiplier__ ** derived_exp
                    dimensions_idx_dict[idx] = existing_dimension
            namespace["__acc_multiplier__"] = multiplier
            dimension_idx_keys = list(dimensions_idx_dict.keys())
            dimension_idx_keys.sort()
            for idx in dimension_idx_keys:
                _, exp, base_unit = dimensions_idx_dict[idx]
                if exp != 0:
                    dimensions.append((idx, exp, base_unit))
            result = cast(UnitsMeta, super().__new__(cls, name, bases, namespace))
            dimensions_dict[symbol] = None, result
        else:
            result = cast(UnitsMeta, super().__new__(cls, name, bases, namespace))
        return result


dimensions_dict: dict[str, tuple[Optional[int], UnitsMeta]] = dict()
idx_to_dimension: dict[int, tuple[str, UnitsMeta]] = dict()

# A list of dimensions and their exponents
Dimension = tuple[int, int, UnitsMeta]
Dimensions = list[tuple[int, int, UnitsMeta]]


class Unit(metaclass=UnitsMeta):
    """A base class for all units"""

    __dimensions__: Dimensions
    __symbol__: str
    __acc_multiplier__: complex

    def __init__(
        self,
        numerical_val: complex,
        dimensions: Dimensions,
        preferred_units: list[UnitsMeta],
    ):
        self._dimensions: Dimensions = dimensions
        self._preferred_units = preferred_units
        self._numerical_val: complex = numerical_val * self.units_factor

    # Basic functionality
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
        return Unit(
            self.val,
            copy.deepcopy(self._dimensions),
            copy.deepcopy(self._preferred_units),
        )

    @property
    def preferred_units_representation(self) -> list[tuple[UnitsMeta, int]]:
        """Returns preferred units for current unit dimensionality"""

        def _sum_dim_exp_squared(dimensions_exps: dict[int, int]) -> int:
            return sum(val ** 2 for val in dimensions_exps.values())

        def _add_n_unit_to_dimension(
            base_dimensions_exps: dict[int, int],
            unit_dimensions_exp: dict[int, int],
            n: int,
        ) -> dict[int, int]:
            return {
                idx: base_dimensions_exps[idx] + n * unit_dimensions_exp[idx]
                for idx in base_dimensions_exps.keys()
            }

        def _find_best_unit_exp(
            base_dimensions_exps: dict[int, int], unit_dimensions_exp: dict[int, int]
        ) -> int:
            current_sum_dim_exp_squared = _sum_dim_exp_squared(base_dimensions_exps)
            i = 0
            while True:
                next_unit_sum_dim_exp_squared = _sum_dim_exp_squared(
                    _add_n_unit_to_dimension(
                        base_dimensions_exps, unit_dimensions_exp, -i - 1
                    )
                )
                if next_unit_sum_dim_exp_squared >= current_sum_dim_exp_squared:
                    break
                i += 1
                current_sum_dim_exp_squared = next_unit_sum_dim_exp_squared
            if i > 0:
                return i
            i = 0
            while True:
                next_unit_sum_dim_exp_squared = _sum_dim_exp_squared(
                    _add_n_unit_to_dimension(
                        base_dimensions_exps, unit_dimensions_exp, -i + 1
                    )
                )
                if next_unit_sum_dim_exp_squared >= current_sum_dim_exp_squared:
                    break
                i -= 1
                current_sum_dim_exp_squared = next_unit_sum_dim_exp_squared
            return i

        result: list[tuple[UnitsMeta, int]] = list()
        remaining_dimensions: dict[int, int] = {
            idx: exp for idx, exp, _ in self._dimensions
        }
        for preferred_unit in self._preferred_units:
            preferred_unit_dimensions: dict[int, int] = {
                idx: exp for idx, exp, _ in preferred_unit.__dimensions__
            }
            for idx in remaining_dimensions.keys():
                if idx not in preferred_unit_dimensions:
                    preferred_unit_dimensions[idx] = 0
            for idx in preferred_unit_dimensions.keys():
                if idx not in remaining_dimensions:
                    remaining_dimensions[idx] = 0
            unit_exp = _find_best_unit_exp(
                remaining_dimensions, preferred_unit_dimensions
            )
            if unit_exp != 0:
                result.append((preferred_unit, unit_exp))
                remaining_dimensions = _add_n_unit_to_dimension(
                    remaining_dimensions, preferred_unit_dimensions, -unit_exp
                )
        idxs_to_pop: list[int] = list()
        for idx, exp in remaining_dimensions.items():
            if exp == 0:
                idxs_to_pop.append(idx)
        for idx in idxs_to_pop:
            remaining_dimensions.pop(idx)
        # Fill in remaining base dimensions
        for idx, _, _ in self._dimensions[::-1]:  # start with least common units
            if idx not in remaining_dimensions:
                continue
            result.append((idx_to_dimension[idx][1], remaining_dimensions[idx]))
        return result

    @property
    def units_string(self) -> str:
        """Return string representation of units"""
        units_representation_parts: list[str] = list()
        for unit, exp in self.preferred_units_representation:
            units_symbol: str = unit.__symbol__
            if exp != 1:
                units_symbol += f"^{str(exp) if exp > 0 else '(' + str(exp) + ')'}"
            units_representation_parts.append(units_symbol)
        return "*".join(units_representation_parts)

    @property
    def units_factor(self) -> complex:
        """Get units factor to base unit"""
        units_factor: complex = 1
        for unit, exp in self.preferred_units_representation:
            units_factor *= unit.__acc_multiplier__ ** exp
        return units_factor

    @property
    def val(self) -> complex:
        """Get current unit numerical value"""
        return self._numerical_val / self.units_factor

    @property
    def base_units_val(self) -> complex:
        """Return value in base units"""
        return self._numerical_val

    def _mrege_preferences(self, other: Unit) -> None:
        for (
            preferred_unit
        ) in other._preferred_units:  # pylint: disable=protected-access
            if preferred_unit not in self._preferred_units:
                self._preferred_units.append(preferred_unit)

    def __repr__(self) -> str:
        numerical_representation = repr(self.val)
        units_representation = self.units_string
        return numerical_representation + units_representation

    # Arithmetic functionality
    def __lt__(self, other: Union[Unit, complex]) -> bool:
        if isinstance(other, Unit):
            assert self._is_matching_dimensions(other)
            return self._numerical_val < other._numerical_val  # type: ignore
        else:
            return self < Number(other)

    def __le__(self, other: Union[Unit, complex]) -> bool:
        if isinstance(other, Unit):
            assert self._is_matching_dimensions(other)
            return self._numerical_val <= other._numerical_val  # type: ignore
        else:
            return self <= Number(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Unit):
            assert self._is_matching_dimensions(other)
            return self._numerical_val == other._numerical_val
        else:
            if isinstance(other, (complex, float, int)):
                return self == Number(other)
            raise RuntimeError(f"Bad type in comparison with unit: {other}")

    def __ge__(self, other: Union[Unit, complex]) -> bool:
        if isinstance(other, Unit):
            assert self._is_matching_dimensions(other)
            return self._numerical_val >= other._numerical_val  # type: ignore
        else:
            return self >= Number(other)

    def __gt__(self, other: Union[Unit, complex]) -> bool:
        if isinstance(other, Unit):
            assert self._is_matching_dimensions(other)
            return self._numerical_val > other._numerical_val  # type: ignore
        else:
            return self > Number(other)

    def __iadd__(self, other: Unit) -> Unit:
        assert self._is_matching_dimensions(other)
        self._numerical_val += other._numerical_val
        return self

    def __add__(self, other: Unit) -> Unit:
        new_unit = self._clone()
        new_unit += other
        self._mrege_preferences(other)
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
        self._mrege_preferences(other)
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
        self._mrege_preferences(other)
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
        result = Number(other) / self
        result._mrege_preferences(self)
        return result

    def __imod__(self, other: Unit) -> Unit:
        assert self._is_matching_dimensions(other)
        self._numerical_val %= other._numerical_val  # type: ignore
        self._mrege_preferences(other)
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
        self._mrege_preferences(other)
        return self

    def __imul__(self, other: Union[Unit, complex]) -> Unit:
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
        result = Number(other) * self
        result._mrege_preferences(self)
        return result

    def _ipow_unit(self, other: Unit) -> Unit:
        # Exponent should be dimensionless
        assert len(other._dimensions) == 0  # pylint: disable=protected-access
        self **= other._numerical_val  # pylint: disable=protected-access
        self._mrege_preferences(other)
        return self

    def __ipow__(self, other: Union[Unit, complex]) -> Unit:
        if isinstance(other, Unit):
            return self._ipow_unit(other)
        else:
            if len(self._dimensions) > 0:
                if isinstance(other, complex):
                    exponent = other.real
                else:
                    exponent = other
                exponent = int(math.floor(exponent))
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
        result = Number(other) ** self
        result._mrege_preferences(self)
        return result

    # Misc functions
    def as_base_units(self) -> Unit:
        """Return a unit without representation preferences"""
        new_unit = self._clone()
        new_unit._preferred_units = list()  # pylint: disable=protected-access
        return new_unit


class BaseUnit(Unit):
    """A class for base units"""

    def __init__(self, numerical_val: complex):
        super().__init__(numerical_val, self.__dimensions__, [self.__class__])


class DerivedUnit(Unit):
    """A base class for derived units"""

    __multiplier__: complex = 1
    __base_units__: list[tuple[UnitsMeta, int]]

    def __init__(self, numerical_val: complex):
        super().__init__(numerical_val, self.__dimensions__, [self.__class__])


class Number(Unit):
    """A class for unitless numbers"""

    __dimensions__: Dimensions = list()

    def __init__(self, numerical_val: complex):
        super().__init__(numerical_val, list(), list())


def parse_symbol(symbol: str) -> UnitsMeta:
    """Parse symbol as unit"""
    if symbol not in dimensions_dict:
        raise RuntimeError(f"Unrecognized symbol {symbol} in unit")
    return dimensions_dict[symbol][1]


def parse_pure_units(units_str: str) -> list[tuple[UnitsMeta, int]]:
    """Parse units string to list of units and exponents"""

    def _parse_pure_unit_exp(unit_exp_str: str) -> tuple[UnitsMeta, int]:
        unit_exp_parts = unit_exp_str.split("^")
        if len(unit_exp_parts) > 2:
            raise RuntimeError(f"Malformed unit: {unit_exp_str}")
        symbol = unit_exp_parts[0]
        unit = parse_symbol(symbol)
        exp = 1
        if len(unit_exp_parts) > 1:
            try:
                exp = int(unit_exp_parts[1].strip("()"))
            except ValueError as e:
                raise RuntimeError(
                    f"Cannot parse exponent {unit_exp_parts[1]} in unit {unit_exp_str}"
                ) from e
        return unit, exp

    def _parse_nodiv_unit_string(nodiv_str: str) -> list[tuple[UnitsMeta, int]]:
        _result: list[tuple[UnitsMeta, int]] = list()
        if len(nodiv_str) == 0:
            return _result
        units_exps = nodiv_str.split("*")
        for unit_exp in units_exps:
            _result.append(_parse_pure_unit_exp(unit_exp))
        return _result

    div_parts = units_str.split("/")
    if len(div_parts) > 2:
        raise RuntimeError("Cant have multiple '/' characters in unit string!")
    result_parts: list[tuple[UnitsMeta, int]] = _parse_nodiv_unit_string(div_parts[0])
    if len(div_parts) > 1:
        result_parts += [
            (unit, -exp) for (unit, exp) in _parse_nodiv_unit_string(div_parts[1])
        ]
    units = OrderedSet(unit for unit, _ in result_parts)
    result: list[tuple[UnitsMeta, int]] = list()
    for unit in units:
        exp = 0
        for res_unit, res_exp in result_parts:
            if res_unit is unit:
                exp += res_exp
        if exp != 0:
            result.append((unit, exp))
    return result
