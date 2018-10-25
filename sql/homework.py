import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # # Insert 5 values in the table inventory
    # inventory = [
    #     ("Ford", "Blue", 123),
    #     ("Hondas", "Orange", 25),
    #     ("Hondas", "Green", 852),
    #     ("Ford", "Black", 456),
    #     ("Ford", "Yellow", 741)
    # ]

    # c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", inventory)

    # Update all records where make == "Hondas"
    # c.execute("UPDATE inventory SET Quantity = 951 WHERE Make = 'Hondas' ")

    # print("\nNew Data:\n")

    # c.execute("SELECT * FROM inventory")

    # rows = c.fetchall()

    # for r in rows:
    #     print(r[0], r[1], r[2])

    # execute all records where make == "ford"
    c.execute("SELECT * from inventory WHERE make = 'Ford'")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output headers
    print('Make Model Qty')
    print('--------------')

    # output the rows to the screen, row by row
    for r in rows:
        print(r[0], r[1], r[2])
