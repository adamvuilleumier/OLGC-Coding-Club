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

    def attack(self, damage: int, pokemon_to_attack):
        # if weakness(self.type, pokemon_to_attack.type):
        pokemon_to_attack.take_damage(damage)



print("Start screen:")
print("Select an option:")
print("     Start game")
print("     View leaderboard")

selection = input()

def start_game():
    # pokemon come out of pokeball
    charmander = Pokemon("charmander", "fire")
    bulbasaur = Pokemon("bulbasaur", "grass")

    current_attacker = charmander
    current_defender = bulbasaur
    while current_attacker.health > 0 and current_defender.health > 0:
        # print out health
        # print("Charmander health: " + str(charmander.health))
        print(f"Charmander health: {charmander.health}")
        print("Bulbasaur health")
        print(bulbasaur.health)

        print(f"{current_attacker} is attacking, say an attack")
        attack_type = input()
        attack_damage = current_attacker.attack_list[attack_type]
        current_attacker.attack(attack_damage, current_defender)

        for i in range(30):
            print()

        # change turns
        if current_attacker == charmander:
            current_attacker = bulbasaur
            current_defender = charmander
        else:
            current_attacker = charmander
            current_defender = bulbasaur


    if current_attacker.health > 0:
        print(f"{current_attacker} wins!!!!")
    else:
        print(f"{current_defender} wins!!!!")



def show_leaderboard():
    print("---------------------------")
    print("Adam has the high score of 100")
    print("Jaden has 99")
    print("---------------------------")



if selection == "Start game":
    start_game()
elif selection == "View leaderboard":
    show_leaderboard()
else:
    print("give a valid command")
