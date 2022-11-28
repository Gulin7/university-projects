from domain.entities import Student, Disciplina
from persistenta.repository import RepositoryNote


class ServiceStudenti:

    def __init__(self, validatorStudent, repoStudenti):
        self.__validatorStudent = validatorStudent
        self.__repoStudenti = repoStudenti

    def adaugaStudent(self, idStudent, numeStudent):
        student = Student(idStudent, numeStudent)
        self.__validatorStudent.valideaza(student)
        self.__repoStudenti.store(student)

    def cautaStudent(self, idStudent):
        return self.__repoStudenti.cautaStudent(idStudent)

    def modificaStudent(self, idStudent, numeNouStudent):
        self.__repoStudenti.modificaStudent(idStudent, numeNouStudent)

    def getAll(self):
        return self.__repoStudenti.getAll()

    def size(self):
        return self.__repoStudenti.size()


class ServiceDiscipline:

    def __init__(self, validatorDisc, repoDisc):
        self.__validatorDisc = validatorDisc
        self.__repoDisc = repoDisc

    def adaugaDisc(self, idDisc, numeDisc, profDisc):
        disciplina = Disciplina(idDisc, numeDisc, profDisc)
        self.__validatorDisc.valideaza(disciplina)
        self.__repoDisc.store(disciplina)

    def cautaDisciplina(self, idDisciplina):
        return self.__repoDisc.cautaDisciplina(idDisciplina)

    def modificaNumeDisc(self, idDisciplina, numeNouDisc):
        self.__repoDisc.modificaNumeDisciplina(idDisciplina, numeNouDisc)

    def modificaProfDisc(self, idDisciplina, profNouDisc):
        self.__repoDisc.modificaProfDisciplina(idDisciplina, profNouDisc)

    def getAll(self):
        return self.__repoDisc.getAll()

    def size(self):
        return self.__repoDisc.size()


class ServiceNote:

    def __init__(self, validatorNota, repoNote, repoStudenti, repoDisc):
        self.__validatorNota = validatorNota
        self.__repoNote = repoNote
        self.__repoStudenti = repoStudenti
        self.__repoDisc = repoDisc

    def StergeStudentSiNote(self, idStudent):
        student = self.__repoStudenti.cautaStudent(idStudent)
        note = self.__repoNote.getAll()
        noteStudent = [x for x in note if x.getStudent() == student]
        for notaStudent in noteStudent:
            self.__repoNote.stergeNota(notaStudent.getID)
        self.__repoStudenti.stergeStudent(idStudent)

    def StergeDisciplinaSiNote(self, idDisciplina):
        disciplina = self.__repoDisc.cautaDisciplina(idDisciplina)
        note = self.__repoNote.getAll()
        noteDiscipline = [x for x in note if x.getDisc() == disciplina]
        for notaDisc in noteDiscipline:
            self.__repoNote.stergeNota(notaDisc.getID)
        self.__repoDisc.stergeDisc(idDisciplina)

    def size(self):
        return self.__repoNote.size()

