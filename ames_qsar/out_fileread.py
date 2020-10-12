def out_fileread(filepath):
    import os
    os.chdir(filepath)
    #filepath = '/home/twsleight/ames_qsar/tests'
    import glob
    #print(filepath + '/*.out')
    namelist = []
    for filename in glob.glob('*.out'):

    #    print(filename)
        filename = filename.replace(filepath, '')
        namelist.append(filename)
        print(namelist)

    return namelist
