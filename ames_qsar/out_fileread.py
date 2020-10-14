import os
import glob
def out_fileread(filepath):

    os.chdir(filepath)
    #filepath = '/home/twsleight/ames_qsar/tests'

    #print(filepath + '/*.out')
    namelist = []
    for filename in glob.glob('*.out'):

    #    print(filename)
        filename = filename.replace(filepath, '')
        namelist.append(filename)
        print(namelist)

    return namelist
