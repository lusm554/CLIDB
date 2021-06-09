from pyfiglet import Figlet
from termcolor import cprint
import argparse
from dbmethods import *

#fonts: larry3d standard starwars
logo = Figlet(font='standard').renderText('CLI Database')
print(logo)

commands = {
  '1': {
    'info': 'Get item',
    'action': get
  },
  '2': {
    'info': 'Delete item',
    'action': delete
  },
  '3': {
    'info': 'Add item',
    'action': add
  },
  '4': {
    'info': 'Info about items',
    'action': info
  },
  '5': {
    'info': 'Change element in db',
    'action': put
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

