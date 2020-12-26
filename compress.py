#!python3

import hashlib
import os
import zlib, gzip, zipfile, bz2

__archive_types = ['zip', 'bz2', 'tar', 'gz', '7z', 'rar']

def compress(files, type, dir, name):
    if dir == '' or dir == None:
        dir = os.curdir
    

    
