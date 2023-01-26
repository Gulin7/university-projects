from src.domain.Grade import Grade
from src.exceptions.exceptions import InvalidDisciplineAttribute


class Discipline:
    def __init__(self, discipline_id, name):
        try:
            discipline_id = int(discipline_id)
            if discipline_id < 0:
                raise InvalidDisciplineAttribute('invalid attribute')
        except ValueError:
            raise InvalidDisciplineAttribute('invalid attribute')
        self.__discipline_id = discipline_id
        self.__name = name
        self.__all_grades = []

    """
    GETTERS AND SETTERS
    """

    def get_discipline_id(self):
        return self.__discipline_id

    def get_name(self):
        return self.__name

    def set_discipline_id(self, new_id):
        try:
            new_id = int(new_id)
            if new_id < 1:
                raise InvalidDisciplineAttribute('invalid new id')
        except ValueError:
            raise InvalidDisciplineAttribute('invalid new id')
        self.__discipline_id = new_id

    def set_name(self, new_name):
        self.__name = new_name

    """
    __STR__
    """

    def __str__(self):
        return f"Discipline id:{self.get_discipline_id()}, name:{self.get_name()}"

    """
    IS EQUAL
    """

    def is_equal(self, other_discipline):
        return self.get_name() == other_discipline.get_name() and self.get_discipline_id() == other_discipline.get_discipline_id()

    """
    GRADES
    """

    def add_grade(self, grade: Grade):
        self.__all_grades.append(grade)

    def delete_grade(self, grade: Grade):
        self.__all_grades.remove(grade)

    def update_grade(self, grade: Grade, new_grade: Grade):
        for _grade in self.__all_grades:
            if _grade == grade:
                _grade = new_grade
                return

    def get_average_grade(self):
        average = 0
        total = 0
        for grade in self.__all_grades:
            total += 1
            average += grade.get_grade_value()
        return average / total
