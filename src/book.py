class Book:
    def __init__(self):
        self.title = ""
        self.author = []
        self.publisher = ""
        self.year = 0
        self.volume = 0
        self.number = 0
        self.pages = ""
        self.month = 0
        self.note = ""

    def __str__(self):
        return f"{self.title} {self.author} {self.publisher} {self.year} {self.volume} {self.number} {self.pages} {self.month} {self.note}"
