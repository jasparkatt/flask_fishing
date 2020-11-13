from os import environ

SECRET_KEY = environ.get('SECRET_KEY')
MAPBOX_ACCESS_TOKEN = environ.get('MAPBOX_ACCESS_TOKEN')

PG_HOST = environ.get('POSTGRES_HOST')
PG_NAME = environ.get('POSTGRES_NAME')
PG_USER = environ.get('POSTGRES_USER')
PG_PORT = environ.get('POSTGRES_PORT')
PG_PASSWORD = environ.get('POSTGRES_PASSWORD')


