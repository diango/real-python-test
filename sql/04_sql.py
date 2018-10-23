import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # Open a csv file and assign it to a variable
    employees = csv.reader(open("employees.csv", "rU"))
    c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
    c.executemany("INSERT INTO employees(firstname, lastname) values(?, ?)", employees)