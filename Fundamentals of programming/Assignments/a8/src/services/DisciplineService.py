from src.domain.Discipline import Discipline
from src.repository.DisciplineRepository import DisciplineRepository


class DisciplineService:
    def __init__(self, discipline_repository: DisciplineRepository):
        self.__discipline_repository = discipline_repository

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
