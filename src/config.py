import os
# from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

# try:
#     load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
# except FileNotFoundError:
#     pass

DATABASE_FILENAME = "bookrefdatabase.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

DATABASE_FILENAME1  = "arefdatabase.sqlite"
DATABASE_FILE_PATH1 = os.path.join(dirname, "..", "data", DATABASE_FILENAME1)

DATABASE_FILENAME2  = "irefdatabase.sqlite"
DATABASE_FILE_PATH2 = os.path.join(dirname, "..", "data", DATABASE_FILENAME2)
