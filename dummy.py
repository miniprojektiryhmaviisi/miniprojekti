class Calculator:
    def __init__(self) -> None:
        self.value = 0

    def add(self, value: int) -> int:
        self.value += value
        return self.value

    def multiply(self, value: int) -> int:
        self.value *= value
        return self.value
