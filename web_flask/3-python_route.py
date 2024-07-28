#!/usr/bin/python3
"""
Script that starts a Flask web application:
Web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Handle requests to the root URL '/'.
    Returns a simple greeting message.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Handle requests to the '/hbnb' URL.
    Returns a different greeting message.
    """
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Handle text requests
    """
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    Handle text requests
    """
    return "Python " + text.replace("_", " ")


if __name__ == '__main__':
    # Run the Flask application on all available IP addresses and port 5000.
    app.run(host='0.0.0.0', port=5000)
