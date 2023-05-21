# Goal: make a file containing everyone's name

# Imagine if there were 1000 of us in this class, how would we do this without it taking forever??
#
# Idea:
# Let's use other people's work!
# Get the class roster Excel sheet from email
import pandas


# Quick Lesson on Filepaths:
#   Absolute filepath = the full path from the "root" of your computer 
#   Root = the location on your computer you get if you "cd .." until you can't anymore
#        - if you pwd at your root, you will see "/" as the output
#   Relative filepath = the path to a file from another location on your computer
#        Ex. Let's say I cloned the "OLGC-Coding-Club" repo on my Desktop cd'ed into that folder, 
#            if my working directory is here, the relative filepath to Downloads is ../../Downloads
#   Working directory = the green letters on your terminal (ie. C:\Users\adamv\Desktop\OLGC-Coding-Club\)
#         - the place where relative filepaths start from

# challenge: get the absolute path to your computer's Downloads folder
# 
# 
# solution: cd to Downloads and run "pwd"


# read the class roster table into a dictionary / dataframe variable called "roster_dict"
# Absolute path (if I just Downloaded the csv from my browser)
# roster_dict = pandas.read_csv("C:/Users/adamv/Downloads/Coding club 4th qtr 2023 (Responses) - Form Responses 1.csv")
#                             ^^^ - replace this filepath with the output of "pwd" command
# Relative path (since the csv is also copied in this repo)
roster_dict = pandas.read_csv("class_roster.csv")

# print the keys of the dictionary (the columns)
print("Columns of input table")
print(roster_dict.keys())

# get a list of students names from the table column named "Student Name (Last, First)"
name_list = roster_dict['Student Name (Last, First)']

print("Contents of Student Name (Last, First) column:")
print(name_list)

# go through each entry in name_list and print out the first names only
print("Printing first names only:")
for full_name in name_list:
    # Split() function: a built-in Python function (you'll get familiar with these over time)
    #     Reference: https://www.w3schools.com/python/ref_string_split.asp
    # ex. full_name = "Adam Vuilleumier"
    #     print(full_name.split(" "))         ->     a two element list, ["Adam", "Vuilleumier"]

    # for each full_name (a string datatype), split by the space character into a list of strings
    if " " in full_name:
        first_last_name = full_name.split(" ")
    # if full_name does not contain a space (ie. Vuilleumier,Adam), split by the "," character
    else:
        first_last_name = full_name.split(",")

    # special case where we have Last Name First Name (with no comma)
    if "Furtado" in first_last_name:
        print(first_last_name[1])
        continue

    # special case where we have Last Name First Name (with no comma)
    if "Chirpka" in first_last_name:
        print(first_last_name[1])
        continue

    # if there is a comma, the first name is the second item in first_last_name
    # (element 1, because of zero-indexing)
    if "," in full_name:
        print(first_last_name[1])
    # if there is no comma, the first name is the first item in first_last_name
    else:
        print(first_last_name[0])
