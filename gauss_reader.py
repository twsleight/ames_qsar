
#gauss_reader reads in a .out file from gaussian 09 and extracts
#data as desired for further analysis. A pandas dataframe should be generated
#which can be easily written off to an excel file

#author Trevor Sleight: twsleight@gmail.# COMBAK:
#Initially drafted Summer 2020


import os
import pandas as pd
import glob
#need to show lots of precision because we're working in Hartrees
pd.set_option('precision', 7)


cwd = os.getcwd()
print(cwd)
namelist=[]
prevLine = []

allData = pd.DataFrame(columns = ['SMILES',  'TA98', 'filename'])

#this is a reference file that provides the truth data that will be used for
#training algorithms later.
ta98 = pd.read_excel(cwd +r"//newta98.xlsx", sheet_name = 'Sheet1')


for filename in glob.glob('*gas.out'):
    print(filename)
    namelist.append(filename)
    termFlag = 0 # make sure the file terminated normally
    errorFlag = 0 # make sure that there are no errors
    with open(filename)as searchfile:
        #************************
        #initialized with error codes
        p = 'not found'
        c = 'not found'
        t = 'not found'

        for line in searchfile:
            #error checking
            if 'Normal termination of Gaussian 09' in line:
                termFlag = 1
            if 'slurmstepd: error:' in line:
                errorFlag = 1
            #***************************************************************
            #Get the smiles code that we have in the top of every input card
            left,sep,right=line.partition('Symbolic Z-matrix:')

            if sep:
#                print(sep)
#                print(prevLine)
                parsedLine = prevLine2. split()
                for p in parsedLine:
                    #restricting the smiles code to just this limits the
                    #dataset to hydrocarbons
                    if set(p).issubset('CcOo=()-123456789\/') and ('c' or 'C') in set(p):
#                        print(p)
                        curSmiles = p

            prevLine2 = prevLine
            prevLine = line
        #end of the searchfile loop
        #add the filename data, and the TA98 data

        if termFlag == 1 and errorFlag == 0:
        #********************
            if len(ta98.loc[ta98['SMILES'] == p]['result']) == 1:
                ta98Result = int(ta98.loc[ta98['SMILES'] == p]['result'])
            else:
                ta98Result = 'error'

            saveName = filename.split('_')
            tempSlice = pd.DataFrame(data = {'SMILES':[p],'TA98': ta98Result, 'filename': saveName[0] })
            allData = allData.append(tempSlice)

        #********************
        else:
            print(filename, ' did not terminate correctly')

#clean up and drop duplicate smiles codes
allData.drop_duplicates(subset='SMILES', keep="first", inplace = True)
print(allData.to_string())
