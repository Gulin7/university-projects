import random

from src.domain.Grade import Grade
from src.exceptions.exceptions import *
from src.repository.GradeRepository import GradeRepository
from src.services.DisciplineService import DisciplineService
from src.services.StudentService import StudentService


class GradeService:
    def __init__(self, grade_repository: GradeRepository, discipline_service: DisciplineService,
                 stud_service: StudentService):
        self.__grade_repository = grade_repository  # self.__grade_repository  is a DICT of grades
        self.__discipline_service = discipline_service
        self.__student_service = stud_service
        self.__generate_grades()

    def add(self, new_grade: Grade):
        """
        Adds a grade to the service.

        :param new_grade: Grade
        :return: none
        """
        if not self.__student_service.find_id(new_grade.get_grade_student_id()):
            raise StudentOrDisciplineInexistingError('inexisting student or discipline')
        if not self.__discipline_service.find_id(new_grade.get_grade_discipline_id()):
            raise StudentOrDisciplineInexistingError('inexisting student or discipline')
        self.__grade_repository.add(new_grade)
        self.__discipline_service.add_grade(new_grade)
        self.__student_service.add_grade(new_grade)

    def delete(self, grade_id):
        """
        Deletes a grade.

        :param grade_id:
        :return:
        """
        if not self.__student_service.find_id(grade_id[1]):
            raise StudentOrDisciplineInexistingError('inexisting student or discipline')
        if not self.__discipline_service.find_id(grade_id[0]):
            raise StudentOrDisciplineInexistingError('inexisting student or discipline')
        # self.__student_service.delete(self.__student_service.get_student_by_id(grade_id[1]))
        # self.__discipline_service.delete(self.__discipline_service.get_discipline_by_id(grade_id[0]))
        self.__discipline_service.delete_grade(self.get_by_id(grade_id))
        self.__student_service.delete_grade(self.get_by_id(grade_id))
        self.__grade_repository.delete(grade_id)

    def get_all(self):
        """
        Gets all the grades from the service (repo).

        :return: dict
        """
        return self.__grade_repository.get_all()

    def get_by_id(self, grade_id):
        for grade in self.get_all():
            if grade.get_id() == grade_id:
                return grade

        return False

    def update(self, grade: Grade, new_grade: Grade):
        """

        :param grade:
        :param new_grade:
        :return:
        """
        self.__grade_repository.update(grade, new_grade)
        self.__discipline_service.update_grade(grade, new_grade)
        self.__student_service.update_grade(grade, new_grade)

    def update_all(self, new_grade_repo: GradeRepository):
        """
        Updates the service repository.

        :param new_grade_repo: GradeRepository
        :return: none
        """
        self.__grade_repository.update_all(new_grade_repo)

    def find_id(self, grade_id):
        """

        :param grade_id: grade_id
        :return: bool
        """
        return self.__grade_repository.find_id(grade_id)

    def find(self, grade: Grade):
        """
        Checks if a grade is in the service.

        :param grade:Grade
        :return: bool
        """
        return self.__grade_repository.find(grade)

    def number_of_grades(self):
        """
        Computes and return the number of grades.
        :return: int, number of grades
        """
        return len(list(self.get_all().values()))

    def __generate_grades(self):
        for discipline in self.__discipline_service.get_all():
            for student in self.__student_service.get_all():
                grade = Grade(discipline.get_discipline_id(), student.get_student_id(), random.randint(1, 10))
                self.add(grade)
