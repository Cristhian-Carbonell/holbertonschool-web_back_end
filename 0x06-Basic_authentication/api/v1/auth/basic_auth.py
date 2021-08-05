#!/usr/bin/env python3
"""Class Basic_auth"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple


class BasicAuth(Auth):
    """class Basic auth"""
    pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header for a Basic"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        encoded = authorization_header.split(' ', 1)[1]

        return encoded

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = base64.b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None

        return decoded

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> (str, str):
        """returns the user email and password from the Base64 decoded
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        decoded = decoded_base64_authorization_header.split(":")
        email = decoded[0]
        password = decoded[1]
        return email, password
