#!/usr/bin/env python3
"""Module of session_id views
"""
from api.v1.views import app_views
from flask import request, jsonify
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_id():
    """ POST /api/v1/auth_session/login
    Return:
      - loggin user id
    """
    from api.v1.app import auth
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    foundUsers = User.search({'email': email})
    if not foundUsers:
        return jsonify({"error": "no user found for this email"}), 404

    for user in foundUsers:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrog password"}), 401

    session_id = auth.create_session(user.id)
    SESSION_NAME = getenv("SESSION_NAME")
    response = jsonify(user.to_json())
    response.set_cookie(SESSION_NAME, session_id)

    return response
