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

# Sidebar:
# difference between OSX(Apple) and Windows:
#      - Windows gets to access two layers above the "User directory" = a feature
#           - User directory = Desktop, Downloads, Documents
#           - feature = more control, but also need to make a contract/understand/learn
# 
roster_dict = pandas.read_csv()

print(roster_dict.keys())

name_list = roster_dict['Student Name (Last, First)']

for name in names:
    print(name)

    # now let's do some if filtering to reverse the names that need to be reversed


    # now lets store first and last names separately


    # make a class game where students each have a character
    # make a table in the shared google drive folder that has names and other attributes of character