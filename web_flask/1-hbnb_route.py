#!/usr/bin/python3

"""Flask basic web app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start app flask"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB display"""
    return 'HBNB'


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(host='0.0.0.0', port='5000')
