"""
Creates employee database and access to database 
manipulation
"""

import sqlite3

connection = sqlite3.connect('employee.db')

c = connection.cursor()


def connect_database(database):
    """
    creates and/or connects database
    """
    print(f"Connecting to database {database}\n")
    connection = sqlite3.connect(database)
    print(f"Conected to {database}\n")
    return connection


def create_cursor(connection):
    """
    Access the database
    """
    c = connection.cursor()
    return c


def create_table(c):
    """
    Creates employees table
    """
    try:
        c.execute("""CREATE TABLE employees (
                    first text,
                    last text,
                    role text,
                    expertise text,
                    pay integer)""")
    except sqlite3.OperationalError:
        print("Table already exist\n")


def add_employee(emp):
    """Adds employee to the database"""
    with connection:
        c.execute("""INSERT INTO employees VALUES
        (:first, :last, :role, :expertise, :pay)""",
                  {'first': emp.first, 'last': emp.last,
                   'role': emp.role, 'expertise': emp.expertise,
                   'pay': emp.pay})


def show_all_employee():
    """
    displays all employess to the terminal
    """
    with connection:
        c.execute("SELECT * from employees")
        rows = c.fetchall()
        no_of_emps = len(rows)
        return [rows, no_of_emps]


def remove_employee(first_name, last_name):
    """
    Removes an employee from the database
    """
    with connection:
        c.execute("""DELETE FROM employees WHERE
        first=:first AND last=:last""",
                  {'first': first_name, 'last': last_name})


def select_employee(first_name, last_name):
    """
    Search for employees by frist and last name
    """
    with connection:
        c.execute("""SELECT * From employees WHERE
        first=:first AND last=:last""",
                  {'first': first_name, 'last': last_name})

        return c.fetchall()


def update_pay(first, last, new_pay):
    """
    Update the pay of an existing employee
    """
    with connection:
        c.execute("""UPDATE employees SET pay=:pay WHERE 
        first=:first AND last=:last""",
                  {'first': first, 'last': last, 'pay': new_pay})


def drop_table():
    """
    Deletes the employees table
    """
    with connection:
        c.execute("""DROP TABLE employees""")
