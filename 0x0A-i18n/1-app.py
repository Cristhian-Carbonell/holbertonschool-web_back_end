#!/usr/bin/env python3
"""Basic Babel setup
"""
from flask_babel import Babel
from flask import request

app = __import__('0-app.py').app

babel = Babel(app)


class Config:
    """Config class
    """
    LANGUAGES = ["en", "fr"]

    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
