import os, json
from uuid import uuid4

facilities_path = '/usr/src/data/facilities.json'

def load_json():
  if os.path.isfile(facilities_path) and os.path.getsize(facilities_path) > 0:
    with open(facilities_path, 'r') as file:
      return json.load(file)
  return json.loads('{"facilities":[]}')

def save_json(datastore):
  with open(facilities_path, 'w+') as file:
    json.dump(datastore, file)
    file.close()

def add_facility(payload):
  datastore = load_json()
  datastore['facilities'].append({
    'id': str(uuid4()),
    'title': payload['title'],
    'description': payload['description'],
    'latitude': payload['latitude'],
    'longitude': payload['longitude'],
    'address': payload['address']
  })
  save_json(datastore)

def remove_facility(id):
  datastore = load_json()
  facility = next(f for f in datastore['facilities'] if f['id'] == id)
  datastore['facilities'].remove(facility)
  save_json(datastore)
