class Services:
    def __init__(self, book_repo):
        self.book_repo=book_repo
        
    def config_reference(self,title,author,publisher,year,volume,number,pages,month,note):
        self.book_repo.add_title(title)
        self.book_repo.add_author(author)
        self.book_repo.add_publisher(publisher)
        self.book_repo.add_year(year)
        self.book_repo.add_volume(volume)
        self.book_repo.add_number(number)
        self.book_repo.add_pages(pages)
        self.book_repo.add_month(month)
        self.book_repo.add_note(note)

    def return_book(self):
        return f"{self.book_repo.title}, {self.book_repo.author}, {self.book_repo.publisher}, {self.book_repo.year}, {self.book_repo.volume}, {self.book_repo.number}, {self.book_repo.pages}, {self.book_repo.month}, {self.book_repo.note}"
