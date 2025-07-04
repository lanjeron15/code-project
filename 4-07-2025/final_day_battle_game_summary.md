# 🧙‍♂️ Final Day — Hero Battle with Random Names

## 🧠 What I built:

A full **turn-based battle game** using:

- `def` functions
- `return` values
- `random` module for dynamic gameplay
- dictionaries to store hero info
- a battle loop with `while`
- functions calling other functions

## 🎯 Game Features:

- Two heroes get **random names** from a name list
- Each hero has:
  - `hp` (health points) = 100
  - random `power` between 10–20
- Each turn, a hero does **random damage** to the opponent
- Game continues until one hero loses
- Winner is shown at the end

## 🧪 Code Preview:

```python
names = ["Axel", "Blaze", "Nova", "Zara", "Orion", "Lyra", "Drake", "Kael"]
name1 = random.choice(names)
name2 = random.choice([n for n in names if n != name1])

hero1 = create_hero(name1)
hero2 = create_hero(name2)

battle(hero1, hero2)
```

## ✅ What I learned:

- How to use `random.choice()` and `random.randint()`
- How to keep hero stats in dictionaries
- How to create a full looped game using functions
- How to build logic into a real game project

This was my final project for the week on **functions** in Python!