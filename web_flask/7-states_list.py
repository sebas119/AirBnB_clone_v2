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


@app.route('/states_list', strict_slashes=False)
def display_html_n_type():
    """Display all states from SQLalchemy in html file"""
    all_states = storage.all('State')
    return render_template('7-states_list.html', states=all_states)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(host='0.0.0.0', port='5000')
