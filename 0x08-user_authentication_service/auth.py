#!/usr/bin/env python3
"""auth module
"""
import bcrypt
import base64


def _hash_password(password: str):
    """returns bytes.
    """
    encoded = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encoded, salt)
