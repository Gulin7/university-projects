import copy

from src.domain.Grade import Grade
from src.exceptions.exceptions import *


class GradeRepository:
    """
        CRUD OPERATIONS
        """

    def __init__(self):
        self.__grade_repository = []

    def add(self, new_grade: Grade):
        """
        Adds a new grade.

        :param new_grade:Grade
        :return:none
        """
        self.__grade_repository.append(new_grade)

    def update(self, grade: Grade, new_grade: Grade):
        """
        Updates a grade.
        :param grade: Grade
        :param new_grade: Grade
        :return: none
        """
        if grade.get_id() != new_grade.get_id():
            raise IdError('id cannot be changed')
        for index in range(len(self.__grade_repository)):
            if self.__grade_repository[index] == grade:
                self.__grade_repository[index] = new_grade
                return
        raise InexistingEntityError('inexisting grade')

    def update_all(self, new_grade_repo):
        """
        Updates the repository to a new one.

        :param new_grade_repo: GradeRepository
        :return: none
        """
        self.__grade_repository = copy.deepcopy(new_grade_repo)

    def delete(self, grade_id):
        """
        Deletes grade that is in the repository.

        :param grade_id: grade_id
        :return: none
        """
        gr = self.find_id(grade_id)
        if gr:
            self.__grade_repository.remove(gr)
        else:
            raise InexistingEntityError('inexisting entity')

    def find_id(self, grade_id):
        """
        Checks if a grade is in the repository (only by student_id and discipline_id).

        :param grade_id: int, grade_id
        :return: bool, True if the grade_id is in repo
        """
        for grade in self.__grade_repository:
            if grade.get_id() == grade_id:
                return grade
        return False

    def find(self, grade: Grade):
        """
        Checks if a grade is in the repository.

        :param grade: Grade
        :return: bool, True if grade is in repository
        """
        for gr in self.__grade_repository:
            if grade.is_equal(gr):
                return gr
        return False

    def get_all(self):
        """
        Gets all the grades in the repository.

        :return: dict, all grades in repository
        """
        return self.__grade_repository

    def get_all_ids(self):
        ids = []
        for grade in self.__grade_repository:
            ids.append(grade.get_id())
        return ids
