from pyfiglet import Figlet
from termcolor import cprint
import os
#from dao.files import add, delete, put, get, info
from dao.files import FileDAO

FILES_DIR = 'var'
logo = Figlet(font='standard').renderText('CLI Database')
#print(logo)

class File:
    def __init__(self, name, fdir=FILES_DIR):
        try:
            if not os.path.exists(fdir):
                os.makedirs(fdir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        self.name = name
        self.fdir = fdir
        self.dir = os.path.join(fdir, name)

    
    def __str__(self):
        return str(FileDAO(self.dir, self.fdir))
       

    def add(self, data):
        FileDAO(self.dir, self.fdir).add(data)
        return 'File added.'
    

    def get(self):
        data = FileDAO(self.dir, self.fdir).get()
        return data
    
    
    def put(self, data):
        FileDAO(self.dir, self.fdir).put(data)
        return 'File updated.'

    def delete(self):
        FileDAO(self.dir, self.fdir).delete()
        return 'File deleted.'

