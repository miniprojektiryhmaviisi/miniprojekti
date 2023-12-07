from references import References
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services
from db_build import build
from tests.references_test import StubIO

def main():
    build()
    console_io = StubIO([
        "0", "A", "book", "Operating Systems: Internals and Design Principles", "William Stallings",
        "", "MacMillan", "2012", "768", "7", "110--115", "", "",
        "0", "B", "article", "How artificial intelligence is transforming the world",
        "Darrel. M West", "", "Brookings", "2018", "", "", "", "4", "",
        "0", "C", "inproceeding", "Augmenting Robot Software Development Process with Flexbot",
        "2023 IEEE/ACM 5th International Workshop on Robotics Software Engineering (RoSE)",
        "Paulius Daubaris", "", "2023", "", "", "", "", "69--72", "United States", "7", "", "", "",
        "5"
    ])
    ref_repo = ReferencesRepository()
    refe_services = Services(ref_repo)
    References(console_io, refe_services)

if __name__ == "__main__":
    main()
