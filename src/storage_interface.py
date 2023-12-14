from database_connection import get_bookref_connection
from database_connection import get_aref_connection
from database_connection import get_iref_connection
from db_build import build

class StorageInterface:
    def __init__(self, connection1,connection2,connection3):
        self._connection1=connection1
        self._connection2=connection2
        self._connection3=connection3

    def store_bookref(self, bookref):
        db_connection=self._connection1.cursor()
        try:
            db_connection.execute("INSERT INTO BReferences\
            (dbkey,author,title,publisher,year,volume,number,pages,month,note) \
            VALUES (?,?,?,?,?,?,?,?,?,?)",(bookref.key,bookref.author[0],\
            bookref.title,bookref.publisher,bookref.year,bookref.volume,\
            bookref.number,bookref.pages,bookref.month,bookref.note))
        except Exception as exc:
            raise exc
        self._connection1.commit()

    def store_articleref(self, articleref):
        db_connection=self._connection2.cursor()
        try:
            db_connection.execute("INSERT INTO AReferences\
            (dbkey,author,title,journal,year,volume,number,pages,month,note) \
            VALUES (?,?,?,?,?,?,?,?,?,?)",(articleref.key,articleref.author[0],\
            articleref.title,articleref.journal,articleref.year,articleref.volume,\
            articleref.number,articleref.pages,articleref.month,articleref.note))
        except Exception as exc:
            raise exc
        self._connection2.commit()

    def store_inproref(self, inproref):
        db_connection=self._connection3.cursor()
        try:
            db_connection.execute("INSERT INTO IReferences\
            (dbkey,author,title,booktitle,year,editor,volume,number,series,pages,\
            address,month,organization,publisher,note)\
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(inproref.key,inproref.author[0],\
            inproref.title,inproref.booktitle,inproref.year,inproref.editor,\
            inproref.volume,inproref.number,inproref.series,inproref.pages,\
            inproref.address,inproref.month,inproref.organization,\
            inproref.publisher,inproref.note))
        except Exception as exc:
            raise exc
        self._connection3.commit()

    def get_all_from_bookref(self):
        db_connection=self._connection1.cursor()
        query = "SELECT * FROM BReferences"
        res = db_connection.execute(query).fetchall()
        return res

    def get_all_from_articleref(self):
        db_connection=self._connection2.cursor()
        query = "SELECT * FROM AReferences"
        res = db_connection.execute(query).fetchall()
        return res

    def get_all_from_inproref(self):
        db_connection=self._connection3.cursor()
        query = "SELECT * FROM IReferences"
        res = db_connection.execute(query).fetchall()
        return res

    def find_key_from_bookref(self, key):
        db_connection=self._connection1.cursor()
        query = f"SELECT dbkey FROM BReferences WHERE dbkey={key}"
        exist=db_connection.execute(query).fetchall()
        if len(exist)!=0:
            return False
        return True

    def search_book_by_title(self, title):
        db_connection=self._connection1.cursor()
        db_connection.execute("SELECT * FROM BReferences WHERE title=?", (title,))
        res = db_connection.fetchall()
        return res

    def search_article_by_title(self, title):
        db_connection=self._connection2.cursor()
        db_connection.execute("SELECT * FROM AReferences WHERE title=?", (title,))
        res = db_connection.fetchall()
        return res

    def search_inpro_by_title(self, title):
        db_connection=self._connection3.cursor()
        db_connection.execute("SELECT * FROM IReferences WHERE title=?", (title,))
        res = db_connection.fetchall()
        return res

    def search_book_by_author(self, author):
        db_connection=self._connection1.cursor()
        db_connection.execute("SELECT * FROM BReferences WHERE author=?", (author,))
        res = db_connection.fetchall()
        return res

    def search_article_by_author(self, author):
        db_connection=self._connection2.cursor()
        db_connection.execute("SELECT * FROM AReferences WHERE author=?", (author,))
        res = db_connection.fetchall()
        return res

    def search_inpro_by_author(self, author):
        db_connection=self._connection3.cursor()
        db_connection.execute("SELECT * FROM IReferences WHERE author=?", (author,))
        res = db_connection.fetchall()
        return res

    def search_book_by_author_and_title(self, author, title):
        db_connection=self._connection1.cursor()
        db_connection.execute("SELECT * FROM BReferences WHERE author=? AND title=?", \
                             (author, title))
        res = db_connection.fetchall()
        return res

    def search_article_by_author_and_title(self, author, title):
        db_connection=self._connection2.cursor()
        db_connection.execute("SELECT * FROM AReferences WHERE author=? AND title=?", \
                             (author, title))
        res = db_connection.fetchall()
        return res

    def search_inpro_by_author_and_title(self, author, title):
        db_connection=self._connection3.cursor()
        db_connection.execute("SELECT * FROM IReferences WHERE author=? AND title=?", \
                             (author, title))
        res = db_connection.fetchall()
        return res

    def delete_all_references(self):
        self._connection1.cursor().execute("DROP TABLE BReferences")
        self._connection2.cursor().execute("DROP TABLE AReferences")
        self._connection3.cursor().execute("DROP TABLE IReferences")
        build()

    def get_all_citekeys(self):
        book_keys = self._connection1.cursor().execute("SELECT dbkey from BReferences").fetchall()
        art_keys = self._connection2.cursor().execute("SELECT dbkey from AReferences").fetchall()
        inpro_keys = self._connection3.cursor().execute("SELECT dbkey from IReferences").fetchall()

        return {
            "book": book_keys,
            "article": art_keys,
            "inproceedings": inpro_keys
        }

    def delete_book_reference(self, key):
        self._connection1.cursor().execute("DELETE FROM BReferences WHERE dbkey=?", key)

    def delete_article_reference(self, key):
        self._connection1.cursor().execute("DELETE FROM AReferences WHERE dbkey=?", key)

    def delete_inproceedings_reference(self, key):
        self._connection1.cursor().execute("DELETE FROM IReferences WHERE dbkey=?", key)


refe_interface=StorageInterface(
    get_bookref_connection(),get_aref_connection(),get_iref_connection()
)
