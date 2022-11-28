import erori
from domain.entities import *
from erori.repoError import RepoError
from erori.validationError import ValidError


class Teste:
    def __init__(self, validatorStudent, validatorDisciplina, validatorNota, repoStudenti, repoDiscipline, repoNote, serviceStudenti, serviceDiscipline, serviceNote):
        self.__validatorStudent = validatorStudent
        self.__validatorDisciplina = validatorDisciplina
        self.__validatorNota = validatorNota
        self.__repoStudenti = repoStudenti
        self.__repoDiscipline = repoDiscipline
        self.__repoNote = repoNote
        self.__serviceStudenti = serviceStudenti
        self.__serviceDiscipline = serviceDiscipline
        self.__serviceNote = serviceNote

    def testCreazaStudent(self):
        student = Student("1", "Alex")
        assert student.getID() == "1"
        assert student.getName() == "Alex"

    def testEgalStudent(self):
        student1 = Student("1", "Alex")
        student2 = Student("1", "Alex")
        assert student1 == student2

    def testCreazaDisciplina(self):
        disciplina = Disciplina("1", "FP", "Czibula")
        assert disciplina.getID() == "1"
        assert disciplina.getName() == "FP"
        assert disciplina.getProf() == "Czibula"

    def testEgalDisciplina(self):
        d1 = Disciplina("1", "FP", "Czibula")
        d2 = Disciplina("1", "FP", "Czibula")
        assert d1 == d2

    def testCreeazaNota(self):
        nota = Nota("1", "1 Alex", "1 FP Czibula", 10.0)
        assert nota.getID() == "1"
        assert nota.getStudent() == "1 Alex"
        assert nota.getDisc() == "1 FP Czibula"
        assert nota.getNota() == 10.0

    def testEgalNota(self):
        nota1 = Nota("1", "1 Alex", "1 FP Czibula", 10.0)
        nota2 = Nota("2", "1 Alex", "2 ASC Vancea", 10.0)
        assert nota1 == nota2

    def testValidatorStudent(self):
        student = Student("-3", "")
        try:
            self.__validatorStudent.valideaza(student)
            assert False
        except ValidError as ve:
            assert str(ve) == "ID student invalid!\nNume student invalid!\n"

    def testValidatorDisciplina(self):
        disciplina = Disciplina("-5", "", "")
        try:
            self.__validatorDisciplina.valideaza(disciplina)
            assert False
        except ValidError as ve:
            assert str(ve) == "ID disciplina invalid!\nNume disciplina invalid!\nNume profesor invalid!\n"

    def testValidatorNota(self):
        nota = Nota("-1", "1 Alex", "1 FP Czibula", -5)
        try:
            self.__validatorNota.valideaza(nota)
            assert False
        except ValidError as ve:
            assert str(ve) == "ID nota invalid!\nValoare nota invalida!\n"

    def testStoreStudent(self):
        student = Student("1", "Alex")
        assert self.__repoStudenti.size() == 0
        self.__repoStudenti.store(student)
        assert self.__repoStudenti.size() == 1
        student2 = Student("2", "Iarina")
        self.__repoStudenti.store(student2)
        assert self.__repoStudenti.size() == 2
        student3 = Student("2", "Cipriana")
        try:
            self.__repoStudenti.store(student3)
            assert False
        except RepoError:
            pass

    def testStoreDisciplina(self):
        disc = Disciplina("1", "FP", "Czibula")
        assert self.__repoDiscipline.size() == 0
        self.__repoDiscipline.store(disc)
        assert self.__repoDiscipline.size() == 1
        disc2 = Disciplina("2", "ASC", "Vancea")
        self.__repoDiscipline.store(disc2)
        assert self.__repoDiscipline.size() == 2
        disc3 = Disciplina("2", "LC", "Pop")
        try:
            self.__repoDiscipline.store(disc3)
            assert False
        except RepoError:
            pass

    def testStoreNota(self):
        nota = Nota("1", "1 Alex", "1 FP Czibula", 10.0)
        assert self.__repoNote.size() == 0
        self.__repoNote.store(nota)
        assert self.__repoNote.size() == 1
        nota2 = Nota("2", "1 Alex", "1 FP Czibula", 10.0)
        self.__repoNote.store(nota2)
        assert self.__repoNote.size() == 2
        nota3 = Nota("2", "1 Alex", "1 ASC Vancea", 10.0)
        try:
            self.__repoNote.store(nota3)
            assert False
        except RepoError:
            pass

    def testCautaStudent(self):
        student = Student("5", "Alex")
        self.__repoStudenti.store(student)
        assert self.__repoStudenti.cautaStudent("5") == student
        try:
            self.__repoStudenti.cautaStudent("3")
            assert False
        except RepoError:
            pass

    def testCautaDisciplina(self):
        disc = Disciplina("1", "FP", "Czibula")
        assert self.__repoDiscipline.cautaDisciplina("1") == disc
        try:
            self.__repoDiscipline.cautaDisciplina("3")
            assert False
        except RepoError:
            pass

    def testModificaStudent(self):
        student = Student("7", "Alex")
        self.__repoStudenti.store(student)
        self.__repoStudenti.modificaStudent("7", "Tudor")
        assert student.getName() == "Tudor"

    def testModificaDisciplina(self):
        disc = Disciplina("8", "FP", "Czibula")
        self.__repoDiscipline.store(disc)
        self.__repoDiscipline.modificaNumeDisciplina("8", "ASC")
        self.__repoDiscipline.modificaProfDisciplina("8", "Vancea")
        assert disc.getName() == "ASC"
        assert disc.getProf() == "Vancea"

    def testStergeStudent(self):
        student = Student("10", "Alex")
        self.__repoStudenti.store(student)
        self.__repoStudenti.stergeStudent("10")
        assert student.getSters() == True

    def testStergeDisc(self):
        disc = Disciplina("10", "FP", "Czibula")
        self.__repoDiscipline.store(disc)
        self.__repoDiscipline.stergeDisc("10")
        assert disc.getSters() == True
