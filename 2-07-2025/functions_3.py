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

# 📋 List of students and their scores
students = [
    {"name": "Vova", "score": 82},
    {"name": "Max", "score": 91},
    {"name": "John", "score": 70},
    {"name": "Anna", "score": 95}
]

# 🔁 Process each student
for student in students:
    grade = get_grade(student["score"])
    comment = message(grade)
    print("Name:", student["name"])
    print("Score:", student["score"])
    print("Grade:", grade)
    print("Message:", comment)
    print("--------------------")
