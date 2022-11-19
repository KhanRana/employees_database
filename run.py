# Write your code to expect a terminal of 80 characters wide and 24 rows high

# import sqlite3
import sqlite as data

connection = data.connect_database('employee.db')

c = data.create_cursor(connection)

data.create_table(c)


