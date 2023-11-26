# komentoriville: sqlite3 referancedb < schema.sql

import sqlite3

connection = sqlite3.connect('your_database.db')
cursor = connection.cursor()

connection.commit()
connection.close()
