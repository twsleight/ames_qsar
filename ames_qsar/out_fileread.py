import os

def out_fileread(filepath):

    namelist = [i for i in os.listdir(filepath) if '.out' in i]

    return namelist
