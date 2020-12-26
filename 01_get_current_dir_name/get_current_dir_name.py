#!/usr/bin/python

import os

def GetCurrentFolderName():
    print(os.name)
    dir_now = os.getcwd()
    os.chdir('..')
    dir_upper = os.getcwd()
    os.chdir(dir_now)
    if dir_upper == dir_now:
        # this is a root directory
        return dir_now
    else:
        if 'posix' == os.name:
            return dir_now.replace(dir_upper, '').replace('/', '')
        else:
            # maybe 'nt' which stands for Windows
            return dir_now.replace(dir_upper, '').replace('\\', '')

# some test
print(GetCurrentFolderName())

