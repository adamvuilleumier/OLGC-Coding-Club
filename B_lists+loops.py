# GOAL: Print a pyramid of stars

# Let's use a loop, or a repeated process on data 

# my_list = range(100)
# for number in my_list:
#     print("*" * number)

# Goal: make a file containing everyone's name






# Imagine if there were 1000 of us in this class, how would we do this without it taking forever??
#
# Idea:
# Let's use other people's work!
# Get the class roster Excel sheet from email
import pandas

# challenge: get the absolute path to your Downloads folder
# 
# 
# solution: cd to Downloads and run "pwd"


# read the class roster table into a dictionary / dataframe variable called "roster_dict"
# Absolute path (if I just Downloaded the csv from my browser)
roster_dict = pandas.read_csv("C:/Users/adamv/Downloads/Coding club 4th qtr 2023 (Responses) - Form Responses 1.csv")
#                             ^^^ - replace this filepath with the output of "pwd" command
# Relative path (since the csv is also copied in this repo)
roster_dict = pandas.read_csv("class_roster.csv")

print(roster_dict.keys())

name_list = roster_dict['Student Name (Last, First)']

for name in names:
    print(name)

    # now let's do some if filtering to reverse the names that need to be reversed


    # now lets store first and last names separately


    # make a class game where students each have a character
    # make a table in the shared google drive folder that has names and other attributes of character
    