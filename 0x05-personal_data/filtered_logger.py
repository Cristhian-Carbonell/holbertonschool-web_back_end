#!/usr/bin/env python3
"""Regex-ing
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """[summary]
    """
    for index in fields:
        message = re.sub(index + "=.*?" + separator,
                         index + "=" + redaction + separator, message)
    return message
