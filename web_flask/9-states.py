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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def filter_state(id=None):
    """All cities by states or an specfic states with its cities"""

    states = storage.all('State')
    if id is not None:
        for state in states.values():
            if state.id == id:
                return render_template('9-states.html', state=state, id=id)
    return render_template('9-states.html', states=states, id=id)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(host='0.0.0.0', port='5000')
