#i = 1
#while i <= 500  :
#    print("Привет!", i)
#    i += 1

#while True:
#    text = input("Введи '1', чтобы остановиться: ")
#    if text == "1":
#        break
#    print("Ты ввёл:", text)

secret = 7
guess = 0

while guess != secret:
    guess = int(input("Угадай число от 1 до 10: "))
    if guess == secret:
        print("Правильно! ")
    else:
        print("Попробуй ещё!")
