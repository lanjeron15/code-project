# 📘 Day 4 — Working with Lists, Dictionaries and Functions Together

## 🧠 What I learned:

- How to store multiple students using a **list of dictionaries**
- How to use a **`for` loop** to go through each student
- How to **call functions inside a loop** to calculate grades
- How to use `return` to **send results from one function to another**
- How to print a nice **report** for each student

## 🧪 Example code:

```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    else:
        return "C"

def message(grade):
    if grade == "A":
        return "Excellent work!"
    elif grade == "B":
        return "Good job, but keep improving."
    else:
        return "Keep practicing, you can do better."

students = [
    {"name": "Vova", "score": 82},
    {"name": "Arsen", "score": 91},
    {"name": "Peter", "score": 70},
    {"name": "Anna", "score": 95}
]

for student in students:
    grade = get_grade(student["score"])
    comment = message(grade)
    print("Name:", student["name"])
    print("Score:", student["score"])
    print("Grade:", grade)
    print("Message:", comment)
    print("--------------------")
```

## ✅ Project result:
The program goes through a list of students, calculates their grade (A, B, or C), and prints a message for each one.

Great practice in combining: **lists, dictionaries, functions, loops, return, and logic**! 💪