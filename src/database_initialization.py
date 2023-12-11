from database_connection import get_bookref_connection
from database_connection import get_aref_connection
from database_connection import get_iref_connection

def create_book_references(get):
    db_connection=get.cursor()

    db_connection.execute(
        """CREATE TABLE IF NOT EXISTS BReferences (
            dbkey TEXT PRIMARY KEY,
            author TEXT,
            title TEXT,
            publisher TEXT,
            year INTEGER,
            volume INTEGER,
            number INTEGER,
            pages TEXT,
            month INTEGER,
            note TEXT
        );"""
    )
    get.commit()

def create_article_references(get):
    db_connection=get.cursor()

    db_connection.execute(
        """CREATE TABLE IF NOT EXISTS AReferences (
            dbkey TEXT PRIMARY KEY,
            author TEXT,
            title TEXT,
            journal TEXT,
            year INTEGER,
            volume INTEGER,
            number INTEGER,
            pages TEXT,
            month INTEGER,
            note TEXT
        );"""
    )
    get.commit()

def create_inproceedings_references(get):
    db_connection=get.cursor()
    db_connection.execute(
        """CREATE TABLE IF NOT EXISTS IReferences (
            dbkey TEXT PRIMARY KEY,
            author TEXT,
            title TEXT,
            booktitle TEXT,
            year INTEGER,
            editor TEXT,
            volume INTEGER,
            number INTEGER,
            series TEXT,
            pages TEXT,
            address TEXT,
            month INTEGER,
            organization TEXT,
            publisher TEXT,
            note TEXT
        );"""
    )
    get.commit()

def initialize_database():
    get = get_bookref_connection()
    get1 = get_aref_connection()
    get2=get_iref_connection()
    create_book_references(get)
    create_article_references(get1)
    create_inproceedings_references(get2)
