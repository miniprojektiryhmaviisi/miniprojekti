from db_config.database_connection import get_bookref_connection
from db_config.database_connection import get_aref_connection
from db_config.database_connection import get_iref_connection
from db_config.database_initialization import initialize_database

class StorageInterface:
    def __init__(self, connection1,connection2,connection3):
        self._connection1=connection1
        self._connection2=connection2
        self._connection3=connection3

    def reset_test_data(self):
        self.delete_all_references()
        try:
            rows = [
                ("wilson_data", "Wilson", "The Art of Data", "NextGen Publishers", "2019", "4",
                 "10", "297--303", "5", ""),
                ("brown_demystified", "Brown", "Data Science Demystified", "TechBooks Publishing",
                 "2020", "4", "4", "198--200", "2", ""),
                ("emberson_practice", "Emberson", "Python in Practice", "NextGen Publishers",
                 "2022", "4", "6", "568--569", "9", ""),
                ("brown_automating", "Brown", "Automating with Python", "CodeHouse", "2020", "4",
                 "9", "560", "1", ""),
                ("daniels_solutions", "Daniels", "Reliable IT Solutions", "TechBooks Publishing",
                 "2020", "1", "9", "497--501", "8", "")
            ]
            db_connection=self._connection1.cursor()
            db_connection.executemany("INSERT INTO BReferences\
            (dbkey,author,title,publisher,year,volume,number,pages,month,note) \
            VALUES (?,?,?,?,?,?,?,?,?,?)",rows)

            rows = [
                ("miller_analysis", "Miller", "Data Analysis Techniques",
                 "Science and Technology Review", "1990", "3", "7", "5--14", "6", ""),
                ("brown_sustainable", "Brown", "Sustainable IT Solutions", "Journal of Computing",
                 "2001", "3", "3", "70--73", "9", ""),
                ("miller_ml", "Miller", "Advancements in Machine Learning",
                 "Information Technology Today", "2001", "6", "16", "56--66", "1", ""),
                ("jones_protocols", "Jones", "Network Security Protocols", "Future of IT", "1991",
                 "10", "15", "74--90", "2", ""),
                ("davis_ml", "Davis", "Threats in Machine Learning", "Tech Innovations", "1994",
                 "18", "5", "20--30", "8", "")
            ]
            db_connection=self._connection2.cursor()
            db_connection.executemany("INSERT INTO AReferences\
            (dbkey,author,title,journal,year,volume,number,pages,month,note) \
            VALUES (?,?,?,?,?,?,?,?,?,?)", rows)

            rows = [
                ("davis_blockchain", "Davis", "Blockchain Revolution",
                "Proceedings of the 10th International Conference on Technology", "2017", "Anderson",
                  "10", "1", "Emerging Trends in IT", "268--271", "Sydney", "4",
                  "Foundation for IT Advancement", "Future Tech Books", ""),
                ("merryb_quantum", "Merrybottom", "Advances in Quantum Computing",
                 "International Workshop on Blockchain", "2011", "White", "7", "7",
                 "Advances in Technology", "243--245", "Sydney", "8", "Global Tech Symposium",
                 "Innovations Inc.", ""),
                ("johnson_iot", "Johnson", "Innovations in IoT",
                 "Proceedings of the 10th International Conference on Technology",
                 "2001", "Anderson", "5", "10", "Innovations in Engineering", "68--69", "Tokyo",
                 "10", "Network of Tech Academics", "Tech Press", ""),
                ("garcia_today", "Garcia", "Cybersecurity Today", "Tech Trends in the 21st Century",
                 "1993", "Moore", "8", "2", "Advances in Technology", "98--102", "Berlin", "9",
                 "International Technology Association", "Cloud Computing Publications", ""),
                ("roberts_beginners", "Roberts", "Deep Learning for Beginners",
                 "International Workshop on Blockchain", "2011", "Jackson", "4", "8",
                 "Critical Reviews in Computing", "196--207", "Sydney", "11",
                 "Society for AI Innovations", "Cloud Computing Publications", "")
            ]
            db_connection=self._connection3.cursor()
            db_connection.executemany("INSERT INTO IReferences\
            (dbkey,author,title,booktitle,year,editor,volume,number,series,pages,\
            address,month,organization,publisher,note)\
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
        except Exception as exc:
            raise exc
        self._connection1.commit()
        self._connection3.commit()
        self._connection2.commit()

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
        initialize_database()

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


def get_interface():
    initialize_database()
    return StorageInterface(
        get_bookref_connection(),get_aref_connection(),get_iref_connection()
    )
