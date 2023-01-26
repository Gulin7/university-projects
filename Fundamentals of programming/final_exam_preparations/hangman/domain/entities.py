class Sentence:
    def __init__(self, sentence):
        self.__sentence = sentence.lower()
        self.__sentence_list = []
        for letter in self.__sentence:
            if letter != '\n':
                self.__sentence_list.append(letter)

    def get_sentence(self):
        return self.__sentence

    def get_sentence_list(self):
        return self.__sentence_list

    def check_equal(self, sentence: str):
        if self.get_sentence() == sentence:
            return True
        return False

    def __str__(self):
        return str(self.__sentence)
