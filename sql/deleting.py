import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("SELECT firstname, lastname from employees")

    # fetchall() method retrieves all method from query
    rows = c.fetchall()

    # output the row to the screen row by row
    for r in rows:
        print(r[0], r[1])