# A function takes inputs / arguments and returns outputs

# def function_name(argument1, argument2):
# if condition:
#   helper_function1()
# else:
#   helper_function2()

# GOAL: Print a pyramid of stars

# BUG: number of stars in each row is one too few
def print_star_row(n_stars_to_print):
    star_string = "*" * n_stars_to_print
    print(star_string)

def print_star_pyramid(bottom_row_length: int):
    number_of_rows = bottom_row_length
    for i in range(number_of_rows):
        print_star_row(i)

print_star_pyramid(3)


# CONCEPTS: 
# Zero-indexing: "you aren't born 1 year old, you are born 0 years old"
# The first iteration of a loop and the first index of a list are both 0

# CLASS GAME:
# print character sprite (made of stars and other characters: an attribute of everyone's character)
#    ____nn_
#   /      \
# _|   []   \
# 3_        =
#  |  \____|
#   \______/

print("   ____nn_\n  /      \\n_|   []   \\n3_        =\n |  \____|\n  \______/")

# print wrong the first time, need an escape for backslash
print("   ____nn_\n  /      \\\n_|   []   \\\n3_        =\n |  \____|\n  \______/")

     
# different sprites for different actions
# character sprite could also be printing a picture