from app import app
from flask import render_template
import psycopg2
from app.settings import *

con = psycopg2.connect(database=PG_NAME, user=PG_USER, password=PG_PASSWORD, host=PG_HOST, port=PG_PORT)
cursor = con.cursor()


# route for map with some data displayed
@app.route('/map')
def mapPage():
    access_token = MAPBOX_ACCESS_TOKEN
    data = {'center': [44.41, -89.00], 'title': 'Home Waters', 'zoom': 7}
    return render_template('public/map_base.html', access_token=access_token,data=data)

@app.route('/avalanche')
def driftless():
    access_token = MAPBOX_ACCESS_TOKEN
    geo_json = []
    data = {'center':[43.602222, -90.630278], 'title': 'The Driftless', 'zoom': 9}
    marks = [[43.41543,-90.54951], [43.59822,-90.78042]]
    return render_template('public/map_base.html', access_token=access_token,data=data,marks=marks,geo_json=geo_json)

@app.route('/central')
def centralPage():
    access_token = MAPBOX_ACCESS_TOKEN
    geo_json = []
    data = {'center': [44.1475, -89.181389], 'title': 'Central Sands', 'zoom': 10}
    return render_template('public/map_base.html', access_token=access_token,data=data,geo_json=geo_json)

@app.route('/upperwis')
def upperwis():
    access_token = MAPBOX_ACCESS_TOKEN
    geo_json = []
    data = {'center': [46.555, -91.629], 'title': 'Lake Fish', 'zoom': 11}
    return render_template('public/map_base.html', access_token=access_token,data=data,geo_json=geo_json)  

@app.route('/newis')
def newis():
    access_token = MAPBOX_ACCESS_TOKEN
    geo_json = []
    data = {'center': [44.883333, -87.866667], 'title': 'Lake Fish', 'zoom': 13}
    return render_template('public/map_base.html', access_token=access_token,data=data,geo_json=geo_json)

@app.route('/key')
def key():
    access_token = MAPBOX_ACCESS_TOKEN
    data = {'center': [44.883333, -89.866667], 'title': 'All Spots', 'zoom': 7}
    marks = []
    cursor.execute("select row_to_json(fc) from (select 'FeatureCollection' as type, array_to_json(array_agg(f)) as features from (select 'Feature' as type, ST_AsGeoJSON(lg.geom)::json as geometry,(select row_to_json(t) from (select id, stream, county, species) t) as properties from all_spots as lg) as f) as fc;")
    varcons = cursor.fetchall()
    geo_json=[]
    for varcon in varcons:
        geo_json.append(varcon[0])
    return render_template('public/map_base.html', geo_json=geo_json,access_token=access_token,data=data,marks=marks)