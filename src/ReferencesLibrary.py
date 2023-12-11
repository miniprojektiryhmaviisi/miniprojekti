import secrets
from unittest.mock import Mock
from references import References
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services
from tests.references_test import StubIO

class ReferencesLibrary:
    def __init__(self):
        self.repo = ReferencesRepository()
        self.storage_interface = Mock()
        self.reference_service = Services(self.repo)
        self._io = StubIO()

    def get_random_key(self):
        return secrets.token_hex(16)

    def execute_app(self):
        self._references = References(self._io, self.reference_service)

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def order_should_be(self, value1, value2):
        outputs = self._io.outputs

        if not (value1 in outputs and value2 in outputs):
            with open("debug.txt", "wt", encoding="utf-8") as file:
                file.writelines(outputs)
            raise AssertionError("Both expected values were not present")

        index1 = outputs.index(value1)
        index2 = outputs.index(value2)

        if not index1 < index2:
            print(outputs)
            raise AssertionError("The values were not in correct order")

    def order_in_file_should_be(self, filepath, value1, value2):
        with open(filepath, "rt", encoding="utf-8") as file:
            outputs = [line.strip() for line in file.readlines()]

        index1 = outputs.index(value1)
        index2 = outputs.index(value2)

        if not index1 < index2:
            raise AssertionError("The values were not in correct order")
