import sqlite3

#Evt. Datenbank neu
connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO emotions (label, explanation, etymology, example) VALUES (?, ?)",
            ('First label', 'first explanation')
            )

connection.commit()
connection.close()
