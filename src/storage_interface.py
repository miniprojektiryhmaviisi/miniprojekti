import sqlite3
from database_connection import get_bookref_connection
from database_connection import get_aref_connection
from database_connection import get_iref_connection

class StorageInterface:
    def __init__(self, connection1,connection2,connection3):
        self._connection1=connection1
        self._connection2=connection2
        self._connection3=connection3
    def store_bookref(self, bookref):
        db_connection=self._connection1.cursor()
        db_connection.execute("INSERT INTO BReferences(dbkey,author,title,publisher,year,volume,number,pages,month,note) VALUES (?,?,?,?,?,?,?,?,?,?)",("ww","ww","ss","ss",22,22,22,"2",2,"no"))
        self._connection1.commit()

    def store_articleref(self, articleref):
        db_connection=self._connection2.cursor()

        query = f"INSERT INTO BReferences VALUES \
                ({articleref.key}, {articleref.author}, {articleref.title}, \
                {articleref.journal}, {articleref.year}, \
                {articleref.volume}, {articleref.number}, \
                {articleref.pages}, {articleref.month}, \
        {articleref.note})"
        db_connection.execute(query)
        self._connection2.commit()

    def store_inproref(self, inproref):
        db_connection=self._connection3.cursor()

        query = f"INSERT INTO BReferences VALUES \
                ({inproref.key}, {inproref.author}, {inproref.title}, \
                {inproref.booktitle}, {inproref.year}, \
                {inproref.editor}, {inproref.volume}, \
                {inproref.number}, {inproref.series}, \
                {inproref.pages}, {inproref.address}, \
                {inproref.month}, {inproref.organization}, \
                {inproref.publisher}, {inproref.note})"
        db_connection.execute(query)
        self._connection3.commit()

    def get_all_from_bookref(self):
        db_connection=self._connection1.cursor()
        query = "SELECT * FROM BReferences"
        res = db_connection.execute(query).fetchall()
        return res
    def find_key_from_bookref(self,key,table):
        db_connection=self._connection1.cursor()
        query = f"SELECT dbkey FROM BReferences WHERE dbkey={key}"
        exist=db_connection.execute(query).fetchall()
        if len(exist)!=0:
            return False
        return True
refe_interface=StorageInterface(get_bookref_connection(),get_aref_connection(),get_iref_connection())
