"""A module for SI units definition. See https://en.wikipedia.org/wiki/International_System_of_Units"""

from units_calculator.baseunit import BaseUnit


class Seconds(BaseUnit):
    __symbol__: str = "s"


class Meters(BaseUnit):
    __symbol__: str = "m"


class Kilograms(BaseUnit):
    __symbol__: str = "kg"


class Amperes(BaseUnit):
    __symbol__: str = "A"


class Kelvins(BaseUnit):
    __symbol__: str = "K"


class Mols(BaseUnit):
    __symbol__: str = "mol"


class Candelas(BaseUnit):
    __symbol__: str = "cd"
