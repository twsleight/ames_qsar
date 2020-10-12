import os
import glob

def out_fileread(filepath):
    os.chdir(filepath)
    namelist = []
    for filename in glob.glob('*.out'):

        filename = filename.replace(filepath, '')
        namelist.append(filename)

    return namelist
