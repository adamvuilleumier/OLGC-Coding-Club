# A function takes inputs / arguments and returns outputs

# We use functions to make a high-level contract of what is to be implemented,
# or in coding terms, to "abstract", the small details of a problem
# If the small details are taken care of, we can build and build to perform more complex processes.

# This is how you "declare" a function:

def function_name(argument1, argument2):
#   implementation goes here, indented
#   Ex.
    if helper_function1() == constant1:
        return helper_function1()
    else:
        helper_function2(constant1)

# You must declare a function before "calling" it. 

# This is how you call a function:

function_name(argument1=constant2, argument2=constant3)

# You will get yellow squigglies under the above code if you are in VsCode

# This means that if you try to run this file with the Python interpreter 
# (by typing python C_functions.py into your terminal), you will get an error

# Tip for VsCode: highlight multiple lines of text and then press ctrl+/ to add (or remove) the # 
# which will comment or uncomment the line of code

# Challenge: 
#   Somewhere above line 9...
#    1. give these helper_functions both declarations
#    2. set the constants equal to something 
#    3. try running with the Python interpreter and see your output


# Ex. Contract for split() function: 
#        - input / arguments = 1. a string to divide into pieces a
#                              2. a string to split the text on
#          Arranged like so:

greeting_list = "hi:hello:hola".split(":")

#        - processing = we don't care!
#        - output = a list of strings that have been split the given argument #2


# Let's implement our own version of split
def split(str1, split_char):
    output = []
    cur_str = ""
    for char in str1:
        if char is split_char:
            output.append(cur_str)
        else:
            cur_str += char


# In the future, use library function split() (a function of the str object in Python)

# That way you don't need to build from building blocks that you could've used
# in the first place.
#    - You wouldn't want to use a bunch of 2x2 Lego bricks if you have an 8x2


def add_plus_5(left: int, right: int) -> int:
    sum = left + right + 5

    return sum

def concatenate(left, right):
    together = str(left) + str(right)
    return together


# Uncomment below to see your output!
# print(add_plus_5(2, 5))
# print(concatenate(6, "five"))



# GOAL: Make function to print a pyramid of stars

# Implentation from a few classes ago...

# my_list = range(100)
# for number in my_list:
#     print("*" * number)


# Let's convert this implementation into two functions (not practical but a
# good demo of functions calling functions)...

# Let's make our basic building block:
def print_star_row(n_stars_to_print: int):
    star_string = "*" * n_stars_to_print
    print(star_string)


def print_star_pyramid(bottom_row_length: int):
    number_of_rows = bottom_row_length
    for i in range(number_of_rows):
        print_star_row(i)

# print_star_pyramid(3)





# CLASS GAME:
# print character sprite (made of stars and other characters: an attribute of everyone's character)
#    ____nn_
#   /      \
# _|   []   \
# 3_        =
#  |  \____|
#   \______/

# print("   ____nn_\n  /      \\n_|   []   \\n3_        =\n |  \____|\n  \______/")

# print wrong the first time, need an escape for backslash
# print("   ____nn_\n  /      \\\n_|   []   \\\n3_        =\n |  \____|\n  \______/")
     
# different sprites for different actions
# character sprite could also be printing a picture
