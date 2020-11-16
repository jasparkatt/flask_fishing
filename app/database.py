from app import app
import os
from flask import render_template
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
    return render_template('public/data_fav_cnty.html', data=data, results=results)    

