from functions import pokemon_fight, show_leaderboard
from classes import Pokemon


print("Start screen:")
print("Select an option:")
print("     Start game")
print("     View leaderboard")

selection = input()

my_pokemon = Pokemon("Bulbasaur")
my_opponent = Pokemon("Charmander")

if selection == "Start game":
    pokemon_fight(my_pokemon, my_opponent)
elif selection == "View leaderboard":
    show_leaderboard()
else:
    print("give a valid command")
