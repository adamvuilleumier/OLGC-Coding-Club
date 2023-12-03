from glob import glob
from params import ASSETS_PATH
from random import randint

def get_random_sound():
    sound_folders = glob(f"{ASSETS_PATH}/sounds/attacks/*")
    rand = randint(0, len(sound_folders) - 1)
    random_sound_dir = sound_folders[rand]

    sounds = glob(f"{random_sound_dir}/*")
    rand = randint(0, len(sounds) - 1)
    random_sound = sounds[rand]

    return random_sound