from src import dummy

# pylint: disable=invalid-name
class dummy_library:
    def __init__(self):
        self._dummy = dummy.Calculator()

    def add(self, value):
        self._dummy.add(int(value))

    def value_should_be(self, expected):
        int_expected = int(expected)
        if self._dummy.value != int_expected:
            raise AssertionError(f"{self._dummy.value} != {int_expected}")

    def multiply(self, value):
        self._dummy.multiply(int(value))
