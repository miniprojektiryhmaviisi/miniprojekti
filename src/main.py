from references import References
from console_io import ConsoleIO
from repositories.book import Book
from services.reference_service import Services


def init():
    console_io = ConsoleIO()
    book_repo = Book()
    refe_services = Services(book_repo)
    final_reference = References(console_io, refe_services)

if __name__ == "__main__":
    init()
