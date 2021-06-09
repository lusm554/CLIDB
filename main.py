from pyfiglet import Figlet
from termcolor import cprint
import os
from dao.files import *

#fonts: larry3d standard starwars
logo = Figlet(font='standard').renderText('CLI Database')
print(logo)

# Create dir for files if not exist
try:
  if not os.path.exists('var'):
    os.makedirs('var')
except OSError as e:
  if e.errno != errno.EEXIST:
    raise

def add_file():
  file_name = input('File name: ')
  if file_name == '': return cprint('Value field cannot be empty.\n', 'red', attrs=['underline'])
  data = {
    'name': None,
    'age': None,
    'class': None
  }
  for key in data.keys():
    input_data = input('{0}: '.format(key))
    if input_data == '':
      cprint('Value field cannot be empty.\n', 'red', attrs=['underline'])
      return
    data[key] = input_data
  add(file_name, data)
  cprint('\nFile {0} writen\n'.format(file_name), 'green', attrs=['underline'])

def get_file():
  file_name = input('File name: ')
  if not os.path.exists(os.path.join('var', file_name)):
    return cprint('File not found.\n', 'red', attrs=['underline'])
  print()
  data = get(file_name)
  for key in data.keys():
    print('{0}: {1}'.format(key, data[key]))
  print()

def info_files():
  files = info()
  for file in files.keys():
    print('{0}'.format(file))
    for info_key in files[file].keys():
      print('  {0}: {1}'.format(info_key, files[file][info_key]))
  print()

def delete_files():
  file_name = input('File name: ')
  if not os.path.exists(os.path.join('var', file_name)):
    return cprint('File not found.\n', 'red', attrs=['underline'])
  delete(file_name)
  cprint('File deleted.', 'green')

def change_file():
  file_name = input('File name: ')
  current = {}
  if not os.path.exists(os.path.join('var', file_name)):
    return cprint('File not found.\n', 'red', attrs=['underline'])
  print()
  data = get(file_name)
  for key in data.keys():
    print('{0}: {1}'.format(key, data[key]))
  key = input('Which key you want change? ')
  if not key in data:
    return cprint('Key does not exist.', 'red')
  current[key] = input('Value for {0}: '.format(key))
  put(file_name, current)
  cprint('File successul changed.', 'green')

commands = {
  '1': {
    'info': 'Get item',
    'action': get_file
  },
  '2': {
    'info': 'Delete item',
    'action': delete_files
  },
  '3': {
    'info': 'Add item',
    'action': add_file
  },
  '4': {
    'info': 'Info about items',
    'action': info_files
  },
  '5': {
    'info': 'Change element in db',
    'action': change_file
  },
  '6': {
    'info': 'Exit',
    'action': lambda code=0: cprint('Bye, have a nice day!', 'green') or exit(code)
  } 
}

def log_cmd():
  info = ''
  for (k, v) in commands.items():
    info += '{0}. {1}\n'.format(k, v['info']) 
  print(info)
  
while 1:   
  log_cmd()
  cmd = input('cmd? ')
  if cmd not in commands:
    cprint('Command \'{0}\' not found.\n'.format(cmd), 'red', attrs=['underline'])
    continue
  commands[cmd]['action']() 
  print('-'*50)

