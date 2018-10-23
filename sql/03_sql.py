import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    cities = [
        ('Boston', 'MA', 60000000),
        ('Chicago', 'IL', 2700000),
        ('Houston', 'TX', 2100000),
        ('Phoenix', 'AZ', 15000000),
        ('New York City', 'NY', 7500000)
    ]
    
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)