import os

parameters_path = os.path.realpath(__file__)
game_path = os.path.dirname(parameters_path)
print(game_path)