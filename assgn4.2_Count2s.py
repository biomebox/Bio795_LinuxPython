#!/usr/bin/env python3

## Name of program: assgn4.2_Count2s.py
## Fucntion: Reads a number and counts the number of 2s in it.
## Author: Chandra Sarkar

### takes input of the number 112345678911234566 from user ###
num = input("Input the given number: ")

###converts into a string for using the in-built count function ###
num_convert = str(num)

### takes input of the number 2 from user ###
what_num = str(input("Input what number to count: "))

### uses the in-built count function and prints the results ###
count = num_convert.count(what_num) #stores in the count variable
print("The number of %ss in the number %s is: %d"%(what_num,num_convert,count)) #prints output

