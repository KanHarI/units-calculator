"""A module containing metaclass for all unit classes"""
from typing import Any


class UnitsMeta(type):
    """A metaclass for all unit classes"""

    def __new__(
        mcs: type,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        *args,
        **kwargs
    ):
        """Check required attributes exists in unit class"""
        return super().__new__(mcs, name, bases, namespace, *args, **kwargs)  # type: ignore
