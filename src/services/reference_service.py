class Services:

    def __init__(self, ref_repo,database_interface):
        self.ref_repo=ref_repo
        self.database_interface=database_interface
    def config_book_reference(self, key, title,author,publisher,year,volume="",number="",pages="",
                              month="",notes=""):
        self.ref_repo.add_key(key)
        self.ref_repo.add_title(title)
        self.ref_repo.add_author(author)
        self.ref_repo.add_publisher(publisher)
        self.ref_repo.add_year(year)
        self.ref_repo.add_volume(volume)
        self.ref_repo.add_number(number)
        self.ref_repo.add_pages(pages)
        self.ref_repo.add_month(month)
        self.ref_repo.add_note(notes)
        self.database_interface.store_bookref(self.ref_repo)

    def config_article_reference(self, key, title,author,journal,year,volume="",number="",pages="",
                                 month="",notes=""):
        self.ref_repo.add_key(key)
        self.ref_repo.add_title(title)
        self.ref_repo.add_author(author)
        self.ref_repo.add_publisher(journal)
        self.ref_repo.add_year(year)
        self.ref_repo.add_volume(volume)
        self.ref_repo.add_number(number)
        self.ref_repo.add_pages(pages)
        self.ref_repo.add_month(month)
        self.ref_repo.add_note(notes)

    def config_inpro_reference(self, key, title,booktitle, author,year,volume="",number="",
                               series="",pages="",month="",organization="", publisher="", notes="",
                               address=""):
        self.ref_repo.add_key(key)
        self.ref_repo.add_title(title)
        self.ref_repo.add_title(booktitle)
        self.ref_repo.add_author(author)
        self.ref_repo.add_publisher(publisher)
        self.ref_repo.add_year(year)
        self.ref_repo.add_volume(volume)
        self.ref_repo.add_number(number)
        self.ref_repo.add_series(series)
        self.ref_repo.add_pages(pages)
        self.ref_repo.add_month(month)
        self.ref_repo.add_organization(organization)
        self.ref_repo.add_note(notes)
        self.ref_repo.add_address(address)

    # FIXME: deprecate this function
    def return_book(self):
        return f"{self.ref_repo.key}, {self.ref_repo.title}, {self.ref_repo.author}, \
{self.ref_repo.publisher}, {self.ref_repo.year}, {self.ref_repo.volume}, {self.ref_repo.number}, \
{self.ref_repo.pages}, {self.ref_repo.month}, {self.ref_repo.notes}"
