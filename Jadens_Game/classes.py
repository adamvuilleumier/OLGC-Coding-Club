class Pokemon():
    def __init__(self, poke_name, poke_type):
        self.name = poke_name
        self.health = 100
        self.attack_list = {"Punch": 20, "Kick": 10}
        self.type = poke_type

    def __str__(self):
        return self.name

    def take_damage(self, damage):
        self.health -= damage
        # self.health = self.health - damage

    def attack(self, damage: int, pokemon_to_attack):
        # if weakness(self.type, pokemon_to_attack.type):
        pokemon_to_attack.take_damage(damage)
