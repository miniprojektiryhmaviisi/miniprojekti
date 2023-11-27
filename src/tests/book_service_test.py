import unittest
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services

class TestBookService(unittest.TestCase):
    def setUp(self):
        self.bookref = ReferencesRepository()
        self.reference_service = Services(self.bookref)
        self.reference_service.config_book_reference(
            "somekey", "Operating Systems", ['Stallings'], "MacMillan", 1991, 682, 1, "100-107", 10, "")

    def test_service_can_set_book_reference(self):
        self.assertEqual(self.bookref.key, "somekey")
        self.assertEqual(self.bookref.title, "Operating Systems")
        self.assertEqual(self.bookref.author[0], "Stallings")
        self.assertEqual(self.bookref.publisher, "MacMillan")
        self.assertEqual(self.bookref.year, 1991)
        self.assertEqual(self.bookref.volume, 682)
        self.assertEqual(self.bookref.number, 1)
        self.assertEqual(self.bookref.pages, "100-107")
        self.assertEqual(self.bookref.note, "")

    # def test_service_returns_book_reference_correctly(self):
    #     self.assertEqual(
    #         self.reference_service.return_book(),
    #         "somekey, Operating Systems, ['Stallings'], MacMillan, 1991, 682, 1, 100-107, 10")
