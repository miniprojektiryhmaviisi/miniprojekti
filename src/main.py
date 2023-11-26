from references import References
from console_io import ConsoleIO
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services


def init():
    console_io = ConsoleIO()
    book_repo = ReferencesRepository()
    refe_services = Services(book_repo)
    References(console_io, refe_services)

if __name__ == "__main__":
    init()
