#!/usr/bin/env python3
"""Class Basic_auth"""
from api.v1.auth.auth import Auth


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
        for i in range(len(authorization_header)):
            if authorization_header[i] == " ":
                encode = authorization_header[i+1:-1]

        return encode
