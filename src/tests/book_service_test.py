import unittest
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services

class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book = ReferencesRepository()
        self.reference_service = Services(self.book)
        self.reference_service.config_reference(
            "Operating Systems", ['Stallings'], "MacMillan", 1991, 682, 1, "100-107", 10, "")

    def test_service_can_set_book_reference(self):
        self.assertEqual(self.book.title, "Operating Systems")
        self.assertEqual(self.book.author[0], "Stallings")
        self.assertEqual(self.book.publisher, "MacMillan")
        self.assertEqual(self.book.year, 1991)
        self.assertEqual(self.book.volume, 682)
        self.assertEqual(self.book.number, 1)
        self.assertEqual(self.book.pages, "100-107")
        self.assertEqual(self.book.note, "")

    def test_service_returns_book_reference_correctly(self):
        self.assertEqual(
            self.reference_service.return_book(),
            "Operating Systems, ['Stallings'], MacMillan, 1991, 682, 1, 100-107, 10, ")
