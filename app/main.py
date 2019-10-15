from flask import Flask, render_template
from os import environ
app = Flask(__name__)

mapboxToken = environ['MAPBOX_TOKEN']

@app.route('/')
def helloWorld():
  return render_template('map.html', token=mapboxToken)
