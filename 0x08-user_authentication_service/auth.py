#!/usr/bin/env python3
"""auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from flask import request
import uuid


def _hash_password(password: str) -> bytes:
    """returns bytes.
    """
    encoded = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encoded, salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """return a User
        """
        try:
            find_user = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            user = self._db.add_user(email, password)

        return user

    def valid_login(self, email: str, password: str) -> bool:
        """valid login
        """
        encoded = password.encode('utf-8')
        try:
            find_user = self._db.find_user_by(email=email)
            check_password = _hash_password(find_user.hashed_password)
            if bcrypt.checkpw(encoded, check_password):
                return True
        except NoResultFound:
            return False

        return False


def _generate_uuid(self) -> str:
    """return a string representation of a new UUID
    """
    return str(uuid.uuid4())
