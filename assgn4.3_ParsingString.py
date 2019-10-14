#!/usr/bin/env python3

## Name of program: assgn4.3_ParsingString.py
## Fucntion: Reads a sentence/string from user and turns all letters to lowercase,
##              removes spaces, counts and prints out the length of the string
## Author: Chandra Sarkar

### takes string input from user ###
sentence = str(input("Input a sentence: "))

### turn sentence into lowercase and print it ###
sentence_lowercase = sentence.lower()
print ("\nThe sentence in all lower case is:\t", sentence_lowercase)

### remove spaces ###
sentence_no_space = sentence.replace(" ","")
print ("\nThe sentence with no space:\t", sentence_no_space)

### counts no. of characters of the sentence and prints out ###
sentence_length = len(sentence)     #length of sentence without spaces i.e. original input length
print ("\nThe length of the original sentence:\t",sentence_length)

sentence_length_nospace = len(sentence_no_space)
print ("\nThe length of the sentence without spaces:\t",sentence_length_nospace)