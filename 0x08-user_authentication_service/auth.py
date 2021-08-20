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
from typing import Union


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

    def create_session(self, email: str) -> str:
        """return the session ID.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return

        new_UUID = _generate_uuid()
        user.session_id = new_UUID
        self._db._session.commit()

        return str(user.session_id)

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """"returns the corresponding User or None
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user


def _generate_uuid() -> str:
    """return a string representation of a new UUID
    """
    return str(uuid.uuid4())
