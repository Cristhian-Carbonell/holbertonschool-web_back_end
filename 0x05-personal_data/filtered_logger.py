#!/usr/bin/env python3
"""Regex-ing

Functions:
    filter_datum(list(str), str, str, str) -> str:
"""
from typing import List, Pattern
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated
    """
    for index in fields:
        message = re.sub(index + "=.*?" + separator,
                         index + "=" + redaction + separator, message)
    return message
