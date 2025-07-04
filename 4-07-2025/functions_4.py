import random

def create_hero(name):
    return {
        "name": name,
        "hp": 100,
        "power": random.randint(10, 20)
    }

def attack(attacker, defender):
    damage = random.randint(5, attacker["power"])
    defender["hp"] -= damage
    print(f"{attacker['name']} attacks {defender['name']} for {damage} damage!")

def show_status(hero):
    print(f"{hero['name']} HP: {hero['hp']}")

def is_alive(hero):
    return hero["hp"] > 0

def battle(hero1, hero2):
    print("⚔️ BATTLE STARTS!")
    while is_alive(hero1) and is_alive(hero2):
        attack(hero1, hero2)
        if is_alive(hero2):
            attack(hero2, hero1)
        show_status(hero1)
        show_status(hero2)
        print("--------------")

    if is_alive(hero1):
        print(f"🏆 {hero1['name']} WINS!")
    else:
        print(f"🏆 {hero2['name']} WINS!")

# Random name generation
names = ["Axel", "Blaze", "Nova", "Zara", "Orion", "Lyra", "Drake", "Kael"]
name1 = random.choice(names)
name2 = random.choice([n for n in names if n != name1])

hero1 = create_hero(name1)
hero2 = create_hero(name2)

battle(hero1, hero2)

