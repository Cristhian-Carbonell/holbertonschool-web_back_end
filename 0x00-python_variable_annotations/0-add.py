#!/usr/bin/env python3
"""Basic annotations.

a type-annotated function add that takes a float a and a float b
as arguments and returns their sum as a float.

Functions:

    add(a: float, b: float) -> float
"""


def add(a: float, b: float) -> float:
    """
    Returns their sum as a float.

        Parameters:
            a (float): a number float
            b (float): another number float

        Returns:
            float_sum (float): number float of the sum of a and b
    """
    float_sum = a + b
    return float_sum
