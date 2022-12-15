from dataclasses import dataclass

from src.exceptions.exceptions import *


@dataclass
class Grade:
    def __init__(self, discipline_id, student_id, grade_value):
        try:
            discipline_id = int(discipline_id)
            student_id = int(student_id)
            grade_value = int(grade_value)
            if grade_value < 1 or grade_value > 10:
                raise InvalidGradeValue('invalid grade_value')
            if discipline_id < 0:
                raise InvalidGradeAttribute('invalid attribute')
            if student_id < 0:
                raise InvalidGradeAttribute('invalid attribute')
        except ValueError:
            raise InvalidGradeAttribute('invalid attribute')
        self.__id = (discipline_id, student_id)
        self.__discipline_id = discipline_id
        self.__student_id = student_id
        self.__grade_value = grade_value

    """
    GETTERS AND SETTERS
    """

    def get_id(self):
        """
        Gets the id of the grade.

        :return: tuple, (discipline_id:int, student_id:int)
        """
        return self.__id

    def get_grade_discipline_id(self):
        """
        Gets the discipline id of the grade.

        :return: int
        """
        return self.__discipline_id

    def get_grade_student_id(self):
        """
        Gets the student id of the grade.

        :return: int
        """
        return self.__student_id

    def get_grade_value(self):
        """
        Gets the grade value of the grade.

        :return: int
        """
        return self.__grade_value

    def set_id(self, new_id):
        """
        SETS THE ID. DO NOT USE. THE ID IS SET WHEN THE GRADE IS CREATED.

        :param new_id:
        :return:
        """
        self.__id = new_id

    def set_discipline_id(self, new_discipline_id):
        """
        SETS THE DISCIPLINE ID. DO NOT USE. THE DISCIPLINE ID IS SET WHEN THE GRADE IS CREATED.

        :param new_discipline_id:
        :return:
        """
        self.__discipline_id = new_discipline_id

    def set_student_id(self, new_student_id):
        """
        SETS THE STUDENT ID. DO NOT USE. THE STUDENT ID IS SET WHEN THE GRADE IS CREATED.

        :param new_student_id:
        :return:
        """

        self.__student_id = new_student_id

    def set_grade_value(self, new_grade_value):
        """
        Sets a new grade value.

        :param new_grade_value: int
        :return:
        """
        if 1 > new_grade_value or new_grade_value > 10:
            raise InvalidGradeValue('invalid grade_value')
        self.__grade_value = new_grade_value

    """
    __STR__
    """

    def __str__(self):
        return f"Grade discipline_id:{self.get_grade_discipline_id()}, " \
               f"student_id: {self.get_grade_student_id()} " \
               f"grade_value: {self.get_grade_value()}"

    """
    IS EQUAL
    """

    def is_equal(self, other_grade):
        return self.get_id() == other_grade.get_id() and self.get_grade_value() == other_grade.get_grade_value()
