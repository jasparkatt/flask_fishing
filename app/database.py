from app import app
import os
from flask import render_template
import psycopg2
from app.settings import *



con = psycopg2.connect(database=PG_NAME, user=PG_USER, password=PG_PASSWORD, host=PG_HOST, port=PG_PORT)
cursor = con.cursor()


# route for data entry to postgresql 'fishing' db tables
@app.route('/data', methods=['POST', 'GET'])
def dataPage():
    cursor.execute("select id, stream, county, species from all_spots order by county asc")
    result = cursor.fetchall()
    return render_template('public/dataPage.html', data=result)
