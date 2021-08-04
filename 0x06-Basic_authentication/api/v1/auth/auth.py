#!/usr/bin/env python3
"""Module of class auth"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class Auth
    """
    def __init__(self):
        """method constructor"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method require_auth

        Returns:
            False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """public method authorization_header

        Returns:
            None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """public method current_user

        Returns:
            None
        """
        return None
