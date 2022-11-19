"""
Creating employee database
"""

import sqlite3
from employee import Employee


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
        print("Table already exist")

