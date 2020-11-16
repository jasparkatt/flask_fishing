from app import app
from flask import render_template
from app.settings import MAPBOX_ACCESS_TOKEN



@app.route('/key')
def key():
    access_token = MAPBOX_ACCESS_TOKEN
    data = {'center': [43.556667, -90.887778],'title': 'Testing Page'}   
    return render_template('public/key.html', access_token=access_token,data=data)

# route for map with some data displayed
@app.route('/map')
def mapPage():
    access_token = MAPBOX_ACCESS_TOKEN
    data = {'center': [44.41, -89.00]}
    return render_template('public/maps.html', access_token=access_token,data=data)


@app.route('/avalanche')

@app.route('/central')
def centralPage():
    access_token = MAPBOX_ACCESS_TOKEN
    data = {'center': [44.49016, -89.30744], 'title': 'Central Sands'}
    return render_template('public/map_base.html', access_token=access_token,data=data)


@app.route('/upperwis')
def upperwis():
    access_token = MAPBOX_ACCESS_TOKEN
    data = {'center': [46.555, -91.629], 'title': 'Lake Fish'}
    return render_template('public/map_base.html', access_token=access_token,data=data)    