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

    """
    GETTERS AND SETTERS
    """

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def set_student_id(self, new_id):
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
