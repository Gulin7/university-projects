import copy

from src.domain.Discipline import Discipline
from src.exceptions.exceptions import *


class DisciplineRepository:
    """
    CRUD OPERATIONS
    """

    def __init__(self):
        self.__discipline_repository = list()

    def add(self, new_discipline: Discipline):
        """
        Adds a new_discipline to the repostiory.

        :param new_discipline: Discipline
        :return: none
        """
        for discipline in self.__discipline_repository:
            if discipline.get_discipline_id() == new_discipline.get_discipline_id():
                raise ExistingEntityError('existing discipline id')
        self.__discipline_repository.append(new_discipline)

    def update(self, discipline: Discipline, new_discipline: Discipline):
        """
        Updates an existing discipline.

        :param new_discipline: Discipline
        :return: none
        """
        if discipline.get_discipline_id() != new_discipline.get_discipline_id():
            raise IdError('id cannot be changed')
        for index in range(len(self.__discipline_repository)):
            if self.__discipline_repository[index] == discipline:
                self.__discipline_repository[index] = new_discipline
                return
        raise InexistingEntityError('inexisting discipline')

    def update_all(self, new_discipline_repo: list):
        """
        Updates the discipline repository with a new one.

        :param new_discipline_repo: DisciplineRepository
        :return: none
        """
        self.__discipline_repository = copy.deepcopy(new_discipline_repo)

    def delete(self, discipline: Discipline):
        """
        Deletes an existing discipline.

        :param discipline: Discipline
        :return: none
        """
        disc = self.find(discipline)
        if not disc:
            raise InexistingEntityError('inexisting discipline')
        else:
            self.__discipline_repository.remove(disc)

    def get_all(self):
        """
        Gets all the disciplines in the repository.

        :return: dict, all disciplines in the repository
        """
        return self.__discipline_repository

    def get_all_names(self):
        names = []
        for discipline in self.get_all():
            names.append(discipline.get_name())
        return names

    def get_all_ids(self):
        ids = []
        for discipline in self.__discipline_repository:
            ids.append(discipline.get_discipline_id())
        return ids

    def find(self, discipline: Discipline):
        """

        :param discipline:
        :return:
        """
        for disc in self.__discipline_repository:
            if discipline.is_equal(disc):
                return disc
        return False

    def find_id(self, discipline_id):
        """

        :param discipline_id:
        :return:
        """
        for discipline in self.__discipline_repository:
            if discipline.get_discipline_id() == discipline_id:
                return discipline
        return False

    def find_name(self, discipline_name):
        """

        :param discipline_name:
        :return:
        """
        for discipline in self.__discipline_repository:
            if discipline.get_name() == discipline_name:
                return discipline
        return False

    def get_discipline_by_id(self, disc_id):
        for discipline in self.__discipline_repository:
            if discipline.get_discipline_id() == disc_id:
                return discipline
        raise InexistingEntityError('inexisting discipline')
