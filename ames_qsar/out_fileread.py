import os
import glob

def out_fileread(filepath):
    os.chdir(filepath)

    namelist = []
    #This could be adjusted later to locate other extentions
    for filename in glob.glob('*.out'):
        
        #removing the filepath leaves just the filename
        filename = filename.replace(str(filepath), '')
        namelist.append(filename)

    return namelist
