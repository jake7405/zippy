#!python3

import hashlib
import os
import zlib, zipfile, bz2

__archive_types = ['zip', 'bz2', 'tar', 'gz', '7z', 'rar']

def compress(files: list, type, dir, name):
    if dir == '' or dir == None:
        dir = os.curdir
    if type not in __archive_types:
        pass
    else:
        if type == 'zip':
            with zipfile.ZipFile(name, 'w') as zipf:
                (zipf.write(f) for f in files)    
        elif type == 'bz2':
            with bz2.BZ2File(name, 'w') as zipf:
                (zipf.write(f) for f in files)  
        elif type == 'gz':
            pass
#TODO auto-append filetype if not present in name param            
compress(['test1.txt', 'test2.txt'], 'bz2', '', 'testzip.bz2')