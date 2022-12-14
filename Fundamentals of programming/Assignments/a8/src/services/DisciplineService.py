import random

from src.domain.Discipline import Discipline
from src.domain.Grade import Grade
from src.repository.DisciplineRepository import DisciplineRepository


class DisciplineService:
    def __init__(self, discipline_repository: DisciplineRepository):
        self.__discipline_repository = discipline_repository
        self.__generate_disciplines()
        self.discipline_grades = []

    def add(self, new_discipline: Discipline):
        """
        Adds a discipline to the service (repo).

        :param new_discipline: Discipline
        :return: none
        """
        self.__discipline_repository.add(new_discipline)

    def delete(self, discipline: Discipline):
        """
        Deletes a discipline from the service (repo)
        :param discipline: Discipline
        :return: none
        """
        self.__discipline_repository.delete(discipline)

    def get_all(self):
        """
        Gets all the disciplines.

        :return: dict, all the disciplines
        """
        return self.__discipline_repository.get_all()

    def update(self, discipline: Discipline, new_discipline: Discipline):
        """

        :param discipline:
        :param new_discipline:
        :return:
        """
        self.__discipline_repository.update(discipline, new_discipline)

    def update_all(self, discipline_repo):
        """
        Updates the services repository.

        :param discipline_repo: list
        :return: none
        """
        self.__discipline_repository.update_all(discipline_repo)

    def find_id(self, discipline_id):
        """

        :param discipline_id:
        :return:
        """
        return self.__discipline_repository.find_id(discipline_id)

    def find(self, discipline: Discipline):
        """
        Checks if a discipline is in the service.

        :param discipline: Discipline
        :return: bool
        """
        return self.__discipline_repository.find(discipline)

    def number_of_disciplines(self):
        """
        Computes and returns the total number of disciplines.

        :return: int, number of disciplines
        """
        return len(self.get_all())

    def get_discipline_by_id(self, disc_id):
        return self.__discipline_repository.get_discipline_by_id(disc_id)

    def get_discipline_by_name(self, disc_name):
        return self.__discipline_repository.get_discipline_by_name(disc_name)

    def __generate_disciplines(self):
        list_of_disciplines = ['Mathematics', 'English', 'Romanian', 'Informatics', 'History', 'Geography', 'Biology']
        for i in range(1, 5):
            while True:
                try:
                    new_discipline = Discipline(i, random.choice(list_of_disciplines))
                    self.add(new_discipline)
                    break
                except:
                    pass

    def find_name(self, discipline_name):
        return self.__discipline_repository.find_name(discipline_name)

    def add_grade(self, grade: Grade):
        for discipline in self.__discipline_repository.get_all():
            if discipline.get_discipline_id() == grade.get_grade_discipline_id():
                discipline.add_grade(grade)

    def delete_grade(self, grade: Grade):
        for discipline in self.__discipline_repository.get_all():
            if discipline.get_discipline_id() == grade.get_grade_discipline_id():
                discipline.delete_grade(grade)

    def update_grade(self, grade: Grade, new_grade: Grade):
        for discipline in self.__discipline_repository.get_all():
            if discipline.get_discipline_id() == grade.get_grade_discipline_id():
                discipline.update_grade(grade, new_grade)
