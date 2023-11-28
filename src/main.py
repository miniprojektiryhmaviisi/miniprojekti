from references import References
from console_io import ConsoleIO
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services
from build import build
from storage_interface import StorageInterface

def init():
    build()
    console_io = ConsoleIO()
    ref_repo = ReferencesRepository()
    refe_services = Services(ref_repo)
    References(console_io, refe_services)
#    connection.close()

if __name__ == "__main__":
    init()
