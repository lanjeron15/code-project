#name = input()
#print(len(name))

#text = "Python" это для срезов тоесть частей строки
#print(text[0])
#print(text[0:3])
#print(text[-1])

#first_name = "Vova" это у нас склейка строк
#last_name = "Burinov"
#full_name = first_name + " " + last_name а тут между скобками нету ничего потому что долженбыт пробел
#print("Полное имя:", full_name)

name = input("Как тебя зовут? ")
age = input("Сколько тебе лет? ")
game = input("Во что ты любишь играть? ")
food = input("Какая у тебя любимая еда? ")

print("\n🎮 Твоя анкета:")
print("Имя:", name)
print("Возраст:", age)
print("Любимая игра:", game)
print(f"Любимая еда: {food}")

#name = "Вова" тут я смотрел зачем нужна f это чтоб добовлять переменые без запятых
#print(f"Привет, меня зовут {name}")