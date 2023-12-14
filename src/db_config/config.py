import os

dirname = os.path.dirname(__file__)
print(__file__)

DATABASE_FILENAME = "bookrefdatabase.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

DATABASE_FILENAME1  = "arefdatabase.sqlite"
DATABASE_FILE_PATH1 = os.path.join(dirname, "..", "data", DATABASE_FILENAME1)

DATABASE_FILENAME2  = "irefdatabase.sqlite"
DATABASE_FILE_PATH2 = os.path.join(dirname, "..", "data", DATABASE_FILENAME2)
