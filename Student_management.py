students = []

# add student

def add_student():
    roll = int(input("enter the roll number: "))
    name = input("enter the name: ")
    age = int(input("enter your age: "))
    course = input("enter course: ")
    marks = int(input("enter the marks: "))

    for student in students:
        if student["roll"] == roll:
            print("roll number already exists!")
            return

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
    }

    students.append(student)
    print("student added successfully")


# view student

def view_students():
    if len(students) == 0:
        print("no student found")
        return

    print("\nRoll\tName\tAge\tCourse\tMarks")
    print("-" * 45)

    for student in students:
        print(
            student["roll"], "\t",
            student["name"], "\t",
            student["age"], "\t",
            student["course"], "\t",
            student["marks"],
        )


# search student

def search_student():
    roll = int(input("enter roll number : "))

    for student in students:
        if student["roll"] == roll:
            print(student)
            return

    print("student not found")


# update student

def update_student():
    roll = int(input("enter roll number: "))

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("new name: ")
            student["age"] = int(input("new age: "))
            student["course"] = input("new course: ")
            student["marks"] = int(input("new marks: "))
            print("record updated")
            return

    print("student not found")


# delete student

def delete_student():
    roll = int(input("enter roll number: "))

    for student in list(students):
        if student["roll"] == roll:
            students.remove(student)
            print("student deleted")
            return

    print("student not found")


# grade

def calculate_grade():
    roll = int(input("enter roll number: "))

    for student in students:
        if student["roll"] == roll:
            marks = student["marks"]

            if marks >= 90:
                grade = "A+"
            elif marks >= 80:
                grade = "B+"
            elif marks >= 70:
                grade = "C+"
            elif marks >= 60:
                grade = "D+"
            elif marks >= 50:
                grade = "E"
            else:
                grade = "FAIL"

            print("grade =", grade)
            return

    print("student not found")


# topper

def topper():
    if len(students) == 0:
        print("no students")
        return

    top = students[0]
    for student in students:
        if student["marks"] > top["marks"]:
            top = student

    print("\nTopper Details")
    print(top)


# count students

def count_students():
    print("total students = ", len(students))


# main menu
while True:
    print("\n==== STUDENT MANAGEMENT SYSTEM ====")
    print("1. add student")
    print("2.view student")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("6.calculate grade")
    print("7.display topper")
    print("8.count students")
    print("9.exit")

    choice = int(input("entr choice:"))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        calculate_grade()
    elif choice == 7:
        topper()
    elif choice == 8:
        count_students()
    elif choice == 9:
        print("thank you")
        break
    else:
        print("invalid choice")
