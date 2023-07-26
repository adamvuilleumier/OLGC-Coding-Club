import requests
import re

HP_SCALING_FACTOR = 20

class Pokemon():
    def __init__(self, poke_name, poke_type):
        self.name = poke_name
        self.health = self.get_pokemon_hp_from_internet(poke_name) * HP_SCALING_FACTOR
        self.attack_damage_list = {"Punch": 20, "Kick": 10}
        self.attack_current_cooldown = {"Punch": 0, "Kick": 0}
        self.type = poke_type

    def __str__(self):
        return self.name

    def take_damage(self, damage):
        self.health -= damage
        # self.health = self.health - damage

    def attack(self, damage: int, pokemon_to_attack):
        # if weakness(self.type, pokemon_to_attack.type):
        # change the cooldown
        pokemon_to_attack.take_damage(damage)

    def get_pokemon_hp_from_internet(self, pokemon_name):
        my_pokemon_url = "https://www.pokemon.com/us/pokedex/" + pokemon_name
        response = requests.get(my_pokemon_url)
        ugly_html = response.text

        line_with_hp = 0
        lines = ugly_html.split("\n")
        for line_num, line_content in enumerate(lines):
            if "<span>HP" in line_content:
                line_with_hp = line_num
                break

        line_with_hp_value = line_with_hp - 17

        result = re.search('data-value="(.*)" class', lines[line_with_hp_value])
        return int(result.group(1))
