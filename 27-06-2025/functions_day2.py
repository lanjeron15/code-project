def greet(name):
    print("Привет,", name)
greet("vova")

def add(a, b):
    return a + b
result = add(5, 3)
print(result)



def evaluate_hero(strength, magic, speed):
    score = strength * 2 + magic * 3 + speed

    if score > 100:
        return " legendary hero"
    elif score > 60:
        return " strong hero"
    else:
        return " normal hero"

s = int(input("strenght (0–30): "))
m = int(input("magic (0–30): "))
sp = int(input("speed (0–30): "))

result = evaluate_hero(s, m, sp)
print("result:", result)


