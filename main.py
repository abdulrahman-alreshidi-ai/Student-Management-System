import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


students = load_students()


def add_student():

    print("\n=== Add Student ===")

    student_id = input("Student ID: ")
    name = input("Student Name: ")
    age = input("Age: ")
    major = input("Major: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    students.append({
        "id": student_id,
        "name": name,
        "age": age,
        "major": major
    })

    save_students(students)

    print("Student added successfully.")


def view_students():

    print("\n=== Students ===")

    if not students:
        print("No students found.")
        return

    for student in students:
        print("-" * 35)
        print(f"ID    : {student['id']}")
        print(f"Name  : {student['name']}")
        print(f"Age   : {student['age']}")
        print(f"Major : {student['major']}")

def search_student():

    print("\n=== Search Student ===")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("-" * 35)
            print(f"ID    : {student['id']}")
            print(f"Name  : {student['name']}")
            print(f"Age   : {student['age']}")
            print(f"Major : {student['major']}")
            return

    print("Student not found.")


def update_student():

    print("\n=== Update Student ===")

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            student["name"] = input("New Name: ")
            student["age"] = input("New Age: ")
            student["major"] = input("New Major: ")

            save_students(students)

            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student():

    print("\n=== Delete Student ===")

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            save_students(students)

            print("Student deleted successfully.")
            return

    print("Student not found.")


while True:

    print("\n" + "=" * 40)
    print("    STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
