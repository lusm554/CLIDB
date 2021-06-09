import os
import json
from datetime import datetime

# Utils
def path(filename):
  return os.path.join('var', filename)

def to_human_time(time):
  return str(datetime.fromtimestamp(time))

# CRUD functions
def add(file, data):
  with open(path(file), 'w') as outfile:
    json.dump(data, outfile)

def delete(filename):
  os.remove(path(filename))

def put(filename, new_data):
  old_data = ''
  current = {}
  with open(path(filename)) as json_file:
    old_data = json.load(json_file)
  for key in old_data.keys():
    if key in new_data:
      current[key] = new_data[key]
    else:
      current[key] = old_data[key]
  with open(path(filename), 'w') as outfile:
    json.dump(current, outfile)

def get(filename):
  with open(path(filename)) as json_file:
    data = json.load(json_file)
    return data

def info():
  data = {}
  files = os.listdir('var')
  for file in files:
    data[file] = {
      'size': '{0} bytes'.format(os.path.getsize(path(file))),
      'permission': oct(os.stat(path(file)).st_mode)[-3:],
      'created:': to_human_time(os.path.getctime(path(file))),
      'modified': to_human_time(os.path.getmtime(path(file)))
    }
  return data
