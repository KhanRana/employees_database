# Write your code to expect a terminal of 80 characters wide and 24 rows high

# import sqlite3
import sqlite as data
from employee import Employee, Manager, Developer

# connection = data.connect_database('employee.db')

# c = data.create_cursor(connection)

# data.create_table(c)


def create_manager():
    """
    Adds Manager to the database
    """
    while True:
        print("Add an Manager for the database\n")
        print("Please enter the following details\n")
        try:
            first_name = input("First Name:\n").lower()
            last_name = input("Last Name:\n").lower()
            salary = int(input("Salary:\n"))
            if (first_name != '' and last_name != '' and salary != ''):
                print("Creating your profile\n")
                manager = Manager(first_name, last_name, salary)
                data.add_employee(manager)
                print(f"Welcome {first_name}")
                print("You have been added to the database.")
                break
            print("Please enter valid values for all fields!")
        except ValueError:
            print("Please enter valid value for all enteries, try again!")


def add_employees():
    """
    Creates new employee and add it to the database
    """
    while True:
        try:
            first_name = input("First Name:\n").lower()
            last_name = input("Last Name:\n").lower()
            role = input(
                "Role (enter 'programmer' if you are a programmer):\n")
            if role.lower() == "programmer":
                expertise = input("Expertise: ")
            salary = int(input("Salary:\n"))
            if (first_name and last_name and role and salary != ''):
                print("Creating New Employee\n")
                if role.lower() == "programmer":
                    emp = Developer(first_name, last_name,
                                    role, expertise, salary)
                else:
                    emp = Employee(first_name, last_name, role, salary)

                data.add_employee(emp)

                print("Employee created and added to the database\n")
                break
            print("Please enter valid values for all fields!")
        except ValueError:
            print("Please enter valid value for all enteries, try again!")


def remove_employee():
    """
    Removes an employee from the database
    by first and last name
    """
    while True:
        try:
            first_name = input("First Name:\n").lower()
            last_name = input("Last Name:\n").lower()
            if (first_name and last_name != ''):
                data.remove_employee(first_name, last_name)
                print("Employee has been removed if existed in the database")
                break
            print("Please enter valid values for all fields!")
        except ValueError:
            print("Please enter valid value for all enteries, try again!")


def search_employee():
    """
    Search single employee by first and last name
    """
    while True:
        try:
            first_name = input("First Name:\n").lower()
            last_name = input("Last Name:\n").lower()
            if (first_name and last_name != ''):
                print(data.select_employee(first_name, last_name))
                break
            print("Please enter valid values for all fields!")
        except ValueError:
            print("Please enter valid value for all enteries, try again!")


def all_employees():
    """
    Get total number of employees and their details
    """
    print(f"Total employees: {data.show_all_employee()[1]}")
    print("The list of employee:\n")
    print(data.show_all_employee()[0])


def apply_pay_raise():
    """
    Apply pay raise to an employee
    """
    while True:
        try:
            first_name = input("First Name:\n").lower()
            last_name = input("Last Name:\n").lower()
            new_pay = int(input("New Pay:\n"))
            if (first_name and last_name != ''):
                data.update_pay(first_name, last_name, new_pay)
                print(f"New pay for {first_name} {last_name} is {new_pay}")
                break
            print("Please enter valid values for all fields!")
        except ValueError:
            print("Please enter valid value for all enteries, try again!")


def get_user_choice():
    """
    Get an operation option from the user
    """
    while True:
        print("Select an option from the following\n")
        print("0: To exit the program")
        print("1: Create an employee")
        print("2: Delete an employee")
        print("3: Search employees")
        print("4: Apply pay raise")
        print("5: Check all employees\n")
        try:
            your_choice = input("Enter your choice here: ")
            choice = int(your_choice)
            if 0 <= choice <= 5:
                print(f"You would like to perform operation {choice}")
                break
        except ValueError:
            print("Please enter a valid value\n")
    return choice


def perform_requested_operation(requested_operation):
    """
    Receives users reponse and performs requested task
    """
    if requested_operation == 0:
        print("Exit the prgram")
        exit()
    if requested_operation == int(1):
        add_employees()
    elif requested_operation == int(2):
        remove_employee()
    elif requested_operation == int(3):
        search_employee()
    elif requested_operation == int(4):
        apply_pay_raise()
    elif requested_operation == int(5):
        all_employees()
    else:
        print("Invalid input")


def main():
    """
    Runs the program
    """
    connection = data.connect_database('employee.db')

    c = data.create_cursor(connection)

    data.create_table(c)

    create_manager()

    while True:
        operation = get_user_choice()
        if operation == 0:
            print("Terminating the program")
            data.drop_table()
            print("Records Erased!")
            break

        perform_requested_operation(operation)


main()