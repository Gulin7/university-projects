from domain.entities import Sentence


class Repository:
    def __init__(self):
        self.__repo = []

    def get_all(self):
        return list(self.__repo)

    def check_validity(self, sentence: str):
        words = sentence.split(' ')
        for word in words:
            if len(word) < 3:
                raise ValueError('invalid sentence')
        return True

    def add_sentence(self, sentence: str):
        sentence_to_add = Sentence(sentence)
        for sent in self.get_all():
            if sent.check_equal(sentence_to_add.get_sentence()):
                raise ValueError('existing sentence')
        if self.check_validity(sentence_to_add.get_sentence()):
            self.__repo.append(sentence_to_add)

    def delete_sentence(self, sentence: str):
        for sent in self.get_all():
            if sent.check_equal(sentence):
                self.__repo.pop(sent)
                return
        raise ValueError('inexisting sentence')
