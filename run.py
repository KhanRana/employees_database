# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sqlite3
import sqlite as data

connection = sqlite3.connect('employee.db')

c = connection.cursor()

data.create_database()


