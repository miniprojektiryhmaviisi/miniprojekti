class StorageInterface:
    def __init__(self, db):
        self.db = db

    def store_bookref(self, bookref):
        query = f"INSERT INTO BReferences VALUES \
                ({bookref.key}, {bookref.author}, {bookref.title}, \
                {bookref.publisher}, {bookref.year}, \
                {bookref.volume}, {bookref.number}, \
                {bookref.pages}, {bookref.month}, \
                {bookref.note})"
        self.db.execute(query)
        self.db.commit()

    def store_articleref(self, articleref):
        query = f"INSERT INTO BReferences VALUES \
                ({articleref.key}, {articleref.author}, {articleref.title}, \
                {articleref.journal}, {articleref.year}, \
                {articleref.volume}, {articleref.number}, \
                {articleref.pages}, {articleref.month}, \
                {articleref.note})"
        self.db.execute(query)
        self.db.commit()

    def store_inproref(self, inproref):
        query = f"INSERT INTO BReferences VALUES \
                ({inproref.key}, {inproref.author}, {inproref.title}, \
                {inproref.booktitle}, {inproref.year}, \
                {inproref.editor}, {inproref.volume}, \
                {inproref.number}, {inproref.series}, \
                {inproref.pages}, {inproref.address}, \
                {inproref.month}, {inproref.organization}, \
                {inproref.publisher}, {inproref.note})"
        self.db.execute(query)
        self.db.commit()

    def get_all(self):
        query = "SELECT * FROM BReferences, AReferences, IReferences"
        res = self.db.execute(query).fetchall()
        return res
