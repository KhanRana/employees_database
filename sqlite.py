"""
Creating employee database
"""

import sqlite3
from employee import Employee

connection = sqlite3.connect('employee.db')
c = connection.cursor()


def create_database():
    """
    Creates employee database
    """
    try:
        c.execute("""CREATE TABLE employees (
                    first text,
                    last text,
                    role text,
                    expertise text,
                    pay integer)""")
    except sqlite3.OperationalError:
        print("Table already exist")

