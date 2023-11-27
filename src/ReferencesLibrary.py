from references import References
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services
from unittest.mock import Mock, ANY, patch
from tests.references_test import StubIO

class ReferencesLibrary:
    def __init__(self):
        self._io = StubIO()
        self.repo = ReferencesRepository()
        self.reference_service = Services(self.repo)
        self._references = References(self._io, self.reference_service, None)

    def ask_bookform(self):
        self._references.bookform()

    def ask_articleform(self):
        self._references.articleform()

    def ask_inproceedingsform(self):
        self._references.inproceedingsform()

    def input(self, value):
        self._io.write(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )