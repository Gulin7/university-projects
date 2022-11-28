from domain.entities import Student, Disciplina
from erori.validationError import ValidError


class ValidatorStudent:
    def __init(self):
        pass

    def valideaza(self, student):
        errors = ''
        if int(student.getID()) < 0: errors += "ID student invalid!\n"
        if student.getName() == "": errors += "Nume student invalid!\n"
        if len(errors):
            raise ValidError(errors)


class ValidatorDisciplina:
    def valideaza(self, disciplina):
        errors = ''
        if int(disciplina.getID()) < 0: errors += "ID disciplina invalid!\n"
        if disciplina.getName() == "": errors += "Nume disciplina invalid!\n"
        if disciplina.getProf() == "": errors += "Nume profesor invalid!\n"
        if len(errors):
            raise ValidError(errors)


class ValidatorNota:
    def valideaza(self, nota):
        errors = ''
        if int(nota.getID()) < 0: errors += "ID nota invalid!\n"
        if float(nota.getNota()) < 0: errors += "Valoare nota invalida!\n"
        if len(errors):
            raise ValidError(errors)
