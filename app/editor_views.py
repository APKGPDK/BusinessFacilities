from mapbox import Geocoder
from requests import get
from os import environ
from flask import Blueprint, render_template, redirect, url_for, request
from facilities import add_facility, update_facility, get_facility, remove_facility, load_json
editor_app = Blueprint('editor', __name__)

# 
mapbox_token = environ['MAPBOX_TOKEN']
geocoder = Geocoder(access_token=mapbox_token)


@editor_app.route('/editor')
def show_editor():
  data = load_json()
  return render_template('facilities_list.html', facilities=data['facilities'])


@editor_app.route('/editor/add_facility', methods=['GET', 'POST'])
def create_facility():
  if request.method == 'POST':
    longitude = request.values.get('longitude', 0)
    latitude = request.values.get('latitude', 0)
    response = geocoder.reverse(lon=longitude, lat=latitude)
    address = response.geojson()['features'][0]['place_name']
    payload = {
      'title': request.values.get('title'),
      'description': request.values.get('description'),
      'latitude': float(latitude),
      'longitude': float(longitude),
      'address': address,
    }
    add_facility(payload)
    return redirect(url_for('editor.show_editor'))
  return render_template('facilities_form.html', token=mapbox_token)


@editor_app.route('/editor/update_facility_data/<id>', methods=['GET', 'PUT'])
def update_facility_data(id):
  if request.method == 'PUT':
    longitude = request.values.get('longitude', 0)
    latitude = request.values.get('latitude', 0)
    response = geocoder.reverse(lon=longitude, lat=latitude)
    address = response.geojson()['features'][0]['place_name']
    payload = {
      'id': id,
      'title': request.values.get('title'),
      'description': request.values.get('description'),
      'latitude': float(latitude),
      'longitude': float(longitude),
      'address': address,
    }
    update_facility(payload)
    return redirect(url_for('editor.show_editor'))

  payload = get_facility(id)
  return render_template('facilities_edit_form.html', payload=payload, token=mapbox_token)

@editor_app.route('/editor/delete_facility/<id>')
def delete_facility(id):
  remove_facility(id)
  return redirect(url_for('editor.show_editor'))
