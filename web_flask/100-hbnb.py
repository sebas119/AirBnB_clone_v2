#!/usr/bin/python3

"""Flask basic web app"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exc):
    """Teardown db"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB front page with search bar and different places"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template(
        '100-hbnb.html',
        states=states,
        amenities=amenities,
        places=places
    )


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(host='0.0.0.0', port='5000')
