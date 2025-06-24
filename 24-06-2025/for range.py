#for number in range(10):            for — это цикл, который повторяет действия несколько раз.
     #print(number)                  range(n) создаёт последовательность чисел n-1

#for number in range(5):
#    print("Привет!", number)

#for i in range(1, 6):
#    print("Шаг", i)

text = "Вова"
for letter in text:
    print(letter)

fruits = ["яблоко", "банан", "груша"]
for fruit in fruits:
    print("Я люблю", fruit)

for row in range(3):
    for col in range(5):
        print("*", end="")
    print()  # перенос строки


height = int(input("Высота пирамиды: ")) #Спрашивает у пользователя, какой высоты должна быть пирамида.Например, если ты введёшь 4, то будет 4 строки.
for number in range(1, height + 1): #Запускает цикл от 1 до height включительно (то есть 1, 2, 3, ..., height).
    spaces = " " * (height - number) #Считает, сколько пробелов нужно, чтобы звёздочки были по центру.
    stars = "*" * (2 * number - 1) #Считает сколько звёздочек нужно нарисовать на текущей строке.
    print(spaces + stars) #печттет их








