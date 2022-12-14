from src.domain.Discipline import Discipline
from src.domain.Grade import Grade
from src.domain.Student import Student
from src.exceptions.exceptions import *
from src.services.DisciplineService import DisciplineService
from src.services.GradeService import GradeService
from src.services.StudentService import StudentService


class Console:
    def __init__(self, student_service: StudentService, discipline_service: DisciplineService,
                 grade_service: GradeService):
        self.__student_service = student_service
        self.__discipline_service = discipline_service
        self.__grade_service = grade_service

    def display_menu(self):
        """
        Displays the menu to the console.

        :return: none
        """
        print(f"""          🧧 MENU 🧧
1️⃣. Add student / discipline
2️⃣. Remove student / discipline
3️⃣. Update student / discipline
4️⃣. Display students / disciplines
5️⃣. Give grade
6️⃣. Search student / discipline
7️⃣. Failing students
8️⃣. Top students
9️⃣. Disciplines with grades
🔟. Display grades
1️⃣1️⃣. Exit
    ---------------------""")
        return

    def get_command(self):
        """
        Gets a command from the user.

        :return: string, command given by the user(input)
        """
        all_commands = ['add student', 'remove student', 'update student', 'display students', 'add discipline',
                        'remove discipline', 'update discipline', 'display disciplines', 'exit', 'undo', 'redo',
                        'give grade', 'search student id', 'search student name', 'search discipline id',
                        'search discipline name', 'failing students', 'top students', 'disciplines with grades',
                        'display grades']

        command = input('👑 Enter your command senpai🍙🎌: ').lower()
        if command not in all_commands:
            raise InvalidInput('invalid command')
        return command

    def execute_command(self, command):
        """
        Executes a given commands.

        :param command: string, command given by the user
        :return: none, calls another function
        """
        all_commands = {
            'add student': self.add_student,
            'remove student': self.remove_student,
            'update student': self.update_student,
            'display students': self.display_students,
            'add discipline': self.add_discipline,
            'remove discipline': self.remove_discipline,
            'update discipline': self.update_discipline,
            'display disciplines': self.display_disciplines,
            'give grade': self.give_grade,
            'search student id': self.search_student_id,
            'search student name': self.search_student_name,
            'search discipline id': self.search_discipline_id,
            'search discipline name': self.search_discipline_name,
            'failing students': self.failing_students,
            'top students': self.top_students,
            'disciplines with grades': self.disciplines_with_grades,
            'display grades': self.display_grades,
        }
        all_commands[command]()

    def add_student(self):
        try:
            stud_id = int(input('Enter student id: '))
            stud_name = input('Enter student name: ')
            student = Student(stud_id, stud_name)
            self.__student_service.add(student)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except ValueError as ve:
            print('Invalid student id!', ve)
        except:
            print('Invalid command! 👎')

    def remove_student(self):
        try:
            stud_id = int(input('Enter student id: '))
            # stud_name = input('Enter student name: ')
            student = self.__student_service.get_student_by_id(stud_id)
            if not student:
                print('That student doesn\'t even exist! 👿')
                return
            to_remove = []
            for grade in self.__grade_service.get_all():
                if grade.get_grade_student_id() == stud_id:
                    to_remove.append(grade)
            for grade in to_remove:
                self.__grade_service.delete(grade.get_id())
            self.__student_service.delete(student)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except InexistingEntityError as iee:
            print('Inexisting student! 👺')
        except ValueError as ve:
            print('Invalid id!', ve)
        except:
            print('Invalid command! 👎')

    def update_student(self):
        try:
            stud_id = int(input('Enter student id: '))
            # stud_name = input('Enter student name: ')
            stud_name2 = input('Enter the new name: ')
            # student1 = Student(stud_id, stud_name)
            student2 = Student(stud_id, stud_name2)
            self.__student_service.update(self.__student_service.get_student_by_id(stud_id), student2)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except InexistingEntityError as iee:
            print('Invalid command! 😜', iee)
        except ValueError as ve:
            print('Invalid student id!', ve)
        except:
            print('Invalid command! 👎')

    def display_students(self):
        list_of_students = self.__student_service.get_all()
        for student in list_of_students:
            print(student)

    def add_discipline(self):
        try:
            discipline_id = int(input('Enter discipline id: '))
            discipline_name = input('Enter discipline name: ')
            discipline = Discipline(discipline_id, discipline_name)
            self.__discipline_service.add(discipline)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except InexistingEntityError as iee:
            print(iee)
        except ValueError as ve:
            print('Invalid discipline id!', ve)
        except:
            print('Invalid command! 👎')

    def remove_discipline(self):
        try:
            discipline_id = int(input('Enter discipline id: '))
            # discipline_name = input('Enter discipline name: ')
            # discipline = Discipline(discipline_id, discipline_name)
            discipline = self.__discipline_service.get_discipline_by_id(discipline_id)
            if discipline == False:
                print('Discipline does not exist!')
                return
            # print('WORKING FOR NOW')
            to_remove = []
            for grade in self.__grade_service.get_all():
                if grade.get_grade_discipline_id() == discipline_id:
                    to_remove.append(grade)
            for grade in to_remove:
                self.__grade_service.delete(grade.get_id())
            self.__discipline_service.delete(discipline)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except ValueError as ve:
            print('Invalid id!', ve)
        except:
            print('Invalid command! Check the discipline id... 👎')

    def update_discipline(self):
        try:
            discipline_id = int(input('Enter discipline id: '))
            discipline_name2 = input('Enter the new name: ')  # may remove this
            """discipline_name = input('Enter discipline name: ')
            discipline_name2 = input('Enter the new name: ')
            discipline1 = Discipline(discipline_id, discipline_name)
            discipline2 = Discipline(discipline_id, discipline_name2)
            self.__discipline_service.update(discipline1, discipline2)"""
            self.__discipline_service.update(self.__discipline_service.get_discipline_by_id(discipline_id),
                                             Discipline(discipline_id, discipline_name2))
        except InvalidDisciplineAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except ValueError as ve:
            print('Invalid discipline id!', ve)
        except:
            print('Invalid command! 👎')

    def display_disciplines(self):
        list_of_disciplines = self.__discipline_service.get_all()
        for discipline in list_of_disciplines:
            print(discipline)

    def give_grade(self):
        try:
            stud_id = int(input('Enter student id'))
            discipline_id = int(input('Enter discipline id: '))
            grade_value = int(input('Enter  grade_value: '))
            grade = Grade(discipline_id, stud_id, grade_value)
            self.__grade_service.add(grade)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except ValueError as ve:
            print('That\'s not an integer!', ve)
        except:
            print('Invalid command! 👎')

    def search_student_id(self):
        while True:
            try:
                student_id = int(input('Enter a student id: '))
                if student_id < 0:
                    print('Invalid student id!')
                else:
                    break
            except ValueError:
                print('Invalid student id!')
        print(self.__student_service.find_id(student_id))

    def search_student_name(self):
        try:
            student_name = input('Enter a name: ')
            student = self.__student_service.find_name(student_name)
            if student:
                print(student)
            else:
                print('Student not found. 🙈')
        except InexistingEntityError as iee:
            print(iee)

    def search_discipline_id(self):
        while True:
            try:
                disc_id = int(input('Enter discipline id: '))
                if disc_id < 0:
                    print('Invalid discipline id!')
                else:
                    discipline = self.__discipline_service.get_discipline_by_id(disc_id)
                    if discipline:
                        print(discipline)
                    else:
                        print('Inexisting discipline!')
                    break
            except ValueError:
                print('Invalid discipline id!')

    def search_discipline_name(self):
        discipline_name = input('Enter discipline name: ')
        try:
            discipline = self.__discipline_service.find_name(discipline_name)
            if discipline:
                print(discipline)
            else:
                print('Discipline not found. 👺')
        except InexistingEntityError as iee:
            print(iee)

    def failing_students(self):
        list_of_failing_students = []
        for grade in self.__grade_service.get_all():
            if grade.get_grade_value() < 5:
                student = self.__student_service.get_student_by_id(grade.get_grade_student_id())
                if student not in list_of_failing_students:
                    list_of_failing_students.append(student)
        for student in list_of_failing_students:
            print(student)

    def top_students(self):
        pass

    def disciplines_with_grades(self):
        list_of_disciplines = []
        for grade in self.__grade_service.get_all():
            disc_id = grade.get_grade_discipline_id()
            disc = self.__discipline_service.find_id(disc_id)
            if disc not in list_of_disciplines:
                list_of_disciplines.append(disc)
        # todo: sort by grade descending ( each discipline has an average )

    def display_grades(self):
        for grade in self.__grade_service.get_all():
            print(grade)

    def run_console(self):
        while True:
            self.display_menu()
            # command = self.get_command().lower()
            # self.execute_command(command)
            # print(command)
            try:
                command = self.get_command().lower()
                if command == 'exit':
                    print('You\'ve left the app! See you soon... 👋😢😭')
                    break
                else:
                    self.execute_command(command)
            except ExistingEntityError as eee:
                print('Invalid command! 👎😝', eee)
            except InexistingEntityError as iee:
                print('Invalid command! 👎😝', iee)
            except InvalidStudentAttribute as isa:
                print('Invalid command! 👎😝', isa)
            except InvalidDisciplineAttribute as ida:
                print('Invalid command! 👎😝', ida)
            except InvalidGradeAttribute as iga:
                print('Invalid command! 👎😝', iga)
            except InvalidGradeValue as igv:
                print('Invalid command! 👎😝', igv)
            except InvalidInput as ii:
                print('Invalid command! 👎😝', ii)
            except StudentOrDisciplineInexistingError as sdie:
                print('Invalid command! 👎😝', sdie)
            except:
                print('Invalid command! 👎😝')
