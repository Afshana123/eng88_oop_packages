# What are Python Modules?

# We have built in Modules that we can find on Python's library

# if the value is 1.49 -> if you apply the floor() function then it will round up to 1, ceil() 2
# We have a keyword called import that we can use to call a module

# import random
# print(random.random())

# print a random number from random
# generates a random number everytime you run in
# Why are we using it? They use this for lottery

# #     file name     class
# from random import random
# print(random())


# import math
# num1 = 23.66
# print(num1)
# print(math.ceil(num1))
# # rounds up
#
# import math
# num1 = 23.66
# print(num1)
# print(math.floor(num1))
# # rounds down

# generate a number with radom
# apply if conditions
# if the user input is >= .50 apply ceil
# if the user input is <= .49 apply floor
# user should be asked to input data again if they enter a string

# random generates a number from 0 and 1

#check this later:

# from random import random
# import math
# generate_number = float(input("Please enter a number of your choice or press enter to generate a random number: "))
# num1 = generate_number
# if num1 >= 0.5:
#     print(math.ceil(num1))
# else:
#     print(math.floor(num1))



# from random import random
# import math

# random_number = random()
# print("This is randomly generated " + str(random_number))
# if random_number >= 0.5:
#     print(math.ceil(random_number))
# else:
#     print(math.floor(random_number))


# We have a package called os which is used to get information about your localhost/your machine such as name, path etc
# if you want to import more than one package, you can put a comma like the way we have done below

import os, sys

# working_dir = os.getcwd()
# print("This is your current working Dir " + working_dir)
#
# # prints current working directory
#
# system_path = sys.path
# print("This is the path " + str(system_path))

# you don't want to this all the time, so we can create a function

def current_system_path():
    print("This is your current path " )
    return sys.path
print(current_system_path())

def current_system_directory():
    print("This is your current working directory ")
    return os.getcwd()
print(current_system_directory())
