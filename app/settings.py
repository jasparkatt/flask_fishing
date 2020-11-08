from os import environ

SECRET_KEY = environ.get('SECRET_KEY')
MAPBOX_ACCESS_TOKEN = environ.get('MAPBOX_ACCESS_TOKEN')