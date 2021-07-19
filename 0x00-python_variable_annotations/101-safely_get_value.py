#!/usr/bin/env python3
"""More involved type annotations

Given the parameters and the return values, add type annotations
to the function
Hint: look into TypeVar

Functions:
    def safely_get_value(dct, key, default = None):
        if key in dct:
            return dct[key]
        else:
            return default
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any, default: Union[T, None]) -> Union[Any, T]:
    """
    returns dct[key] or default

        Parameters:
            dct (Mapping):
            key (Any):
            default (Union[T, None]):

        Returns:
            dct[key] or default
    """
    if key in dct:
        return dct[key]
    else:
        return default
