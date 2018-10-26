import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers (nums INT)")

    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0, 100),))