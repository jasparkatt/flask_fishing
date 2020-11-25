import os
from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_pyfile('settings.py')


from app import views
from app import admin_views
from app import database
from app import maps

