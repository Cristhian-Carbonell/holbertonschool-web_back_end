#!/usr/bin/env python3
"""Basic annotations

a type-annotated function concat that takes a string str1 and a string str2 as
arguments and returns a concatenated string

Functions:
    concat(str1: str, str2: str) -> str
"""


def concat(str1: str, str2: str) -> str:
    """
    returns a concatenated string

        Parameters:
            str1 (str): a string
            str2 (str): another string

        Returns:
            A concatenated string
    """
    return str1 + str2
