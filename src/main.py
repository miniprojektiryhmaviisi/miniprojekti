import sys

from references import References
from console_io import ConsoleIO
from repositories.referencesrepository import ReferencesRepository
from services.reference_service import Services

# launch normal-mode: 'python src/main.py'
# launch demo-mode: 'python src/main.py demo'
##   demo mode initializes database with test data

def init(use_demo_data: bool):
    console_io = ConsoleIO()
    ref_repo = ReferencesRepository()
    refe_services = Services(ref_repo, demo=use_demo_data)
    References(console_io, refe_services)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        mode = sys.argv[1]
    else:
        mode = "normal"
    demo = mode == "demo"
    init(use_demo_data=demo)
