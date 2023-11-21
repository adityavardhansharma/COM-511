# Function to display all records in the database
def display_records(database):
    print("Student Records:")
    print("-----------------")
    print("ID\tName\t\tGrade")
    print("-----------------")
    for record in database:
        print(f"{record[0]}\t{record[1]}\t\t{record[2]}")
    print("-----------------")

# Function to search for a record by student ID
def search_record(database, search_id):
    for record in database:
        if record[0] == search_id:
            return record
    return None

# Main program
student_database = [
    ("001", "John Doe", "A"),
    ("002", "Jane Smith", "B"),
    ("003", "Bob Johnson", "C"),
    ("004", "Alice Brown", "A"),
]

while True:
    print("\n1. Display all records")
    print("2. Search for a student record")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        display_records(student_database)
    elif choice == '2':
        search_id = input("Enter the student ID to search: ")
        result = search_record(student_database, search_id)
        if result:
            print("\nStudent found!")
            print(f"ID: {result[0]}")
            print(f"Name: {result[1]}")
            print(f"Grade: {result[2]}")
        else:
            print("\nStudent not found.")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
