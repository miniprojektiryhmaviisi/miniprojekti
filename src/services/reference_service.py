from storage_interface import get_interface

class Services:
    def __init__(self, ref_repo):
        self.ref_repo=ref_repo
        self.database_interface=get_interface()

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

    def search_reference(self, author, title):
        if not author:
            book_search = self.database_interface.search_book_by_title(title)
            art_search = self.database_interface.search_article_by_title(title)
            inpro_search = self.database_interface.search_inpro_by_title(title)
        elif not title:
            book_search = self.database_interface.search_book_by_author(author)
            art_search = self.database_interface.search_article_by_author(author)
            inpro_search = self.database_interface.search_inpro_by_author(author)
        else:
            book_search = self.database_interface.search_book_by_author_and_title(author, title)
            art_search = self.database_interface.search_article_by_author_and_title(author, title)
            inpro_search = self.database_interface.search_inpro_by_author_and_title(author, title)

        ref_dict = {
            "book": book_search,
            "article" : art_search,
            "inproceedings" : inpro_search
        }

        return ref_dict

    def delete_all(self):
        self.database_interface.delete_all_references()

    def delete_reference(self, cite_keys):
        db_keys = self.database_interface.get_all_citekeys()
        #print(db_keys)
        message = "Reference(s) with cite key(s)\n ----\n"
        for key in cite_keys:
            if key in db_keys["book"]:
                self.database_interface.delete_book_reference(key)
                message += f"- {key}\n"
            elif key in db_keys["article"]:
                self.database_interface.delete_article_reference(key)
                message += f"- {key}\n"
            elif key in db_keys["inproceedings"]:
                self.database_interface.delete_inproceedings_reference(key)
                message += f"- {key}\n"
        message += "deleted."
        return message
