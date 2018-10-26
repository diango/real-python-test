import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")

    orders = [
        ("Ford", "Green", 1985-12-25),
        ("Hondas", "Orange", 1546-2-12),
        ("Ford", "Yellow", 1999-5-15),
        ("Hondas", "Black", 1998-7-16),
        ("Hondas", "Yellow", 2000-11-27),
        ("Hondas", "Green", 2001-8-19),
        ("Ford", "Green", 2002-10-20),
        ("Hondas", "Yellow", 2003-9-30),
        ("Hondas", "Yellow", 2004-6-18),
        ("Ford", "Black", 2005-4-19),
        ("Ford", "Green", 2006-3-29),
        ("Ford", "Green", 2007-1-7),
        ("Ford", "Yellow", 2008-11-12),
        ("Ford", "Green", 2009-10-5),
        ("Hondas", "Green", 2010-4-26)
    ]

    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)
