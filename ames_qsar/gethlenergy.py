#gethlenergy will take a filepath and a file name
#and return the HOMO and LUMO energies.

#this will also need a test
import os

def gethlenergy(dir_path, filename):

    #initilalize the error codes as ok
    termFlag = 0
    errorFlag = 0
    a = 0
    b = 0
    #initialize a holding variable
    prevLine = []
    os.chdir(dir_path)

    with open(filename)as searchfile:

        #These fences indicate the where the loop ends
        #************************
        for line in searchfile:
            #error checking
            #the normal termination flag should turn to 1
            if 'Normal termination of Gaussian 09' in line:
                termFlag = 1
            if 'slurmstepd: error:' in line:
                errorFlag = 1
            #***************************************************************

            left,sep,right=line.partition('Alpha virt. eigenvalues --')

            if sep and 'Alpha  occ. eigenvalues --' in prevLine:

                b1 = (right[:56])
                b1 = b1. split()
                b = float(b1[0])

                left,sep,right=prevLine.partition('Alpha  occ. eigenvalues --')

                a1 = (right[:56])
                a1 = a1. split()
                a = float(a1[-1])

            prevLine2 = prevLine
            prevLine = line
        #*************************
        #end of the searchfile loop

        if termFlag == 1 and errorFlag == 0:
        #********************
            print(a, b)
        #********************
        else:
            print(filename, ' did not terminate correctly')

    return [a,b]
