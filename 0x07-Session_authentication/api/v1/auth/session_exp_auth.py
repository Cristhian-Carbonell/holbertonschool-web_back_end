#!/usr/bin/env python3
"""Module of  expiration date to a Session ID.
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """class SessionAuth
    """
    def __init__(self):
        """constructor method
        """
        self.session_duration = int(getenv("SESSION_DURATION"))
        if self.session_duration == None or not \
                isinstance(self.session_duration, int):
            self.session_duration = 0

    def create_session(self, user_id=None):
        """create session method
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_dictionary = self.user_id_by_session_id[session_id]
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user id for session id method
        """
        if session_id is None:
            return None
        if "session_id" not in self.user_id_by_session_id:
            return None
        if self.session_duration == 0:
            return self.session_dictionary[session_id]["user_id"]
        if "created_at" not in self.session_dictionary:
            return None
        if timedelta(self.created_at, self.session_duration) < datetime.now():
            return None

        return self.session_dictionary[session_id]["user_id"]
