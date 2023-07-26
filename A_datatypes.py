# operators vs. data
# every term in python is either a comment, operator (function) or data (variable)

# Operator examples are =, -, +, /, *, ^
# Warning! The "=" operator does not mean the same thing in Python as it does in math
#       In Python, "=" is the "load operator" (like loading a video game save file), it names the result of some calculation

# Ex. number = 5           <---   1. find a slot of free memory, name it number, and fill it with 5 (0x101)
#     sum = number + 7     <---   2. reference number's value in memory, add 7 to it, store the result in a memory slot named sum


# first we will learn about data
# data is collected from:
# - a sensor (ie. camera, radar, speedometer)
# - user input (ie. video game controls, button clicks, filling in a form)

# these are the primitive python data types that store / represent data:

# str
what_am_i = "I am a string"

# int
answer_to_ultimate_question = (8 + 6) * 3

# float
acceleration_of_gravity = 9.8

# boolean
is_coding_fun = True

# building from only these simple data types, coders try to make a representation of real life things inside computer memory
# things are represented as "classes" which have "features" or "attributes" which are all either primitive datatypes (or other classes!)
# Ex.
class Dragon:
    def __init__(self, age, species, gold_hoard_value, breathes_fire, color):
        self.age = age
        self.species = species
        self.gold_hoard_value = gold_hoard_value
        self.breathes_fire = breathes_fire


# lets make a dragon!
zolthifax = Dragon(age=1192, species="Hungarian Horntail", gold_hoard_value=152202.78, breathes_fire=True)
bob = Dragon(age=12, species="Magic dragon", gold_hoard_value=300, breathes_fire=False)
print(zolthifax)

# Type() function: takes in a variable as an argument and outputs its datatype (str, int, bool, float) or class
integer = 8
print(type(integer))
print(type(zolthifax))
print("Can Zolthifax breathe fire?" + type(zolthifax.breathes_fire))

# classes can also do things (functions) using information from their attributes
# we will get to functions in more detail next week and classes in more detail in a couple weeks...

# these are built-in Python classes:

# Dict = a dictionary, a mapping of datatype instances (not just string to string), very similar to a class
player_numbers = {"Lebron James": 23, "Nikola Jokic": 15, "Stephen Curry": 30, "Luka Doncic": 77 }

print(player_numbers["Lebron James"])

# a dictionary is a mapping from one piece of data to another


# List = like a shopping list, a grouping of datatype instances

# Ex. 1
prime_numbers_less_than_20 = [2, 3, 5, 7, 11, 13, 17, 19]
# try printing out different items
# print by index
print("First number in the list: " + prime_numbers_less_than_20[1])
# look! it didn't print the first one! why?
# Zero-indexing: "you aren't born 1 year old, you are born 0 years old"


# Ex. 2
hobbits = ["Bilbo Baggins", "Frodo Baggins", "Samwise Gamgee",  "Peregrin Took", "Meriadoc Brandybuck"]
my_list = [what_am_i, answer_to_ultimate_question, is_coding_fun]
print(my_list)
print(hobbits[0])


# Ex. 3
my_crazy_list = [my_list, player_numbers, "extra item??"]
print(my_crazy_list)



# Pro Tip: you can get elements by matching substring (matching any part of the hobbit's name)
print(hobbits["Bilbo" in hobbits])
# "in" is a built-in function that takes in a primitive type on the left side and list on the right side
# Ex. "a" in "pikachu"
# str's are actually lists!
# this is how to print elements of the list that are true for the referenced condition
