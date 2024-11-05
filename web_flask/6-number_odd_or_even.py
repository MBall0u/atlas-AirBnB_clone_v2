#!/usr/bin/python3
"""Start of Web Framework"""
from flask import Flask, abort, render_template

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
    try:
        is_int = int(n)
        return "{} is a number".format(is_int)
    except ValueError:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    try:
        is_int = int(n)
        return render_template("5-number.html", num=n)
    except ValueError:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    try:
        is_int = int(n)
        odd_or_even = is_int % 2
        return render_template("6-number_odd_or_even.html", num=n, odd_or_even=odd_or_even)
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
