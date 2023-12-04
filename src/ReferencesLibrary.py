from unittest.mock import Mock
from references import References
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services
from tests.references_test import StubIO
import secrets
from string import ascii_letters

class ReferencesLibrary:
    def __init__(self):
        self.repo = ReferencesRepository()
        self.storage_interface = Mock()
        self.reference_service = Services(self.repo)
        self._io = StubIO()

    def get_random_key(self):
        return secrets.token_hex(16)

    def ask_form(self):
        self._references = References(self._io, self.reference_service)

    #def ask_articleform(self):
        #self._references.articleform()

    #def ask_inproceedingsform(self):
        #self._references.inproceedingsform()

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )
