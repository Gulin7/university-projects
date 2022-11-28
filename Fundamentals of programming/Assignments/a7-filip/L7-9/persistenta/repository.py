from domain.entities import *
from erori.repoError import RepoError


class RepositoryStudenti:
    def __init__(self):
        self.__studenti = {}

    def store(self, student):
        if student.getID() in self.__studenti:
            raise RepoError("Student deja existent!")
        self.__studenti[student.getID()] = student

    def stergeStudent(self, idStudent):
        if idStudent not in self.__studenti or self.__studenti[idStudent].getSters == True:
            raise RepoError("Student inexistent!")
        self.__studenti[idStudent].sterge()

    def cautaStudent(self, idStudent):
        if idStudent not in self.__studenti:
            raise RepoError("Student inexistent!")
        return self.__studenti[idStudent]

    def modificaStudent(self, idStudent, numeNou):
        if idStudent not in self.__studenti:
            raise RepoError("Student inexistent!")
        self.__studenti[idStudent].setName(numeNou)

    def size(self):
        return len(self.__studenti)

    def getAll(self):
        return list(self.__studenti.values())

    def clear(self):
        for idStudent in self.__studenti:
            self.__studenti[idStudent].sterge()


class RepositoryDiscipline:
    def __init__(self):
        self.__discipline = {}

    def store(self, disc):
        if disc.getID() in self.__discipline:
            raise RepoError("Discplina deja existenta!")
        self.__discipline[disc.getID()] = disc

    def stergeDisc(self, idDisciplina):
        if idDisciplina not in self.__discipline or self.__discipline[idDisciplina].getSters == True:
            raise RepoError("Student inexistent!")
        self.__discipline[idDisciplina].sterge()

    def cautaDisciplina(self, idDisc):
        if idDisc not in self.__discipline:
            raise RepoError("Disciplina inexistenta!")
        return self.__discipline[idDisc]

    def modificaNumeDisciplina(self, idDisciplina, numeNou):
        if idDisciplina not in self.__discipline:
            raise RepoError("Student inexistent!")
        self.__discipline[idDisciplina].setName(numeNou)

    def modificaProfDisciplina(self, idDisciplina, profNou):
        if idDisciplina not in self.__discipline:
            raise RepoError("Student inexistent!")
        self.__discipline[idDisciplina].setProf(profNou)

    def size(self):
        return len(self.__discipline)

    def getAll(self):
        return list(self.__discipline.values())


class RepositoryNote:
    def __init__(self):
        self.__note = {}

    def store(self, nota):
        if nota.getID() in self.__note:
            raise RepoError("Nota deja existenta!")
        self.__note[nota.getID()] = nota

    def stergeNota(self, idNota):
        if idNota not in self.__note or self.__note[idNota].sters() == True:
            raise RepoError("Nota inexistenta!")
        self.__note[idNota].sterge()

    def size(self):
        return len(self.__note)

    def getAll(self):
        return list(self.__note.values())
