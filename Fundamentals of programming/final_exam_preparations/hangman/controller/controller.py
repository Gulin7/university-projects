import random


class Controller:
    def __init__(self, repo):
        self.__repo = repo
        self.__current_sentence = 0
        self.__current_hangman = [['h', 'a', 'n', 'g', 'm', 'a', 'n'], [0, 0, 0, 0, 0, 0, 0]]
        self.__current_progress = []

    def check_validity(self, sentence: str):
        return self.__repo.check_validity(sentence)

    def delete_sentence(self, sentence: str):
        self.__repo.delete_sentence(sentence)

    def add_sentence(self, sentence: str):
        self.__repo.add_sentence(sentence)

    def get_all(self):
        return list(self.__repo.get_all())

    def random_sentence(self):
        sentence = random.choice(self.get_all())
        self.__current_sentence = sentence.get_sentence_list()
        self.__current_progress.append(self.__current_sentence[0])
        for index in range(1, len(self.__current_sentence) - 1):
            if self.__current_sentence[index - 1] == ' ' or self.__current_sentence[index + 1] == ' ':
                self.__current_progress.append(self.__current_sentence[index])
            else:
                self.__current_progress.append('_')

    def check_letter(self, new_letter):
        if new_letter in self.__current_sentence:
            for index in range(len(self.__current_sentence)):
                if self.__current_sentence[index] == new_letter:
                    self.__current_progress[index] = new_letter
            return True
        else:
            for i in range(7):
                if self.__current_hangman[1][i] == 0:
                    self.__current_hangman[1][i] = 1
                    return False
