
# Intro to Parsing: How Data is Made

#   - Parsing is how data is processed and formed into new data

#    - Understanding is built one step at a time; so is parsing
#    - Understanding is storing data (the state of something at a moment in
#      time) in a structure in your head
#    - Parsing is generating data structures (ie. dictionaries) in code
#    - Parsing is how the computer understands data
#    - Data always comes down to a stream of 1s and 0s ordered in a certain way
#      (code.py files)
#    - The computer reads the stream as it comes in, which is visualized from right to left in a stream

# stream = [ "C" + "a" + "t"]

#   - We can use a Python function to do the job of parsing because a Python function has:

#     Inputs: functionName(<the arguments inside here>)
#            Ex. get_height(basketball_player)

#     Processing: some database access / web scraping to find the right piece of data

#     Outputs: return height


#   Assume your computer can use hardware devices made by electrical engineers
#   to interpret the wave which is being sent by a webserver you are accessing as a
#   stream of 1s and 0s of binary telling it which functions to perform on what data.

#   Lets outline a basic parser to use for interpreting binary as letters:

#       Agreement between parser and parsee is a 5 bit word length for
#       binary to integer conversion:
#       Ex. 01101     ->     13   

#       Agreement between parser and parsee is to convert from integer to
#       lowercase character by alphabetical order (a=1, z=26, ...) 
#       Ex.    13     ->     m

#    - There are lookback and lookahead windows to 5 letters before and in front




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

# Uncomment below:
# print(page.text)

# Wow... that was a lot of output.
# Recomment

import pandas
page = requests.get("https://www.basketball-reference.com/players/j/jokicni01.html")

height_chunks = []
for line in page.text.split("\n"):

    if "tall." in line:
        # Uncomment below:
        # print(line)
        height_chunks.append(line)
