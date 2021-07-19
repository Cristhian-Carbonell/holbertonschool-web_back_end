#!/usr/bin/env python3
"""Complex types - list of floats

a type-annotated function sum_list which takes a list input_list of floats
as argument and returns their sum as a float.

Fuctions:
    sum_list(inpu_list: list[float]) -> float
"""


def sum_list(input_list: list[float]) -> float:
    """
    returns their sum as a float.

        Parameters:
            input_list (list[float]): numbers float

        Returns:
            their sum as a float.
    """
    return sum(input_list)
