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
        try:
            self.storage_interface.store_articleref(mock_articleref)
        except Exception as exc:
            self.fail(f"store_articleref failed with exception: {exc}")

        self.mock_connection2.cursor().execute.assert_called_once_with("INSERT INTO AReferences\
            (dbkey,author,title,journal,year,volume,number,pages,month,note) \
            VALUES (?,?,?,?,?,?,?,?,?,?)",("mock_key1", "Author",  \
            "Mock Title", "MockPublisher1", 2023, 1,  \
            1, "1-10", "January", "Mock Note"))


        self.mock_connection2.commit.assert_called_once()
        query = f"SELECT * FROM AReferences WHERE dbkey='mock_key1'"
        result = self.mock_connection2.cursor().execute(query).fetchone()

        self.assertIsNotNone(result)

    def test_store_inproref(self):

        mock_inproref = Mock(
            key="mock_key2", author=["Author"], title="Mock Title", booktitle="MockPublisher1",
            year=2023, editor="hddhd",volume=1, number=1,series=7, pages="1-10",address=3, month="January",organization="xx",publisher="dd", note="Mock Note"
        )

        self.storage_interface.store_inproref(mock_inproref)

        self.mock_connection3.cursor().execute.assert_called_once_with("INSERT INTO IReferences\
            (dbkey,author,title,booktitle,year,editor,volume,number,series,pages,\
            address,month,organization,publisher,note)\
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",("mock_key2", "Author",\
            "Mock Title", "MockPublisher1", 2023,"hddhd",\
            1,1,7, "1-10",\
            3,"January","xx",\
            "dd", "Mock Note"))


        self.mock_connection3.commit.assert_called_once()


        query = f"SELECT * FROM IReferences WHERE dbkey='mock_key1'"
        result = self.mock_connection3.cursor().execute(query).fetchone()

        self.assertIsNotNone(result)

    def test_store_articleref_failure(self):
        mock_articleref = Mock(
            key="mock_key2", author=["Author"], title="Mock Title", journal="MockPublisher1",
            year=2023, volume=1, number=1, pages="1-10", month="January", note="Mock Note"
        )


        self.mock_connection2.cursor().execute.side_effect = Exception("Test exception")


        with self.assertRaises(Exception):
            self.storage_interface.store_articleref(mock_articleref)


        self.mock_connection2.commit.assert_not_called()
    def test_store_inproref_failure(self):
        mock_inproref = Mock(
            key="mock_key2", author=["Author"], title="Mock Title", booktitle="MockPublisher1",
            year=2023, editor="hddhd",volume=1, number=1,series=7, pages="1-10",address=3, month="January",organization="xx",publisher="dd", note="Mock Note"
        )


        self.mock_connection3.cursor().execute.side_effect = Exception("Test exception")



        with self.assertRaises(Exception):
            self.storage_interface.store_inproref(mock_inproref)


        self.mock_connection3.commit.assert_not_called()
