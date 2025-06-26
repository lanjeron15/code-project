def greet(name):
    print("hello,", name)
greet("vova")  # → hello, vova
greet("dad")  # → hello, dad

#-------------------------------------------------------------------------------

def add(a, b):
    return a + b

result = add(8, 10)
print("result:", result)   # → 8

#-------------------------------------------------------------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "You can't divide by zero!"
    return a / b

try:
    a = int(input("Type your first number: "))
    b = int(input("Type your second number: "))
except ValueError:
    print("❌ Error: Please enter numbers only.")
    exit()

operation = input("Choose operation (+ - * /): ")

if operation == "+":
    print("Result:", add(a, b))
elif operation == "-":
    print("Result:", subtract(a, b))
elif operation == "*":
    print("Result:", multiply(a, b))
elif operation == "/":
    print("Result:", divide(a, b))
else:
    print("❌ Unknown operation")




