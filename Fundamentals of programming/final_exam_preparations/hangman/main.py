from controller.controller import Controller
from repo.TextFileRepo import TextFileRepository
from repo.repository import Repository
from ui.console import Ui


def main():
    repo_type = 'text'
    if repo_type == 'text':
        repo = TextFileRepository('text')
    else:
        repo = Repository()
    controller = Controller(repo)
    console = Ui(controller)
    if repo_type == 'text':
        repo.save_data_to_file()
    console.start()


if __name__ == '__main__':
    main()
