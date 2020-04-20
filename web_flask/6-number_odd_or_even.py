#!/usr/bin/python3

"""Flask basic web app"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start app flask"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB display"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    """Print params variables"""
    rep_text = text.replace("_", " ")
    return 'C %s' % rep_text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_iscool(text='is_cool'):
    """Display python is cool by default"""
    rep_text = text.replace("_", " ")
    return 'Python %s' % rep_text


@app.route('/number/<int:n>', strict_slashes=False)
def only_number(n):
    """Display only if n is integer"""
    if type(n) == int:
        return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html_n(n):
    """Display only if n is integer"""
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_html_n_type(n):
    """Display only if n is integer"""
    if type(n) == int:
        math_type = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html',
                               n=n,
                               math_type=math_type)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(host='0.0.0.0', port='5000')
