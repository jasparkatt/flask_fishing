from app import app
from flask import render_template
from app.settings import MAPBOX_ACCESS_TOKEN

@app.route('/key')
def key():
    return secret_key

# route for map with some data displayed
@app.route('/map')
def mapPage():
    access_token = MAPBOX_ACCESS_TOKEN
    return render_template('public/maps.html', access_token=access_token)


@app.route('/avalanche')
def avalanchePage():
    access_token = MAPBOX_ACCESS_TOKEN
    return render_template('public/driftless.html', access_token=access_token)


@app.route('/central')
def centralPage():
    access_token = MAPBOX_ACCESS_TOKEN
    return render_template('public/centralsands.html', access_token=access_token)


@app.route('/upperwis')
def upperwis():
    access_token = MAPBOX_ACCESS_TOKEN
    return render_template('public/upperwis.html', access_token=access_token)    