from setuptools import setup
from typing import List
from pyrestsdk import __version__, __module_name__
import os


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
    install_requires=[
        "black==22.12.0",
        "certifi==2022.12.7",
        "charset-normalizer==2.1.1",
        "click==8.1.3",
        "colorama==0.4.6",
        "idna==3.4",
        "mypy-extensions==0.4.3",
        "pathspec==0.10.3",
        "platformdirs==2.6.0",
        "requests==2.28.1",
        "urllib3==1.26.13"
    ],
)
