from references import References
from console_io import ConsoleIO
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services
from database import db, connection
from storage_interface import StorageInterface

def init():
    console_io = ConsoleIO()
    ref_repo = ReferencesRepository()
    refe_services = Services(ref_repo)
    storage_interface = StorageInterface(db)
    References(console_io, refe_services, storage_interface)
    connection.close()

if __name__ == "__main__":
    init()
