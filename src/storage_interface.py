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
        author_field = self.stringify_list(bookref.author)
        try:
            db_connection.execute("INSERT INTO BReferences\
            (dbkey,author,title,publisher,year,volume,number,pages,month,note) \
            VALUES (?,?,?,?,?,?,?,?,?,?)",(bookref.key,author_field,\
            bookref.title,bookref.publisher,bookref.year,bookref.volume,\
            bookref.number,bookref.pages,bookref.month,bookref.note))
        except Exception as exc:
            raise exc
        self._connection1.commit()

    def store_articleref(self, articleref):
        db_connection=self._connection2.cursor()
        author_field = self.stringify_list(articleref.author)
        try:
            db_connection.execute("INSERT INTO AReferences\
            (dbkey,author,title,journal,year,volume,number,pages,month,note) \
            VALUES (?,?,?,?,?,?,?,?,?,?)",(articleref.key,author_field,\
            articleref.title,articleref.journal,articleref.year,articleref.volume,\
            articleref.number,articleref.pages,articleref.month,articleref.note))
        except Exception as exc:
            raise exc
        self._connection2.commit()

    def store_inproref(self, inproref):
        db_connection=self._connection3.cursor()
        author_field = self.stringify_list(inproref.author)
        try:
            db_connection.execute("INSERT INTO IReferences\
            (dbkey,author,title,booktitle,year,editor,volume,number,series,pages,\
            address,month,organization,publisher,note)\
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(inproref.key,author_field,\
            inproref.title,inproref.booktitle,inproref.year,inproref.editor,\
            inproref.volume,inproref.number,inproref.series,inproref.pages,\
            inproref.address,inproref.month,inproref.organization,\
            inproref.publisher,inproref.note))
        except Exception as exc:
            raise exc
        self._connection3.commit()

    def get_all_from_bookref(self):
        db_connection=self._connection1.cursor()
        query = "SELECT * FROM BReferences ORDER BY author ASC"
        res = db_connection.execute(query).fetchall()
        return res

    def get_all_from_articleref(self):
        db_connection=self._connection2.cursor()
        query = "SELECT * FROM AReferences ORDER BY author ASC"
        res = db_connection.execute(query).fetchall()
        return res

    def get_all_from_inproref(self):
        db_connection=self._connection3.cursor()
        query = "SELECT * FROM IReferences ORDER BY author ASC"
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
        db_connection.execute("SELECT * FROM BReferences WHERE title LIKE ?", ('%' + title + '%',))
        res = db_connection.fetchall()
        return res

    def search_article_by_title(self, title):
        db_connection=self._connection2.cursor()
        db_connection.execute("SELECT * FROM AReferences WHERE title LIKE ?", ('%' + title + '%',))
        res = db_connection.fetchall()
        return res

    def search_inpro_by_title(self, title):
        db_connection=self._connection3.cursor()
        db_connection.execute("SELECT * FROM IReferences WHERE title LIKE ?", ('%' + title + '%',))
        res = db_connection.fetchall()
        return res

    def search_book_by_author(self, author):
        db_connection=self._connection1.cursor()
        db_connection.execute("SELECT * FROM BReferences WHERE author LIKE ?", ('%' + author + '%',))
        res = db_connection.fetchall()
        return res

    def search_article_by_author(self, author):
        db_connection=self._connection2.cursor()
        db_connection.execute("SELECT * FROM AReferences WHERE author LIKE ?", ('%' + author + '%',))
        res = db_connection.fetchall()
        return res

    def search_inpro_by_author(self, author):
        db_connection=self._connection3.cursor()
        db_connection.execute("SELECT * FROM IReferences WHERE author LIKE ?", ('%' + author + '%',))
        res = db_connection.fetchall()
        return res

    def search_book_by_author_and_title(self, author, title):
        db_connection=self._connection1.cursor()
        db_connection.execute("SELECT * FROM BReferences WHERE author LIKE ? AND title LIKE ?", \
                             ('%' + author + '%', '%' + title + '%'))
        res = db_connection.fetchall()
        return res

    def search_article_by_author_and_title(self, author, title):
        db_connection=self._connection2.cursor()
        db_connection.execute("SELECT * FROM AReferences WHERE author LIKE ? AND title LIKE ?", \
                             ('%' + author + '%', '%' + title + '%'))
        res = db_connection.fetchall()
        return res

    def search_inpro_by_author_and_title(self, author, title):
        db_connection=self._connection3.cursor()
        db_connection.execute("SELECT * FROM IReferences WHERE author LIKE ? AND title LIKE ?", \
                             ('%' + author + '%', '%' + title + '%'))
        res = db_connection.fetchall()
        return res

    def delete_all_references(self):
        self._connection1.cursor().execute("DROP TABLE BReferences")
        self._connection2.cursor().execute("DROP TABLE AReferences")
        self._connection3.cursor().execute("DROP TABLE IReferences")
        self._connection1.commit()
        self._connection2.commit()
        self._connection3.commit()
        build()

    def get_all_citekeys(self):
        book_keys = []
        for i in self._connection1.cursor().execute("SELECT dbkey from BReferences").fetchall():
            book_keys.append(i[0])
        art_keys = []
        for i in self._connection2.cursor().execute("SELECT dbkey from AReferences").fetchall():
            art_keys.append(i[0])
        inpro_keys = []
        for i in self._connection3.cursor().execute("SELECT dbkey from IReferences").fetchall():
            inpro_keys.append(i[0])

        return {
            "book": book_keys,
            "article": art_keys,
            "inproceedings": inpro_keys
        }

    def delete_book_reference(self, key):
        self._connection1.cursor().execute("DELETE FROM BReferences WHERE dbkey=(?)", (key,))
        self._connection1.commit()

    def delete_article_reference(self, key):
        self._connection2.cursor().execute("DELETE FROM AReferences WHERE dbkey=(?)", (key,))
        self._connection2.commit()

    def delete_inproceedings_reference(self, key):
        self._connection3.cursor().execute("DELETE FROM IReferences WHERE dbkey=(?)", (key,))
        self._connection3.commit()

    def stringify_list(self, author_list):
        last_index = len(author_list) - 1
        if len(author_list) == 1:
            return author_list[0]
        returning_string = author_list[0]
        index = 1
        while True:
            returning_string += " and " + author_list[index]
            if index == last_index:
                return returning_string
            index += 1

refe_interface=StorageInterface(
    get_bookref_connection(),get_aref_connection(),get_iref_connection()
)
