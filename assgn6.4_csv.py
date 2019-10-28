#! /usr/bin/env python3

'''
## Name of program: assgn6.4_csv.py
## Author: Chandra Sarkar
## Function: 
        Open the file Bloom et al.
        Read and ignore the first line (header line).
            Read rest of the lines, and for each line:
            Break the line into a list with each value as a list object.
            Print the taxon name (first object in the list) and their diadromous state (the last object in the list).
            Add the float values of log body size to obtain a total value for all organisms (initiate the variable outside the loop).
            Count the no. of diadromous states and non-diadromous states.
        Print the sum of the logbody sizes for all the organisms.
'''

InFile = open("Bloom_etal_2018_Reduced_Dataset.csv",'r')    #assigning the input file to the variable InFile


logbody_sum = 0.0   #initializing variable to calculate sum for the logbody sizes                  
diadromous = non_diadromous = 0 #initializing counts for two diadromous states    

header_line = InFile.readline() #reading and storing the header line of the file if needed

#starting a loop to read through each line of the file and do certain operations
for line in InFile:                 
    line = line.strip("\n")         #strip unwanted endline characters
    line_list = line.split(",")     #splitting line by comma into a list

    #printing the first and last items on the list for taxa and diadromous state information
    print("taxa:%s\tdiadromous status:%s"%(line_list[0], line_list[-1]))    

    #coverting the list item of logbody to float value for calculation and summing them together
    logbody = float(line_list[1])
    logbody_sum = logbody_sum + logbody

    #counting the number of diadromous and non-diadromous organisms in the file
    if line_list[-1] == "diadromous":
        diadromous += 1
    elif line_list[-1] == "non-diadromous":
        non_diadromous += 1


#at the end if the loop
#printing the sum of all logbody sizes
print("\nThe sum of all the logbody sizes:%.2f"%logbody_sum)
#printing the counts of diadromous and non-diadromous organisms    
print("\nNo. of diadromous:%d\tNo. of non-diadromous:%d"%(diadromous, non_diadromous))  

