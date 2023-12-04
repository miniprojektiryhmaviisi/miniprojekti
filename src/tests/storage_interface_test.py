import unittest
from unittest.mock import Mock
from storage_interface import StorageInterface  # Replace 'your_module' with the actual module name

class TestStorageInterface(unittest.TestCase):
    def setUp(self):
        # Create mock connections
        self.mock_connection1 = Mock()
        self.mock_connection2 = Mock()
        self.mock_connection3 = Mock()

        # Create StorageInterface instance with mock connections
        self.storage_interface = StorageInterface(
            self.mock_connection1, self.mock_connection2, self.mock_connection3
        )

    def test_store_bookref(self):
        # Create a mock book reference
        mock_bookref = Mock(
            key="mock_key", author=["Author"], title="Mock Title", publisher="Mock Publisher",
            year=2023, volume=1, number=1, pages="1-10", month="January", note="Mock Note"
        )

        # Call the method to store the mock book reference
        self.storage_interface.store_bookref(mock_bookref)

        # Assert that the execute method was called on the mock connection
        self.mock_connection1.cursor().execute.assert_called_once_with("INSERT INTO BReferences\
            (dbkey,author,title,publisher,year,volume,number,pages,month,note) \
            VALUES (?,?,?,?,?,?,?,?,?,?)",("mock_key", "Author",\
            "Mock Title", "Mock Publisher", 2023, 1,\
            1, "1-10", "January", "Mock Note"))

        # Assert that commit was called on the mock connection
        self.mock_connection1.commit.assert_called_once()

        # Query the database to check if the data was stored
        query = f"SELECT * FROM BReferences WHERE dbkey='mock_key'"
        result = self.mock_connection1.cursor().execute(query).fetchone()

        # Assert that the result is not None, indicating that the data was stored
        self.assertIsNotNone(result)


