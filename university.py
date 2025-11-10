# Working with database

import sqlite3

# need to connect or create a database
conn = sqlite3.connect("University.db")

# create a cursor obj
cur = conn.cursor()

# create a table

cur.execute('''CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            MISIS TEXT)
            ''')

# INSERT DATA - A ROW INTO THE TABLE
cur.execute("INSERT INTO students(name, age, MISIS) VALUES(?, ?, ?)",
            ('Albert', 38, 'M01035627'))

cur.executemany("INSERT INTO students(name, age, MISIS) VALUES(?, ?, ?)",
                [('Alice', 88, 'M01059345'), ('Bob', 70, 'M01042759')])

# changes to be saved by using 'commit'
# conn.commit()

# query the database
# cur.execute("SELECT * FROM students")

cur.execute('''UPDATE students SET age = ? WHERE name = ?''', (40, 'Albert'))
# cur..execute('''UPDATE student SET age = 40 WHERE (name = 'Albert')''')

conn.commit()

cur.execute("SELECT * FROM students")

# print(cur.fetchall())

# print(cur.fetchone())

for row in cur.fetchall():
    print(row)

conn.close()
