from .database_connection import (create_db_dirs,
                                 get_bookref_connection,
                                 get_aref_connection,
                                 get_iref_connection)

from .config import (DATABASE_FILE_PATH,
                    DATABASE_FILE_PATH1,
                    DATABASE_FILE_PATH2)


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
    create_db_dirs(DATABASE_FILE_PATH, DATABASE_FILE_PATH1, DATABASE_FILE_PATH2)
    get = get_bookref_connection()
    get1 = get_aref_connection()
    get2 = get_iref_connection()
    create_book_references(get)
    create_article_references(get1)
    create_inproceedings_references(get2)
