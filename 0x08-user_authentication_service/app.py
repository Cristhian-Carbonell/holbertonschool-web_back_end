#!/usr/bin/env python3
"""basic Flask app
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return jsonify({"message": "Bienvenue"})
