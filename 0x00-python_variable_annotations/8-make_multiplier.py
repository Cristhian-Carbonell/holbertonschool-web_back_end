#!/usr/bin/env python3
"""Complex types - functions

a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies a
float by multiplier.

Functions:
    make_multiplier(multiplier: float) -> Callable[[float], float]:
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by multiplier.

        Parameters:
            multiplier (float): numbers float

        Returns:
            a function that multiplies a float by multiplier.
    """
    return lambda x: x * multiplier
