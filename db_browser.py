import sqlite3

conn = sqlite3.connect("tutorial.db")
cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS tutoDB(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    cur.execute("INSERT INTO tutoDB VALUES(123456, '2018-10-21', 'Python', 8)")
    conn.commit()
    cur.close()
    conn.close()

create_table()
data_entry()