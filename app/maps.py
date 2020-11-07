from app import app
from flask import render_template
from app.settings import secret_key, MAPBOX_ACCESS_TOKEN

@app.route('/key')
def key():
    return secret_key

# route for map with some data displayed
@app.route('/map')
def mapPage():
    access_token=app.config.get('MAPBOX_ACCESS_TOKEN')
    return render_template('public/maps.html', access_token=access_token)


@app.route('/avalanche')
def avalanchePage():
    return render_template('public/driftless.html')


@app.route('/central')
def centralPage():
    return render_template('public/centralsands.html')