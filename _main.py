from pyfiglet import Figlet
from termcolor import cprint
import os
from dao.files import *

logo = Figlet(font='standard').renderText('CLI Database')
#print(logo)

class File:
    def __init__(self, file_name=False):
        self.file_name = file_name

    def __str__(self):
        return 'hello'

    def add(self):
        data = {
            'name': None,
            'age': None,
            'class': None
        }
        for key in data.keys():
            input_data = input('{}: '.format(key))
            if input_data == '':
                cprint('Value field cannot be empty.\n', 'red', attrs=['underline'])
                return
            data[key] = input_data
        add(self.file_name, data)
        cprint('\nFile {0} writen\n'.format(self.file_name), 'green', attrs=['underline'])

    def get(self):
        pass

    def getAll(self):
        pass

    def delete(self):
        pass

a = File(input('file? ')).add()

print(a)

