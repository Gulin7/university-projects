from src.repository.Repository import Repository
from src.repository.TextFileRepository import TextFileRepository
from src.service.service import Service
from src.ui.ui import Ui


def main():
    # repo = Repository()
    text_repo = TextFileRepository('boardfile')
    service = Service(text_repo)
    ui = Ui(service)
    ui.start_console()


if __name__ == '__main__':
    main()
