from setuptools import setup
from typing import List
from pyrestsdk import __version__, __module_name__
import os


def get_requirements() -> List[str]:
    with open("./requirements.txt") as file:
        return [requirement.strip() for requirement in file.read().split("\n")]


def get_packages(directory: str) -> List[str]:
    return [
        x[0].replace("\\", ".") for x in os.walk(directory) if "__pycache__" not in x[0]
    ]


setup(
    name=__module_name__,
    version=__version__,
    author="michaeldcanady",
    description=("base set to make a REST Api wrapper/sdk"),
    license="MIT",
    packages=get_packages(os.path.join(".", "pyrestsdk")),
    install_requires=get_requirements(),
)
