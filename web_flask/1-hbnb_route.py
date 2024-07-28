#!/usr/bin/python3

"""
Script that starts a Flask web application.
Our web application must be listening on 0.0.0.0, port 5000.
"""
from flask import Flask


# Create an instance of the Flask class.
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    handle requests to the root URL '/'.
    Returns a simple greeting message.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Handle requests to the '/hbnb' URL.
    Returns a different greeting message.
    """
    return "HBNB"


if __name__ == "__main__":
    # Run the Flask application on all available IP addresses and port 5000.
    app.run(host='0.0.0.0', port=5000)
