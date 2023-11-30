class ReferencesRepository:
    def __init__(self):
        self.key = ""
        self.title = ""
        self.author = []
        self.publisher = ""
        self.year = 0
        self.volume = 0
        self.number = 0
        self.pages = ""
        self.month = 0
        self.note = ""
        self.journal = ""
        self.booktitle = ""
        self.editor = ""
        self.series = ""
        self.address = ""
        self.organization = ""

    def add_key(self, key):
        self.key = key

    def add_title(self, title):
        self.title = title

    def add_author(self, author):
        self.author = author

    def add_publisher(self, publisher):
        self.publisher = publisher

    def add_year(self, year):
        self.year = year

    def add_volume(self, volume):
        self.volume = volume

    def add_number(self, number):
        self.number = number

    def add_pages(self, pages):
        self.pages = pages

    def add_month(self, month):
        self.month = month

    def add_note(self, note):
        self.note = note

    def add_journal(self, journal):
        self.journal = journal

    def add_booktitle(self, booktitle):
        self.booktitle = booktitle

    def add_editor(self, editor):
        self.editor = editor

    def add_series(self, series):
        self.series = series

    def add_address(self, address):
        self.address = address

    def add_organization(self, organization):
        self.organization = organization
