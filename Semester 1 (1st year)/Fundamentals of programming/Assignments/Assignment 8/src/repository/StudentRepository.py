import copy

from src.domain.Student import Student
from src.exceptions.exceptions import *


class StudentRepository:
    """
    CRUD OPERATIONS
    """

    def __init__(self):
        self.__student_repository = list()

    def add(self, new_student: Student):
        """
        Adds a new student.

        :param new_student: Student
        :return: none
        """
        for student in self.__student_repository:
            if student.get_student_id() == new_student.get_student_id():
                raise ExistingEntityError('existing student id')
        for student in self.__student_repository:
            if student.get_name() == new_student.get_name():
                raise ExistingEntityError('existing student name')
        self.__student_repository.append(new_student)

    def update(self, student: Student, new_student: Student):
        if student.get_student_id() != new_student.get_student_id():
            raise IdError('id cannot be changed')
        for index in range(len(self.__student_repository)):
            if self.__student_repository[index] == student:
                self.__student_repository[index] = new_student
                return
        raise InexistingEntityError('inexisting student')

    def update_all(self, new_student_repo):
        """
        Updates the whole repository.

        :param new_student_repo: StudentRepository
        :return:none
        """
        self.__student_repository = copy.deepcopy(new_student_repo)

    def delete(self, student: Student):
        """
        Deletes an existing student.

        :param student:Student
        :return:none
        """
        stud = self.find(student)
        if stud:
            self.__student_repository.remove(stud)
        else:
            raise InexistingEntityError('inexisting entity')

    def find_id(self, student_id):
        """

        :param student_id: int, student_id
        :return:bool
        """
        for student in self.__student_repository:
            if student.get_student_id() == student_id:
                return student
        return False

    def find_name(self, student_name):
        """

        :param student_name: str, student_name
        :return: bool
        """
        for student in self.__student_repository:
            if student.get_name() == student_name:
                return student
        return False

    def find(self, student: Student):
        """
        Finds a student.

        :param student: Student
        :return: bool
        """
        for stud in self.__student_repository:
            if student.is_equal(stud):
                return stud
        else:
            return False

    def get_all(self):
        """
        Gets all Students in the repository.

        :return: list
        """
        return self.__student_repository

    def get_all_names(self):
        names = []
        for student in self.__student_repository:
            names.append(student.get_name())
        return names

    def get_all_ids(self):
        ids = []
        for student in self.__student_repository:
            ids.append(student.get_student_id())
        return ids

    def get_student_by_id(self, stud_id):
        for student in self.__student_repository:
            if student.get_student_id() == int(stud_id):
                return student
        raise InexistingEntityError('inexisting student')
