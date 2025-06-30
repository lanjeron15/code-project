def outer():
    print("I am an external function")

    def inner():
        print("I am an internal function")

    inner()

outer()


#def check_score(score):   return выбирает, какой результат вернуть в зависимости от значения.
#    if score >= 90:
#        return "Awesome"
#    elif score >= 70:
#        return "Good"
#    else:
#        return "You can do better"


def get_points(math, english):
    return math + english  # сумма двух оценок

def show_result(name, total):
    print(name, "набра(л/ла)", total, "баллов")

# запускаем
points = get_points(5, 4)         # → 9
show_result("Вова", points)
#get_points() возвращает сумму (5+4)
#show_result() берёт результат и печатает



def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    else:
        return "C"

def message(grade):
    if grade == "A":
        return "Awesome"
    elif grade == "B":
        return "You can do better"
    else:
        return "Bad"

# запуск
my_grade = get_grade(100)
print(message(my_grade))






