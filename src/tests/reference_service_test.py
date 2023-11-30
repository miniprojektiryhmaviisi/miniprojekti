import unittest
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services

class TestService(unittest.TestCase):
    def setUp(self):
        self.refrepo = ReferencesRepository()
        self.storage_interface = unittest.mock.Mock()
        self.reference_service = Services(self.refrepo)
        self.reference_service.database_interface = unittest.mock.Mock()

    def test_service_can_set_book_reference(self):
        self.reference_service.config_book_reference(
            "somekey", "Operating Systems", ['Stallings'], "MacMillan", 1991, 682, 1, "100-107", 10, "")

        self.assertEqual(self.refrepo.key, "somekey")
        self.assertEqual(self.refrepo.title, "Operating Systems")
        self.assertEqual(self.refrepo.author[0], "Stallings")
        self.assertEqual(self.refrepo.publisher, "MacMillan")
        self.assertEqual(self.refrepo.year, 1991)
        self.assertEqual(self.refrepo.volume, 682)
        self.assertEqual(self.refrepo.number, 1)
        self.assertEqual(self.refrepo.pages, "100-107")
        self.assertEqual(self.refrepo.note, "")

    def test_service_can_set_article_reference(self):
        self.reference_service.config_article_reference(
            "testkey", "testtitle", ['testauthor'], "testjournal", 2023, 900, 1, "100-107", 1, "")

        self.assertEqual(self.refrepo.key, "testkey")
        self.assertEqual(self.refrepo.title, "testtitle")
        self.assertEqual(self.refrepo.author[0], "testauthor")
        self.assertEqual(self.refrepo.journal, "testjournal")
        self.assertEqual(self.refrepo.year, 2023)
        self.assertEqual(self.refrepo.volume, 900)
        self.assertEqual(self.refrepo.number, 1)
        self.assertEqual(self.refrepo.pages, "100-107")
        self.assertEqual(self.refrepo.note, "")
    
    def test_service_can_set_inpro_reference(self):
        self.reference_service.config_inpro_reference(
            "testkey", "testtitle", "testbooktitle", ['testauthor'], 2023, "testeditor",
            700, 1, 1, "108-110", "testaddress", 10, "testorganization", "testpublisher", "testnotes")

        self.assertEqual(self.refrepo.key, "testkey")
        self.assertEqual(self.refrepo.title, "testtitle")
        self.assertEqual(self.refrepo.booktitle, "testbooktitle")
        self.assertEqual(self.refrepo.author[0], "testauthor")
        self.assertEqual(self.refrepo.year, 2023)
        self.assertEqual(self.refrepo.editor, "testeditor")
        self.assertEqual(self.refrepo.volume, 700)
        self.assertEqual(self.refrepo.number, 1)
        self.assertEqual(self.refrepo.series, 1)
        self.assertEqual(self.refrepo.pages, "108-110")
        self.assertEqual(self.refrepo.address, "testaddress")
        self.assertEqual(self.refrepo.month, 10)
        self.assertEqual(self.refrepo.organization, "testorganization")
        self.assertEqual(self.refrepo.publisher, "testpublisher")
        self.assertEqual(self.refrepo.note, "testnotes")
