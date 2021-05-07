"""A module for SI units definition.
See https://en.wikipedia.org/wiki/International_System_of_Units"""

from units_calculator.baseunit import BaseUnit


class Seconds(BaseUnit):
    """Seconds"""

    __symbol__: str = "s"


class Meters(BaseUnit):
    """Meters"""

    __symbol__: str = "m"


class Kilograms(BaseUnit):
    """Kilograms"""

    __symbol__: str = "kg"


class Amperes(BaseUnit):
    """Amperes"""

    __symbol__: str = "A"


class Kelvins(BaseUnit):
    """Kelvins"""

    __symbol__: str = "K"


class Mols(BaseUnit):
    """Mols"""

    __symbol__: str = "mol"


class Candelas(BaseUnit):
    """Candelas"""

    __symbol__: str = "cd"
