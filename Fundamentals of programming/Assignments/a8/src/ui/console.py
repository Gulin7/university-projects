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
5️⃣. Grade student at a discipline
6️⃣. Search student / discipline
7️⃣. Failing students
8️⃣. Top students
9️⃣. Disciplines with grades
🔟.Exit
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
                        'search discipline name', 'failing students', 'top students', 'disciplines with grades']

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
        }
        all_commands[command]()

    def add_student(self):
        try:
            stud_id = input('Enter student id: ')
            stud_name = input('Enter student name: ')
            student = Student(stud_id, stud_name)
            self.__student_service.add(student)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except:
            print('Invalid command! 👎')

    def remove_student(self):
        try:
            stud_id = input('Enter student id: ')
            stud_name = input('Enter student name: ')
            student = Student(stud_id, stud_name)
            self.__student_service.delete(student)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except:
            print('Invalid command! 👎')

    def update_student(self):
        try:
            stud_id = input('Enter student id: ')
            stud_name = input('Enter student name: ')
            stud_name2 = input('Enter the new name: ')
            student1 = Student(stud_id, stud_name)
            student2 = Student(stud_id, stud_name2)
            self.__student_service.update(student1, student2)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except:
            print('Invalid command! 👎')

    def display_students(self):
        list_of_students = self.__student_service.get_all()
        for student in list_of_students:
            print(student)

    def add_discipline(self):
        try:
            discipline_id = input('Enter discipline id: ')
            discipline_name = input('Enter discipline name: ')
            discipline = Discipline(discipline_id, discipline_name)
            self.__discipline_service.add(discipline)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except:
            print('Invalid command! 👎')

    def remove_discipline(self):
        try:
            discipline_id = input('Enter discipline id: ')
            discipline_name = input('Enter discipline name: ')
            discipline = Discipline(discipline_id, discipline_name)
            self.__discipline_service.delete(discipline)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except:
            print('Invalid command! 👎')

    def update_discipline(self):
        try:
            discipline_id = input('Enter discipline id: ')
            discipline_name = input('Enter discipline name: ')
            discipline_name2 = input('Enter the new name: ')
            discipline1 = Discipline(discipline_id, discipline_name)
            discipline2 = Discipline(discipline_id, discipline_name2)
            self.__discipline_service.update(discipline1, discipline2)
        except InvalidDisciplineAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
        except:
            print('Invalid command! 👎')

    def display_disciplines(self):
        list_of_disciplines = self.__discipline_service.get_all()
        for discipline in list_of_disciplines:
            print(discipline)

    def give_grade(self):
        try:
            stud_id = input('Enter student id')
            discipline_id = input('Enter discipline id: ')
            grade_value = input('Enter  grade_value: ')
            grade = Grade(discipline_id, stud_id, grade_value)
            self.__grade_service.add(grade)
        except InvalidStudentAttribute as isa:
            print('Invalid command! 😜', isa)
        except ExistingEntityError as eee:
            print('Invalid command! 😜', eee)
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
        student_name = input('Enter a name: ')
        print(self.__student_service.find_name(student_name))

    def search_discipline_id(self):
        pass

    def search_discipline_name(self):
        pass

    def failing_students(self):
        pass

    def top_students(self):
        pass

    def disciplines_with_grades(self):
        pass

    def run_console(self):
        while True:
            self.display_menu()
            command = self.get_command().lower()
            # print(command)
            if command == 'exit':
                print('You\'ve left the app! See you soon... 👋😢😭')
                break
            else:
                self.execute_command(command)
            """try:
                command = self.get_command().lower()
                # print(command)
                if command == 'exit':
                    print('You\'ve left the app! See you soon... 👋😢😭')
                    break
                else:
                    self.execute_command(command)
            except:
                print('Invalid command! 👎😝')"""
