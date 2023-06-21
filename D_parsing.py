
# Intro to Parsing: How Data is Made

#   - Parsing is how data is processed and formed into new data

#   Ex. Assume a racecar can record its speed, acceleration, and tire
#   temperature at each moment in time as it goes around a turn. If we use a...

#   Physical Model = using code to apply the mathematical laws of physics. 
#   Representing some state in the world as math equations with data filling in the constants and
#   variables in the formulas.
#   We can solve for a variable with the = operator in Python
#   Ex.

m = 5
b = 10
x = input()
y = m * x + b
print(y)


#   - Parsing is like (and can be implemented as) a Python function that has
#   inputs, does some processing, and returns outputs: 

#   Ex. Assume your computer can interpret the wave which is being sent by the 
#   webserver you are accessing as a stream of 1s and 0s of binary through hardware made by  electrical engineers
#   telling it which functions to perform on which data.

#   Lets make a basic parser to use for interpreting binary as letters
#       Agreement between parser and parsee is a 5 bit word length for
#       binary to integer conversion:
#       Ex. 01101     ->     13   
#       Agreement between parser and parsee is to convert from integer to
#       lowercase character by alphabetical order (a=1, z=26, ...) 
#       Ex.    13     ->     m


#    
import pandas as pd
inputs = pd.DataFrame(columns=["Racecar speed", "acceleration", "tire temperature"])

#    The row



#    - understanding is built one step at a time; so is parsing

#    - there are lookback and lookahead windows to other frames

# Ex. 

#    - understanding is storing data (the state of something at a moment in
#      time) in a structure in your head



#    - parsing is generating data structures (ie. dictionaries) in code
#    - parsing is how the computer understands data
#    - data always comes down to a stream of 1s and 0s ordered in a certain way
#      code.py files)


#  Ex. 


# Input:
# get request some html site(same thing that happens when you Google something)
# read in the html as text with 

# Process:
# use pattern matching to get desired text and assign it to a key in a dict

# Output:
# print out something to the terminal
# store results in a csv table (Excel/Google sheet)

import requests
page = requests.get("https://www.basketball-reference.com/players/j/jokicni01.html")

# print(page.text)
# Wow... that was a lot of output.

import pandas
page = requests.get("https://www.basketball-reference.com/players/j/jokicni01.html")

for line in page.text.split("\n"):

    if "tall." in line:
        print(line)