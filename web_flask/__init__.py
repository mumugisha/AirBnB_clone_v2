#!/usr/bin/python3

from flask import Flask

def create_app():
        app = Flask(__name__)

            @app.route('/', strict_slashes=False)
                def hello_hbnb():
                            return "Hello HBNB!"

                            return app

