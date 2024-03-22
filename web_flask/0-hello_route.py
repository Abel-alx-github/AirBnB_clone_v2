#!/usr/bin/python3
"""starts a flask web application """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def fromRoot():
    return f"Hello HBNB!"
