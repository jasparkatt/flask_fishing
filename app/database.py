from app import app
import os
import json
from app.settings import MAPBOX_ACCESS_TOKEN
from flask import render_template, jsonify
import psycopg2
from app.settings import *

con = psycopg2.connect(database=PG_NAME, user=PG_USER, password=PG_PASSWORD, host=PG_HOST, port=PG_PORT)
cursor = con.cursor()



# route for data entry to postgresql 'fishing' db tables
@app.route('/all_spots', methods=['POST', 'GET'])
def dataPage():
    cursor.execute("select id, stream, county, species from all_spots order by county asc")
    results = cursor.fetchall()
    data = {'center': [],'title': 'All Spots, All Species'}
    return render_template('public/data_all.html', data=data, results=results)


@app.route('/fav_cnty', methods=['POST','GET'])
def favcounty():
    cursor.execute("select * from visited_county where visited_county.total > 0;")
    results = cursor.fetchall()
    data = {'center': [],'title': 'Most Visited Counties'}
    return render_template('public/data_fav.html', data=data, results=results)  


@app.route('/fav_wtrshd', methods=['POST','GET'])
def fav_wtrshd():
    cursor.execute("select * from fav_wtrshd where fav_wtrshd.total > 0;")  
    results = cursor.fetchone()
    data = {'center': [],'title': 'Most Visited Watersheds'}
    return render_template('public/data_fav.html', data=data, results=results )



@app.route('/key')
def key():
    access_token = MAPBOX_ACCESS_TOKEN
    cursor.execute("select row_to_json(fc) from (select 'FeatureCollection' as type, array_to_json(array_agg(f)) as features from (select 'Feature' as type, ST_AsGeoJSON(lg.geom)::json as geometry,(select row_to_json(t) from (select id, stream, county, species) t) as properties from all_spots as lg) as f) as fc;")
    varcons = cursor.fetchall()
    geo_json=[] 
    for varcon in varcons:
        geo_json.append(varcon[0])
    return render_template('public/key.html', geo_json=geo_json)

   
   