#! /usr/bin/env python3

## Name of program: assgn5.3_ListOfNos.py
## Function: Creating a list of numbers and looping through the list adding 1 to every number.
##              Then adding the new numbers to another list.
## Author: Chandra Sarkar

### create a list with some numbers ###
number_list = list(range(0, 19, 2)) #adds numbers from 0 to 19 with an increment of 2

### creating an empty list ###
number_list_new = []

### looping through the list of numbers and adding 1 to them ###
for item in number_list:

    print("\nThe number is: ",item)
    item += 1
    print("Adding 1 to the number: ",item)
    number_list_new.append(item)

print ("\n\nThe old list is: ", number_list)    #printing the original list
print("The new list is: ",number_list_new)      #printing the newly created list
    
