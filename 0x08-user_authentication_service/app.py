#!/usr/bin/env python3
"""basic Flask app
"""
from flask import Flask, jsonify, request, abort, make_response
from flask.globals import session
from auth import Auth
import requests


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """register a user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """login user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password) is False:
        abort(401)

    session = AUTH.create_session(email)
    response = make_response("")
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session)

    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Log out
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    destroy_session = AUTH.destroy_session(user.id)
    response = requests.get("http://10.42.0.181:5000/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
