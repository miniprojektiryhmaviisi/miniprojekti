from storage_interface import refe_interface

class Services:
    def __init__(self, ref_repo):
        self.ref_repo=ref_repo
        self.database_interface=refe_interface

    def config_book_reference(self, key, title, author, publisher, year, volume="", number="",
                              pages="", month="", notes=""):
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

    def config_article_reference(self, key, title, author, journal, year, volume="", number="",
                                 pages="", month="",notes=""):
        self.ref_repo.add_key(key)
        self.ref_repo.add_title(title)
        self.ref_repo.add_author(author)
        self.ref_repo.add_journal(journal)
        self.ref_repo.add_year(year)
        self.ref_repo.add_volume(volume)
        self.ref_repo.add_number(number)
        self.ref_repo.add_pages(pages)
        self.ref_repo.add_month(month)
        self.ref_repo.add_note(notes)
        self.database_interface.store_articleref(self.ref_repo)

    def config_inpro_reference(self, key, title, booktitle, author, year, editor="", volume="",
                               number="", series="", pages="", address="", month="",
                               organization="", publisher="", notes=""):
        self.ref_repo.add_key(key)
        self.ref_repo.add_title(title)
        self.ref_repo.add_booktitle(booktitle)
        self.ref_repo.add_author(author)
        self.ref_repo.add_publisher(publisher)
        self.ref_repo.add_year(year)
        self.ref_repo.add_editor(editor)
        self.ref_repo.add_volume(volume)
        self.ref_repo.add_number(number)
        self.ref_repo.add_series(series)
        self.ref_repo.add_pages(pages)
        self.ref_repo.add_month(month)
        self.ref_repo.add_organization(organization)
        self.ref_repo.add_note(notes)
        self.ref_repo.add_address(address)
        self.database_interface.store_inproref(self.ref_repo)

    def get_all_books(self):
        return self.database_interface.get_all_from_bookref()

    def get_all_articles(self):
        return self.database_interface.get_all_from_articleref()

    def get_all_inproceedings(self):
        return self.database_interface.get_all_from_inproref()
