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
    data = {'center': [44.41, -89.00], 'title': 'Home Waters', 'zoom': 7}
    return render_template('public/map_base.html', access_token=access_token,data=data)

@app.route('/avalanche')
def driftless():
    access_token = MAPBOX_ACCESS_TOKEN
    data = {'center':[43.602222, -90.630278], 'title': 'The Driftless', 'zoom': 9}
    marks = [[43.41543,-90.54951], [43.59822,-90.78042]]
    return render_template('public/map_base.html', access_token=access_token,data=data,marks=marks)

@app.route('/central')
def centralPage():
    access_token = MAPBOX_ACCESS_TOKEN
    data = {'center': [44.1475, -89.181389], 'title': 'Central Sands', 'zoom': 10}
    return render_template('public/map_base.html', access_token=access_token,data=data)

@app.route('/upperwis')
def upperwis():
    access_token = MAPBOX_ACCESS_TOKEN
    data = {'center': [46.555, -91.629], 'title': 'Lake Fish', 'zoom': 11}
    return render_template('public/map_base.html', access_token=access_token,data=data)  

@app.route('/newis')
def newis():
    access_token = MAPBOX_ACCESS_TOKEN
    data = {'center': [44.883333, -87.866667], 'title': 'Lake Fish', 'zoom': 13}
    return render_template('public/map_base.html', access_token=access_token,data=data)     