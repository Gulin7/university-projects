zfrom erori.repoError import RepoError
from erori.validationError import ValidError


class UI:

    def __init__(self, serviceStudenti, serviceDisc, serviceNote):
        self.__serviceStudenti = serviceStudenti
        self.__serviceNote = serviceNote
        self.__serviceDisc = serviceDisc
        self.__inputs = {
            "adauga_student": self.__uiAdaugaStudent,
            "adauga_disciplina": self.__uiAdaugaDisc,
            "print_studenti": self.__uiPrintStudenti,
            "print_discipline": self.__uiPrintDisc,
            "sterge_student_si_notele_lui": self.__uiStergeStudentSiNote,
            "sterge_disciplina_si_notele_asociate": self.__uiStergeDisciplinaSiNote,
            "cauta_student": self.__uiCautaStudentID,
            "cauta_disciplina": self.__uiCautaDisciplinaID,
            "modifica_student": self.__uiModificaStudent,
            "modifica_nume_disciplina": self.__uiModificaNumeDisciplina,
            "modifica_prof_disciplina": self.__uiModificaProfDisciplina
        }

    def __uiAdaugaStudent(self):
        if len(self.__params) != 2:
            print("Numar parametri invalid!")
            return
        idStudent = int(self.__params[0])
        numeStudent = self.__params[1]
        self.__serviceStudenti.adaugaStudent(idStudent, numeStudent)
        print("Student adaugat cu succes!")

    def __uiAdaugaDisc(self):
        if len(self.__params) != 3:
            print("Numar parametri invalid!")
            return
        idDisc = int(self.__params[0])
        numeDisc = self.__params[1]
        profDisc = self.__params[2]
        self.__serviceDisc.adaugaDisc(idDisc, numeDisc, profDisc)
        print("Disciplina adaugata cu succes!")

    def __uiPrintDisc(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        discipline = self.__serviceDisc.getAll()
        if len(discipline) == 0:
            print("Nu exista discipline in aplicatie!")
            return
        for disciplina in discipline:
            print(disciplina)

    def __uiPrintStudenti(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        studenti = self.__serviceStudenti.getAll()
        if len(studenti) == 0:
            print("Nu exista studenti in aplicatie")
            return
        for student in studenti:
            print(student)

    def __uiStergeStudentSiNote(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        idStudent = int(self.__params[0])
        self.__serviceNote.StergeStudentSiNote(idStudent)
        print(f"Studentul cu id {idStudent} si notele lui au fost sterse cu succes!")

    def __uiStergeDisciplinaSiNote(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        idDisc = int(self.__params[0])
        self.__serviceNote.StergeDisciplinaSiNote(idDisc)
        print(f"Disciplina cu id {idDisc} si notele asociate au fost sterse cu succes!")

    def __uiCautaStudentID(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        idStudent = int(self.__params[0])
        print(self.__serviceStudenti.cautaStudent(idStudent))

    def __uiCautaDisciplinaID(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        idDisciplina = int(self.__params[0])
        print(self.__serviceDisc.cautaDisciplina(idDisciplina))

    def __uiModificaStudent(self):
        if len(self.__params) != 2:
            print("Numar parametri invalid!")
            return
        idStudent = int(self.__params[0])
        numeNouStudent = self.__params[1]
        self.__serviceStudenti.modificaStudent(idStudent, numeNouStudent)

    def __uiModificaNumeDisciplina(self):
        if len(self.__params) != 2:
            print("Numar parametri invalid!")
            return
        ifDisciplina = int(self.__params[0])
        numeNouDisc = self.__params[1]
        self.__serviceDisc.modificaNumeDisc(ifDisciplina, numeNouDisc)

    def __uiModificaProfDisciplina(self):
        if len(self.__params) != 2:
            print("Numar parametri invalid!")
            return
        ifDisciplina = int(self.__params[0])
        profNouDisc = self.__params[1]
        self.__serviceDisc.modificaProfDisc(ifDisciplina, profNouDisc)

    def run(self):
        while True:
            input0 = input(">>>")
            input0 = input0.strip()
            if input0 == "":
                continue
            if input0 == "exit":
                return
            parti = input0.split()
            input1 = parti[0]
            self.__params = parti[1:]
            if input1 in self.__inputs:
                try:
                    self.__inputs[input1]()
                except ValueError:
                    print("Eroare UI: tip numeric invalid!")
                except ValidError as ve:
                    print(f"Valid error:{ve}")
                except RepoError as re:
                    print(f"Repository error:{re}")
            else:
                print("Comanda invalida!")

