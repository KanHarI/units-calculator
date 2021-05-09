"""Package setup file"""

from setuptools import find_packages, setup  # type: ignore

__version__ = "1.0.0"

packages = find_packages(exclude=["tests"])

setup(
    name="UnitsCalculator",
    version=__version__,
    package_data={package: ["py.typed"] for package in packages},
    packages=find_packages(),
    install_requires=["ordered-set"],
)
