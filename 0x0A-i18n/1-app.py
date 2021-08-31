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

    @babel.localeselector
    def get_locale():
        """get locale method
        """
        return request.accept_languages.best_match(app.config['LANGUAGES'])
