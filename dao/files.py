import os
import json
from datetime import datetime


def to_human_time(time):
    return str(datetime.fromtimestamp(time))


class FileDAO:
    def __init__(self, name, DIR):
        self.file = name
        self.DIR = DIR

    
    def __str__(self):
        print(self.DIR, self.file)
        data = ''
        files = os.listdir(self.DIR)
        for file in files:
            data += f'{file}\n'
            data += ' size: {} bytes\n'.format(os.path.getsize(self.file)) \
            + ' permission: {}\n'.format(oct(os.stat(self.file).st_mode)[-3:]) \
            + ' created: {}\n'.format(to_human_time(os.path.getctime(self.file))) \
            + ' modified: {}\n'.format(to_human_time(os.path.getmtime(self.file)))
        return data


    def add(self, data):
        with open(self.file, 'w') as outfile:
            json.dump(data, outfile)


    def get(self):
        with open(self.file) as json_file:
            return json.load(json_file)


    def put(self, data):
        old_data = ''
        current = {}
        with open(self.file) as json_file:
            old_data = json.load(json_file)
        for key in old_data.keys():
            if key in data:
                current[key] = data[key]
            else:
                current[key] = old_data[key]
        with open(self.file, 'w') as outfile:
            json.dump(current, outfile)


    def delete(self):
        os.remove(self.file)
