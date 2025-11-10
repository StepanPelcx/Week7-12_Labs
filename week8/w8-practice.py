# Working with database

import sqlite3

# need to connect or create a database
conn = sqlite3.connect("Example1.db")

# create a cursor obj
cur = conn.cursor()

# create a table

cur.execute('''CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER)
            ''')

# INSERT DATA - A ROW INTO THE TABLE
cur.execute("INSERT INTO users(name, age) VALUES(?, ?)", ('Albert', 38))

cur.executemany("INSERT INTO users(name, age) VALUES(?, ?)",
                [('Alice', 88), ('Bob', 70)])

# changes to be saved by using 'commit'
conn.commit()

# query the database
cur.execute("SELECT * FROM users")

print(cur.fetchall())

# print(cur.fetchone())

conn.close()
