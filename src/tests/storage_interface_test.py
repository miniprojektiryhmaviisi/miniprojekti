import unittest
from unittest.mock import Mock
from storage_interface import StorageInterface  # Replace 'your_module' with the actual module name

class TestStorageInterface(unittest.TestCase):
    def setUp(self):
        self.mock_connection1 = Mock()
        self.mock_connection2 = Mock()
        self.mock_connection3 = Mock()

        self.storage_interface = StorageInterface(
            self.mock_connection1, self.mock_connection2, self.mock_connection3
        )

    def test_store_bookref(self):
        mock_bookref = Mock(
            key="mock_key", author=["Author"], title="Mock Title", publisher="Mock Publisher",
            year=2023, volume=1, number=1, pages="1-10", month="January", note="Mock Note"
        )

        self.storage_interface.store_bookref(mock_bookref)

        self.mock_connection1.cursor().execute.assert_called_once_with("INSERT INTO BReferences\
            (dbkey,author,title,publisher,year,volume,number,pages,month,note) \
            VALUES (?,?,?,?,?,?,?,?,?,?)",("mock_key", "Author",\
            "Mock Title", "Mock Publisher", 2023, 1,\
            1, "1-10", "January", "Mock Note"))


        self.mock_connection1.commit.assert_called_once()


        query = f"SELECT * FROM BReferences WHERE dbkey='mock_key'"
        result = self.mock_connection1.cursor().execute(query).fetchone()

        self.assertIsNotNone(result)

    def test_store_articleref(self):

        mock_articleref = Mock(
            key="mock_key1", author=["Author"], title="Mock Title", journal="MockPublisher1",
            year=2023, volume=1, number=1, pages="1-10", month="January", note="Mock Note"
        )

        self.storage_interface.store_articleref(mock_articleref)

        self.mock_connection2.cursor().execute.assert_called_once_with("INSERT INTO AReferences\
            (dbkey,author,title,journal,year,volume,number,pages,month,note) \
            VALUES (?,?,?,?,?,?,?,?,?,?)",("mock_key1", "Author",  \
            "Mock Title", "MockPublisher1", 2023, 1,  \
            1, "1-10", "January", "Mock Note"))


        self.mock_connection2.commit.assert_called_once()


        query = f"SELECT * FROM AReferences WHERE dbkey='mock_key1'"
        result = self.mock_connection2.cursor().execute(query).fetchone()

        self.assertIsNotNone(result)

