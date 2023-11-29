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
        self.refrepo = ReferencesRepository()
        self.reference_service = Services(self.refrepo)
        self.database_interface_mock = Mock()
        self.reference_service.database_interface = self.database_interface_mock

    @patch('references.sleep')
    def test_user_can_add_book_reference_with_correct_input(self, mock_sleep):
        mock_sleep.return_value = None
        io_handler = StubIO(
            ["0", "A", "somekey", "Operating Systems", "Stallings", "", "MacMillan", "1991", "", "",
             "", "", "", "2"]
            )
        reference_service_mock = Mock()

        self.assertEqual(reference_service_mock.config_book_reference.call_count, 0)
        References(io_handler, reference_service_mock)
        self.assertEqual(reference_service_mock.config_book_reference.call_count, 1)
        
    @patch('references.sleep')
    def test_user_can_add_article_reference_with_correct_input(self, mock_sleep):
        mock_sleep.return_value = None
        io_handler = StubIO(
            ["0", "B", "somekey", "testtitle", "testauthor", "", "testjournal", "1991", "700", "1",
             "105-108", "10", "testnote", "2"]
            )
        reference_service_mock = Mock()

        self.assertEqual(reference_service_mock.config_article_reference.call_count, 0)
        References(io_handler, reference_service_mock)
        self.assertEqual(reference_service_mock.config_article_reference.call_count, 1)

    @patch('references.sleep')
    def test_user_can_add_inproceedings_reference_with_correct_input(self, mock_sleep):
        mock_sleep.return_value = None
        io_handler = StubIO(
            ["0", "C", "somekey", "testtitle", "testbooktitle", "testauthor", "", "2023", "testeditor",
             "700", "1", "1", "105-108", "testaddress", "2", "testorganization", "testpublisher",
             "testnote", "2"]
            )
        reference_service_mock = Mock()

        self.assertEqual(reference_service_mock.config_inpro_reference.call_count, 0)
        References(io_handler, reference_service_mock)
        self.assertEqual(reference_service_mock.config_inpro_reference.call_count, 1)
    
    @patch('references.sleep')
    def test_user_has_to_enter_all_non_optional_information(self, mock_sleep):
        mock_sleep.return_value = None
        io_handler = StubIO(
            ["0", "A", "somekey", "", "Operating Systems", "", "Stallings", "", "", "MacMillan", "",
             "1991", "", "", "", "", "", "2", "2"]
            )
        References(io_handler, self.reference_service)
        
        self.assertEqual(
            io_handler.outputs.count("Field cannot be empty. Please provide a valid input."),
            4
            )

    @patch('references.sleep')
    def test_user_can_add_multiple_authors(self, mock_sleep):
        mock_sleep.return_value = None
        io_handler = StubIO(
            ["0", "A", "somekey", "Operating Systems", "Stallings", "William", "Jarmo", "",
             "MacMillan", "1991", "", "", "", "", "", "2"]
            )
        References(io_handler, self.reference_service)

        first_author, second_author, third_author = self.refrepo.author
        self.assertEqual(first_author, "Stallings")
        self.assertEqual(second_author, "William")
        self.assertEqual(third_author, "Jarmo")

    @patch('references.sleep')
    def test_user_can_view_all_references(self, mock_sleep):
        mock_sleep.return_value = None
        self.database_interface_mock.get_all_from_bookref.return_value = [[
            "bookkey", "bookauthor", "booktitle", "bookpubliser", 2023, 800, 1,
            "100-101", 5, "booknote"
        ]]
        self.database_interface_mock.get_all_from_articleref.return_value = [[
            "articlekey", "articleauthor", "articletitle", "articlejournal", 2024, 900, 2,
            "102-103", 6, "articlenote"
        ]]
        self.database_interface_mock.get_all_from_inproref.return_value = [[
            "inprokey", "inproauthor", "inprotitle", "inprobooktitle", 2025, "inproeditor", 1000, 3, 1, "103-104",
            "inproaddress", 7, "inproorganization", "inpropublisher", "inpronote"
        ]]
        io_handler = StubIO(
            ["1", "2"]
            )
        References(io_handler, self.reference_service)
        
        self.assertEqual(io_handler.outputs.count("Cite Key   : bookkey"), 1)
        self.assertEqual(io_handler.outputs.count("Cite Key   : articlekey"), 1)
        self.assertEqual(io_handler.outputs.count("Cite Key   : inprokey"), 1)
