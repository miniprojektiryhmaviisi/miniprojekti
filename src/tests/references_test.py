import unittest
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services
from references import References
from unittest.mock import Mock, ANY, patch

class StubIO:
    def __init__(self, inputs=[]):
        self.inputs = inputs
        self.outputs = []

    def read(self, message):
        return self.inputs.pop(0)

    def write(self, message):
        self.outputs.append(message)

    def add_input(self, value):
        self.inputs.append(value)

class TestReferences(unittest.TestCase):
    def setUp(self):
        self.book = ReferencesRepository()
        self.storage_interface = Mock()
        self.reference_service = Services(self.book, self.storage_interface)

    # poistaa sleep-metodin aiheuttama paussi
    @patch('references.sleep')
    def test_user_can_add_book_reference_with_correct_input(self, mock_sleep):
        mock_sleep.return_value = None
        io_handler = StubIO(
            ["0", "A", "somekey", "Operating Systems", "Stallings", "", "MacMillan", "1991", "", "", "", "", "", "2"]
            )
        reference_service_mock = Mock()

        self.assertEqual(reference_service_mock.config_book_reference.call_count, 0)
        References(io_handler, reference_service_mock, None)
        self.assertEqual(reference_service_mock.config_book_reference.call_count, 1)
    
    @patch('references.sleep')
    def test_user_has_to_enter_all_non_optional_information(self, mock_sleep):
        mock_sleep.return_value = None
        io_handler = StubIO(
            ["0", "A", "somekey", "", "Operating Systems", "", "Stallings", "", "", "MacMillan", "", "1991", "", "", "", "", "", "2", "2"]
            )
        References(io_handler, self.reference_service, None)
        
        self.assertEqual(
            io_handler.outputs.count("Field cannot be empty. Please provide a valid input."),
            4
            )

    @patch('references.sleep')
    def test_user_can_add_multiple_authors(self, mock_sleep):
        mock_sleep.return_value = None
        io_handler = StubIO(
            ["0", "A", "somekey", "Operating Systems", "Stallings", "William", "Jarmo", "", "MacMillan", "1991", "", "", "", "", "", "2"]
            )
        References(io_handler, self.reference_service, None)

        first_author, second_author, third_author = self.book.author
        self.assertEqual(first_author, "Stallings")
        self.assertEqual(second_author, "William")
        self.assertEqual(third_author, "Jarmo")

        