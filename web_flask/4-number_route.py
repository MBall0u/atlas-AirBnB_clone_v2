#!/usr/bin/python3
"""Start of Web Framework"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C {}".format(' '.join(text.split('_')))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is_cool"):
    return "Python {}".format(' '.join(text.split('_')))


@app.route("/number/<n>", strict_slashes=False)
def is_number(n):
    if type(n) is int:
        return "{} is a number".format(n)
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
