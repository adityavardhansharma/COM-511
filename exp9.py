class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print("Manager")


class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")
        print("Developer")


# Main program
employees = []

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Display Employee Information")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Employee Salary: "))
        role = input("Enter Employee Role (Manager/Developer): ")

        if role.lower() == 'manager':
            department = input("Enter Manager's Department: ")
            employee = Manager(emp_id, name, salary, department)
        elif role.lower() == 'developer':
            programming_language = input("Enter Developer's Programming Language: ")
            employee = Developer(emp_id, name, salary, programming_language)
        else:
            print("Invalid role. Please enter either 'Manager' or 'Developer'.")

        employees.append(employee)
        print("Employee added successfully.")

    elif choice == '2':
        if not employees:
            print("No employees in the system.")
        else:
            for employee in employees:
                employee.display_info()

    elif choice == '3':
        print("Exiting the Employee Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
