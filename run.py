# Write your code to expect a terminal of 80 characters wide and 24 rows high

# import sqlite3
import sqlite as data
from employee import Employee, Manager, Developer

connection = data.connect_database('employee.db')

c = data.create_cursor(connection)

data.create_table(c)


def create_manager():
    """
    Adds Manager to the database
    """
    print("Please enter the following details\n")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    salary = int(input("Salary: "))

    print("Creating your profile\n")
    manager = Manager(first_name, last_name, salary)
    data.add_employee(manager)
    print("Manager has been added to the database.")


def get_user_choice():
    """
    Get an operation option from the user
    """
    while True:
        print("Select an option from the following\n")
        print("1: Create an employee")
        print("2: Delete an employee")
        print("3: Search employees")
        print("4: Apply pay raise")
        print("5: Check number of employees\n")
        try:
            your_choice = int(input("Your would like to select: "))
            if your_choice in range(1, 6):
                print(f"You would like to perform operation {your_choice}")
                break
        except ValueError:
            print("Please enter a valid value\n")
    return your_choice


requested_operatoin = get_user_choice()


def perform_requested_operation(requested_operation):
    if requested_operation == 1:
        add_employees()
    elif requested_operation == 2:


def add_employees():
    """
    Creates new employee and add it to the database
    """
    
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    role = input("Role: ")
    if role.lower() == "programmer":
        expertise = input("Expertise: ")
    salary = int(input("Salary: "))
    print("Creating New Employee\n")
    if role.lower() == "programmer":
        emp = Developer(first_name, last_name, role, expertise, salary)
    else:
        emp = Employee(first_name, last_name, role, salary)

    data.add_employee(emp)

    print("Employee created and added to the database\n")


# add_employees(choice)

# data.remove_employee("Khan")

# data.update_pay("Rana", "Khan", 90000)
create_manager()
print(data.select_employee("Rana", "Khan"))
print(data.show_all_employee()[0])

print(data.show_all_employee()[1])
