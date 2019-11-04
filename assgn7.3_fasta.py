#! /usr/bin/env python3

'''
## Name of program: assgn7.3_fasta.py
## Author: Chandra Sarkar
## Function: 
    Open the file regex.practice1.fasta for reading.
    Open a new file for writing.

    Read one line from regex.practice1.fasta at a time, and for each line:
        Grab the name row and read the numeric string at the beginning.
        Replace the name row with the words Homo_sapiens and their respective numeric string without spaces.
        Write the line (modified or unmodified) in a new file.
'''
import re   #importing the regex module

InFile = open("regex.practice1.fasta", 'r')     #opening the input file
OutFile = open("regex.practice1_modified.fasta", 'w')   #opening the new output file

for line in InFile:
    
    mod_line = line
    mod_line = re.sub(r"^>(\S+)(.+)",r">Homo_sapiens:\1", line)
    #print(mod_line) 

    OutFile.write(mod_line)

InFile.close()
OutFile.close()