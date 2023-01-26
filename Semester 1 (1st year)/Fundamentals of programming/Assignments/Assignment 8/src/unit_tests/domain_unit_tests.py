import unittest

from src.exceptions.exceptions import *
from src.domain.Discipline import Discipline
from src.domain.Student import Student
from src.domain.Grade import Grade

"""
3 PARTS:
ARRANGE = entry data
ACT = call functions
ASSERT = assert
"""


class TestDiscipline(unittest.TestCase):
    def test_discipline_ok(self):
        """
        This functions tests if we can create a Discipline ( we also use the gettters ).

        :return:
        """
        discipline_id = 5
        name = 'English'
        discipline = Discipline(discipline_id, name)
        invalid_id_message = "The ids are not the same!"
        invalid_name_message = "The names are not the same"
        self.assertEqual(discipline.get_discipline_id(), discipline_id, invalid_id_message)
        self.assertEqual(discipline.get_name(), name, invalid_name_message)

    def test_discipline_invalid_parameters(self):
        discipline_wrong_id_1 = 'Marcel'
        discipline_wrong_id_2 = -3
        discipline_name = 'English'
        error_message = "Something went wrong! 😢"
        self.assertRaises(InvalidDisciplineAttribute, Discipline, discipline_wrong_id_1, discipline_name)
        self.assertRaises(InvalidDisciplineAttribute, Discipline, discipline_wrong_id_2, discipline_name)

    def test_discipline_setters(self):
        discipline_id = 5
        name = 'English'
        discipline = Discipline(discipline_id, name)
        discipline_new_id = 7
        new_name = 'Romanian'
        discipline.set_discipline_id(discipline_new_id)
        discipline.set_name(new_name)
        self.assertEqual(discipline.get_discipline_id(), discipline_new_id)
        self.assertEqual(discipline.get_name(), new_name)


class TestStudent(unittest.TestCase):
    def test_student_ok(self):
        """
        This functions tests if we can create a Student ( we also use the gettters ).

        :return:
        """
        student_id = 5
        name = 'Marcel'
        student = Student(student_id, name)
        invalid_id_message = "The ids are not the same!"
        invalid_name_message = "The names are not the same"
        self.assertEqual(student.get_student_id(), student_id, invalid_id_message)
        self.assertEqual(student.get_name(), name, invalid_name_message)

    def test_student_invalid_parameters(self):
        student_wrong_id_1 = 'Marcel'
        student_wrong_id_2 = -3
        student_name = 'Rodica'
        self.assertRaises(InvalidStudentAttribute, Student, student_wrong_id_1, student_name)
        self.assertRaises(InvalidStudentAttribute, Student, student_wrong_id_2, student_name)

    def test_student_setters(self):
        student_id = 5
        name = 'Vasile din Botosani'
        student = Student(student_id, name)
        student_new_id = 7
        new_name = 'Romario'
        student.set_student_id(student_new_id)
        student.set_name(new_name)
        self.assertEqual(student.get_student_id(), student_new_id)
        self.assertEqual(student.get_name(), new_name)


class TestGrade(unittest.TestCase):
    def test_grade_ok(self):
        """
        This functions tests if we can create a GRADE ( we also use the gettters ).

        :return:
        """
        student_id = 5
        discipline_id = 3
        grade_value = 7
        grade = Grade(discipline_id, student_id, grade_value)
        invalid_id_message = "The ids are not the same!"
        invalid_name_message = "The names are not the same"
        self.assertEqual(grade.get_grade_student_id(), student_id, invalid_id_message)
        self.assertEqual(grade.get_grade_discipline_id(), discipline_id, invalid_id_message)
        self.assertEqual(grade.get_grade_value(), grade_value)

    def test_grade_invalid_parameters(self):
        valid_id = 2
        wrong_id_1 = 'Marcel'
        wrong_id_2 = -3
        grade_value = 3
        wrong_value = -2
        self.assertRaises(InvalidGradeAttribute, Grade, wrong_id_1, valid_id, grade_value)
        self.assertRaises(InvalidGradeAttribute, Grade, valid_id, wrong_id_2, grade_value)
        self.assertRaises(InvalidGradeValue, Grade, valid_id, valid_id, wrong_value)

    def test_grade_setters(self):
        student_id = 2
        student_new = 3
        discipline_id = 5
        discipline_new = 7
        grade_value = 5
        grade_new = 9
        grade = Grade(student_id, discipline_id, grade_value)
        grade.set_grade_value(grade_new)
        grade.set_student_id(student_new)
        grade.set_discipline_id(discipline_new)
        self.assertEqual(grade.get_grade_value(), grade_new)
        self.assertEqual(grade.get_grade_discipline_id(), discipline_new)
        self.assertEqual(grade.get_grade_student_id(), student_new)
