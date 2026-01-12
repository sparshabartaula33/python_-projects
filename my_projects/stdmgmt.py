student_grade = {}

def add_students(name, grade):
    student_grade[name] = grade
    print(f"Added {name} with grade {grade}")

def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name}'s grade updated to {grade}")
    else:
        print(f"{name} not found")

def del_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} deleted successfully")
    else:
        print(f"{name} not found")

def display_students():
    if len(student_grade) == 0:
        print("No students found. Please add some first!")
    else:
        print("\n--- Student List ---")
        for name, grade in student_grade.items():
            print(f"Name: {name} | Grade: {grade}")

def main():
    while True:
        print("\nStudent Grades Management System")
        print("1 : Add student")
        print("2 : Update student")
        print("3 : Delete student")
        print("4 : View students")
        print("5 : Exit")

        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Invalid input! Enter a number.")
            continue

        choice = int(choice)

        if choice == 1:
            name = input("Enter name: ")
            grade = input("Enter grade: ")
            add_students(name, grade)

        elif choice == 2:
            name = input("Enter name: ")
            grade = input("Enter grade: ")
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter name to delete: ")
            del_student(name)

        elif choice == 4:
            display_students()

        elif choice == 5:
            print("Program closed")
            break

        else:
            print("Invalid choice")

main()
