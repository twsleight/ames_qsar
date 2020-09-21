

#readtest.py checks that the file reading function selects the
#lowest line of test that matches the desired line. This lowest prevLine
#should be the final structure in the gaussian .out file.
#coumarin.out files are used for testing
import glob
namelist=[]

for filename in glob.glob('*.out'):
    print(filename)
    namelist.append(filename)
        with open(filename)as searchfile:
            pass
