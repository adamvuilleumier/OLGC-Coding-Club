import os

parameters_path = os.path.realpath(__file__)
GAME_PATH = os.path.dirname(parameters_path)
print(GAME_PATH)