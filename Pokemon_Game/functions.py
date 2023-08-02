from classes import Pokemon


def pokemon_fight(start_attack_pokemon, start_defend_pokemon):
    # load current_attacker and current_defender variables
    current_attacker = start_attack_pokemon
    current_defender = start_defend_pokemon

    # fight until someone faints
    while current_attacker.health > 0 and current_defender.health > 0:
        # print out health
        print(f"{current_attacker} health: {current_attacker.health}")
        print(f"{current_defender} health: {current_defender.health}")

        print(f"{current_attacker} is attacking, say an attack")
        attack_type = input()
        attack_damage = current_attacker.attack_damage_list[attack_type]
        current_attacker.attack(attack_damage, current_defender)

        # clear screen
        for i in range(30):
            print()

        # change turns
        # what should be filled in here? (remember the i and j swapping example)
        if current_attacker == start_attack_pokemon:
            current_attacker = start_defend_pokemon
            current_defender = start_attack_pokemon
        else:
            current_attacker = start_attack_pokemon
            current_defender = start_defend_pokemon

    # check who won
    if current_attacker.health > 0:
        print(f"{current_attacker} wins!!!!")
    else:
        print(f"{current_defender} wins!!!!")


def show_leaderboard():
    print("---------------------------")
    print("Adam has the high score of 100")
    print("Jaden has 99")
    print("Brannagh has 101")
    print("---------------------------")

