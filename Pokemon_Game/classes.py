import requests
import re
import pandas as pd
from parameters import game_path
class Pokemon():
    def __init__(self, poke_name):
        # TODO: Bugfix when pokemon name is not correctly capitalized
        self.name = poke_name
        self.attack_damage_list = {"Punch": 20, "Kick": 10}
        self.attack_current_cooldown = {"Punch": 0, "Kick": 0}
        self.fill_from_database(poke_name)

    def __str__(self):
        return self.name
    
    def fill_from_database(self, pokemon_name):
        db = pd.read_csv(f"{game_path}/tables/pokemon.csv")
        this_pokemon = db[db["Pokemon Name"] == pokemon_name]
        self.health = int(this_pokemon["HP"])
        self.type = this_pokemon['Types'].values[0]

    def take_damage(self, damage):
        self.health -= damage
        # self.health = self.health - damage

    def attack(self, damage: int, pokemon_to_attack):
        # if weakness(self.type, pokemon_to_attack.type):
        # change the cooldown
        pokemon_to_attack.take_damage(damage)