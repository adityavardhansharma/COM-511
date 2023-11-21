def enter_student_record():
    students = {}
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")

        students[student_id] = {"Name": name, "Grade": grade}

    return students

def search_student_record(students, student_id):
    if student_id in students:
        print("\nStudent found!")
        print(f"Student ID: {student_id}")
        print(f"Name: {students[student_id]['Name']}")
        print(f"Grade: {students[student_id]['Grade']}")
    else:
        print("\nStudent not found.")

# Main program
student_records = enter_student_record()

while True:
    print("\n1. Search for a student")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        search_id = input("Enter the student ID to search: ")
        search_student_record(student_records, search_id)
    elif choice == '2':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")
