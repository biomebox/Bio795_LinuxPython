#! /usr/bin/env python3

## Name of program: assgn5.4_animals.py
## Function: Creating a dictionary of animals (names as keys)
##          and their weights as corresponding values.
##          If the animal weighs more than 20gms, it prints big
##          or if the animal weighs less than 20 gms, it prints small
## Author: Chandra Sarkar
'''
Make a dictionary with the following information:
    {
    "dog" = 30000,
    "possum" = 2000,
    "cat" = 4500,
    "hummingbird" = 12
    "bat" = 18
    }

Print out only the keys of the dictionary.
Put all the names of the animals in a list.
For an animal in the list,
    Print the name of the animal
    If the animal weighs more than 20gms (refer to the value for the animal key)
        Print 'big'
    If the animal weighs less than 20 grams
        Print 'small'

'''        
### Writing a dictionary with animal names and their weights ###
animals = {"dog": 30000,
    "possum": 2000,
    "cat": 4500,
    "hummingbird": 12,
    "bat": 18
    }

### Printing the keys i.e. the animal names ###
print (animals.keys())

### Putting the names of the animals as a list ###
anim_list = list(animals.keys())
# print(anim_list)

### Looping through the animal names and checking whether the animals are big or small ###

for item in anim_list:
    if animals[item] > 20:
        print (item,"is big")
    elif animals[item] < 20:
        print (item,"is small")
