from functions import start_game, show_leaderboard
from classes import Pokemon


print("Start screen:")
print("Select an option:")
print("     Start game")
print("     View leaderboard")

selection = input()

my_pokemon = Pokemon()

if selection == "Start game":
    pokemon_fight()
elif selection == "View leaderboard":
    show_leaderboard()
else:
    print("give a valid command")
