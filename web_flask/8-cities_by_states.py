#!/usr/bin/python3
"""Start a Flask web application"""


from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)
from models.state import State


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
