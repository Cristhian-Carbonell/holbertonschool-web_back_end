#!/usr/bin/env python3
from typing import NewType
"""Basic annotations

a type-annotated function floor which takes a float n
as argument and returns the floor of the float.

Functions:
    floor(n: float) -> float
"""


def floor(n: float) -> int:
    """
    Returns the floor of the int.

        Parameters:
            n (float): a number float

        Returns:
            the floor of the int.
    """
    number = int(n)
    if number >= 0:
        return number
    else:
        return int(number) - 1
