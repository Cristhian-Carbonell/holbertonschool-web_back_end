#!/usr/bin/env python3
"""Regex-ing

Functions:
    filter_datum(list(str), str, str, str) -> str:
"""
from typing import List, Pattern
import re
import logging
import os
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated
    """
    for index in fields:
        message = re.sub(index + "=.*?" + separator,
                         index + "=" + redaction + separator, message)
    return message


def get_logger() -> logging.Logger:
    """returns a logging.Logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    c_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    c_handler.setFormatter(formatter)
    logger.addHandler(c_handler)

    return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    """[summary]

    Returns:
        [type]: [description]
    """
    connectionDB = mysql.connector.connection.MySQLConnection(
        user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password = os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database = os.getenv('PERSONAL_DATA_DB_NAME'))

    return connectionDB


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor Method

        Args:
            fields (List[str]): accept a list of strings
            fields constructor argument
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """format method

        filter values in incoming log records using filter_datum.

        Args:
            record (logging.LogRecord):

        Returns:
            str:
        """
        NotImplementedError
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)
