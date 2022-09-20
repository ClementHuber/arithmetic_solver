#!/usr/bin/python3
# =============================================================================
#
#   Arithmetic Solver
#
#   Copyright (c) Clement HUBER
#
#   MIT License
#
# =============================================================================

# IMPORTS =====================================================================

import re
from setuptools import setup
from pathlib import Path


# FUNCTIONS ===================================================================


def read(fname):
    path = Path(__file__).resolve().parent / fname
    return path.open(encoding="utf-8", errors="replace").read()


def get_dependencies():
    requirements = Path(__file__).resolve().parent / "requirements.txt"
    with requirements.open() as fh:
        requirements = fh.readlines()
        return list(
            map(
                lambda x: re.search("([^>=<~]*)[>=<~]", x).group(1),
                map(str.strip, requirements),
            )
        )


setup(
    name="arithmetic_solver",
    version="1.0.0",
    description=[
        "Solver of the arithmetic game 'Le Compte est bon' in the French TV game show 'Des Chiffres et des Lettres'"],
    long_description=read("README.md"),
    url="https://github.com/ClementHuber/arithmetic_solver",
    entry_points={"console_scripts":
                  "arithmetic_solver=arithmetic_solver.__main__:main"},
    author="Clement HUBER",
    author_email="clement.victor.huber@gmail.com",
    license="MIT",
    python_requires=">=3.8",
    packages=["arithmetic_solver"],
    install_requires=get_dependencies(),
    zip_safe=False,
    include_package_data=True,
)
