# Create a SQLite3 database and table

# Import the sqlite3 library
import sqlite3

# Create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQl commands
cursor = conn.cursor()

# Create a table
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)

#close the database connection
conn.commit()
conn.close()