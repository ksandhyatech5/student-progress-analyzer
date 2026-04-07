from db import collection


# 🔹 Add student
def add_student(name, subject, marks):
    student = {
        "name": name,
        "subject": subject,
        "marks": marks
    }
    collection.insert_one(student)
    return {"message": "Student added successfully"}


# 🔹 Get all students
def get_all_students():
    students = []

    data = collection.find()

    for student in data:
        student["_id"] = str(student["_id"])
        students.append(student)

    return students