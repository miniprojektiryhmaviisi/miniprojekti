from database_connection import get_bookref_connection
from database_connection import get_aref_connection
from database_connection import get_iref_connection

def create_book_references(get):
    db_connection=get.cursor()

    db_connection.execute(
        f"CREATE TABLE IF NOT EXISTS BReferences ("
        f"    dbkey TEXT PRIMARY KEY,"
        f"    author TEXT,"
        f"    title TEXT,"
        f"    publisher TEXT,"
        f"    year INTEGER,"
        f"    volume INTEGER,"
        f"    number INTEGER,"
        f"    pages TEXT,"
        f"    month INTEGER   ,"
        f"    note TEXT"
        f");"
    )
    get.commit()

def create_article_references(get):
    db_connection=get.cursor()

    db_connection.execute(
        f"CREATE TABLE IF NOT EXISTS AReferences ("
        f"dbkey TEXT PRIMARY KEY,"
        f"author TEXT,"
        f"title TEXT,"
        f"journal TEXT,"
        f"year INTEGER,"
        f"volume INTEGER,"
        f"number INTEGER,"
        f"pages TEXT,"
        f"month INTEGER   ,"
        f"note TEXT"
        f");"
    )
    get.commit()

def create_inproceedings_references(get):
    db_connection=get.cursor()
    db_connection.execute(
        f"CREATE TABLE IF NOT EXISTS IReferences ("
        f"dbkey TEXT PRIMARY KEY,"
        f"author TEXT,"
        f"title TEXT,"
        f"booktitle TEXT,"
        f"year INTEGER,"
        f"editor TEXT,"
        f"volume INTEGER,"
        f"number INTEGER,"
        f"series TEXT,"
        f"pages TEXT,"
        f"address TEXT,"
        f"month INTEGER,"
        f"organization TEXT,"
        f"publisher TEXT,"
        f"note TEXT"
        f");"
    )
    get.commit()

def initialize_database():
    get = get_bookref_connection()
    get1 = get_aref_connection()
    get2=get_iref_connection()
    create_book_references(get)
    create_article_references(get1)
    create_inproceedings_references(get2)
