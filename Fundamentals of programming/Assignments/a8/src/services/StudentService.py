from src.domain.Student import Student
from src.exceptions.exceptions import *
from src.repository.StudentRepository import StudentRepository


class StudentService:
    def __init__(self, student_repository: StudentRepository):
        self.__student_repository = student_repository

    def add(self, new_student: Student):
        """
        Adds a new student to the service.

        :param new_student: Student
        :return: none
        """
        self.__student_repository.add(new_student)

    def delete(self, student: Student):
        """
        Deletes a student from the service ( repo ).

        :param student: Student
        :return: none
        """
        self.__student_repository.delete(student)

    def get_all(self):
        """
        Gets all the students.

        :return: dict, all the students
        """
        return self.__student_repository.get_all()

    def get_by_id(self, student_id):
        """

        :param student_id:
        :return:
        """
        for student in self.get_all():
            if student.get_student_id() == student_id:
                return student
        raise InexistingEntityError('inexisting student')

    def get_by_name(self, student_name):
        """

        :param student_name:
        :return:
        """
        for student in self.get_all():
            if student.get_name() == student_name:
                return student_name
        raise InexistingEntityError('inexisting student')

    def update(self, student: Student, new_student: Student):
        """

        :param student:
        :param new_student:
        :return:
        """
        self.__student_repository.update(student, new_student)

    def update_all(self, student_repository):
        """
        Updates the student repository to a new one.

        :param student_repository: list
        :return: none
        """
        self.__student_repository.update_all(student_repository)

    def find_id(self, student_id):
        """

        :param student_id:
        :return:
        """
        return self.__student_repository.find_id(student_id)

    def find_name(self, student_name):
        """

        :param student_name:
        :return:
        """
        return self.__student_repository.find_name(student_name)

    def find(self, student: Student):
        """
        Checks if a student is in our service.

        :param student: Student
        :return: bool
        """
        return self.__student_repository.find(student)

    def number_of_students(self):
        """
        Returns the total number of students.

        :return: int, the number of students in the service
        """
        return len(self.get_all())

    def get_student_by_id(self, stud_id):
        return self.__student_repository.get_student_by_id(stud_id)
