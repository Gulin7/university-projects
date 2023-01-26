from src.domain.Grade import Grade
from src.exceptions.exceptions import *


class Student:
    def __init__(self, student_id, name):
        try:
            student_id = int(student_id)
            if student_id < 0:
                raise InvalidStudentAttribute('invalid attribute')
        except ValueError:
            raise InvalidStudentAttribute('invalid attribute')
        self.__student_id = student_id
        self.__name = name
        self.__all_grades = []

    """
    GETTERS AND SETTERS
    """

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def set_student_id(self, new_id):
        try:
            new_id = int(new_id)
            if new_id < 1:
                raise InvalidDisciplineAttribute('invalid new id')
        except ValueError:
            raise InvalidDisciplineAttribute('invalid new id')
        self.__student_id = new_id

    def set_name(self, new_name):
        self.__name = new_name

    """
    __STR__
    """

    def __str__(self):
        return f"Student id: {self.get_student_id()}, name: {self.get_name()}"

    """
    IS EQUAL
    """

    def is_equal(self, other_student):
        return self.get_name() == other_student.get_name() and self.get_student_id() == other_student.get_student_id()

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
