#!/usr/bin/python3
""" routes '/' and '/hbnb' """
from flask import Flask

myapp = Flask(__name__)


@myapp.route('/', strict_slashes=False)
def fromRoot():
    return f'Hello HBNB!'


@myapp.route('/hbnb', strict_slashes=False)
def from_root_hbnb():
    return f'HBNB'


@myapp.route('/c/<text>')
def route_c(text):
    if '_' in text:
        text = text.replace('_', ' ')
    return f'C {text}'


@myapp.route('/python', strict_slashes=False)
@myapp.route('/python/<text>', strict_slashes=False)
def route_python(text='is cool'):
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    myapp.run(host='0.0.0.0', port=5000)
