from src.ui.ui import Ui
from src.services.services import Service
from src.repository.repository import MemoryRepo


def main():
    memory_repo = MemoryRepo()
    service = Service(memory_repo, 'TextFile.txt')
    ui = Ui(service)
    ui.start()


if __name__ == '__main__':
    main()
