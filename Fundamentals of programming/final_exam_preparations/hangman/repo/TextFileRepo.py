import os

from domain.entities import Sentence
from repo.repository import Repository


class TextFileRepository(Repository):
    def __init__(self, file_name):
        Repository.__init__(self)
        self.__file_name = file_name
        self.read_data_from_file()

    def read_data_from_file(self):
        if os.path.getsize(self.__file_name) <= 0:
            self.__repo = []
            return
        with open(self.__file_name) as file:
            for line in file:
                sentence = Sentence(line)
                Repository.add_sentence(self, sentence.get_sentence())

    def save_data_to_file(self):
        sentences = Repository.get_all(self)
        with open(self.__file_name, "w") as file:
            for sentence in sentences:
                file.write(sentence.get_sentence())
