# komentoriville: sqlite3 referencedb.db < schema.sql
import sqlite3

connection = sqlite3.connect('referencedb.db')
db = connection.cursor()
