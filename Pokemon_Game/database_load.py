import re
import requests
import pandas as pd
import webbrowser
from urllib.request import urlretrieve
from PIL import Image
from params import GAME_PATH, ASSETS_PATH

from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile


HP_SCALING_FACTOR = 20

# TODO: Make class for this that has the ugly html

def get_pokemon_image_from_internet(pokemon_name: int):
    
    for pokemon_number in range(1,150):
        # get the url
        padded_pokemon_number = str(pokemon_number).rjust(3, "0")
        image_name = f"{padded_pokemon_number}.png"
        url = f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/{image_name}'
        print(url)

        # save the image
        image_path = f"{GAME_PATH}/poke_images/{padded_pokemon_number}.png"
        urlretrieve(url, image_path)
  
        # Opening the image and displaying it (to confirm its presence)
        # img = Image.open(image_path)
        # img.show()
        # webbrowser.open(url)
    return 


def get_pokemon_hp_from_internet(pokemon_name):
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


def get_pokemon_types_from_internet(pokemon_name):
    # get the html from pokedex website
    my_pokemon_url = "https://www.pokemon.com/us/pokedex/" + pokemon_name
    response = requests.get(my_pokemon_url)
    ugly_html = response.text

    # find the lines that have the type information
    lines = ugly_html.split("\n")
    types = []
    for line_content in lines:
        if '"/us/pokedex/?type=' in line_content:  
            result = re.search('>(.*)<', line_content)
            types += [result.group(1)]
    return types


def get_pokemon_sounds_from_internet():
    http_response = urlopen("https://goo.gl/uhAxsg")
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=f"{ASSETS_PATH}/sounds/attacks")

if __name__ == "__main__":
    pokemon_list = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch’d", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]
    get_pokemon_image_from_internet("042")
    # df = pd.DataFrame(columns=["Pokemon Name", "HP", "Types"])

    # for idx, pokemon in enumerate(pokemon_list):
    #     try:
    #         health = get_pokemon_hp_from_internet(pokemon) * HP_SCALING_FACTOR
    #         df.loc[idx, "Pokemon Name"] = pokemon
    #         df.loc[idx, "HP"] = health
    #         df.loc[idx, "Types"] = get_pokemon_types_from_internet(pokemon)
    #     except:
    #         print(f"Cannot get stats from server for {pokemon}")

    # df.to_csv("Pokemon_Game/tables/pokemon.csv")
       