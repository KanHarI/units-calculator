"""Package setup file"""

import pathlib

from setuptools import find_packages, setup  # type: ignore

__version__ = "1.0.2"

packages = find_packages(exclude=["tests"])

HERE = pathlib.Path(__file__).parent
README_CONTENT = (HERE / "README.md").read_text()

setup(
    name="units-calculator",
    version=__version__,
    description="A units calculator for dimensional analysis,"
    " optimized for comfort over performance",
    long_description=README_CONTENT,
    long_description_content_type="text/markdown",
    url="https://github.com/KanHarI/units-calculator",
    author="Itay KanHar",
    author_email="knaan.harpaz@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    package_data={package: ["py.typed"] for package in packages},
    packages=find_packages(),
    install_requires=["ordered-set"],
)
