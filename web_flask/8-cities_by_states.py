#!/usr/bin/python3
""" start web application to serve html"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states')
def cities_by_states():
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.template_filter('get_cities')
def get_cities(state):
    """Filter to retrieve sorted cities of a state"""
    if hasattr(state, 'cities'):
        cities = sorted(state.cities, key=lambda city: city.name)
    else:
        cities = sorted(storage.all(City).values(), key=lambda city: city.name)
        cities = [city for city in cities if city.state_id == state.id]
    return cities


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
