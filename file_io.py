##############################################
# Wes Cratty
# Lab 2 – Functions, Classes, & File IO
# CSCI 232: Data Structures & Algorithms
# 9/6/13
#
# file_io.py
##############################################

from csv import reader
# Import the 'reader' class from the csv module.

def read(s):
    '''Input: a file, Output: list '''
    
    listScores={}#make dict
    file_location=s# assign perameter to variable
    
    try:
        myfile= open(file_location,mode="r",errors="?")# opens file in read mode marks errors
        myfile.readable
        myfile.readline()
        
    except (LookupError,FileNotFoundError)as error:
        print("LookupError or FileNotFoundError")
        
    parser = reader(myfile, delimiter='\t')# create a parser w/ delimiter tab
    
    for score, name in parser:
        
        listScores[int(score)]=str(name)# makes a new dict

    myfile.close()
    
    return listScores

def write(listIn,outPutLocation ="output.txt"):
    ''' recieves list and location to store a file'''
    
    my_file = open(outPutLocation, "w+")# open a file into
    
    writeList=listIn# assign a list
    my_file.writelines("\n")
    for item in writeList:# loop through list
        my_file.writelines(item + "\n")#cast list item to string and write to file
        my_file.flush()
        
    my_file.close()# close file
    
    


if __name__ == "__main__":
 
    
    (write(read("names.csv")))
 
