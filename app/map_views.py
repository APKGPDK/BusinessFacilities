from flask import Blueprint, render_template
from os import environ
from facilities import load_json
map_app = Blueprint('map', __name__)

mapboxToken = environ['MAPBOX_TOKEN']

@map_app.route('/')
def home():
  return render_template('map.html', token=mapboxToken)

@map_app.route('/data')
def map_data():
  return load_json()