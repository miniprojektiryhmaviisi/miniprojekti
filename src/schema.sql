CREATE TABLE IF NOT EXISTS BReferences (
    dbkey TEXT PRIMARY KEY,
    author TEXT,
    title TEXT,
    publisher TEXT,
    year INTEGER,
    volume INTEGER,
    number INTEGER,
    pages TEXT,
    month INTEGER   ,
    note TEXT
);

CREATE TABLE IF NOT EXISTS AReferences (
    dbkey TEXT PRIMARY KEY,
    author TEXT,
    title TEXT,
    journal TEXT,
    year INTEGER,
    volume INTEGER,
    number INTEGER,
    pages TEXT,
    month INTEGER   ,
    note TEXT
);

CREATE TABLE IF NOT EXISTS IReferences (
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
);