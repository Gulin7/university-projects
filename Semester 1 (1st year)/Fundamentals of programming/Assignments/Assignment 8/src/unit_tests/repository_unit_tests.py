import unittest

from src.domain.Discipline import Discipline
from src.domain.Grade import Grade
from src.domain.Student import Student
from src.repository.DisciplineRepository import DisciplineRepository
from src.repository.StudentRepository import StudentRepository
from src.repository.GradeRepository import GradeRepository
from src.exceptions.exceptions import *


class TestDisciplineRepository(unittest.TestCase):
    def set_up(self):
        new_repo = DisciplineRepository()

    def test_add_find_get(self):
        """
        Testing the get functions and the find ones, as well as adding a discipline.

        :return:
        """
        disc_repo = DisciplineRepository()
        disc_id = 2
        disc_name = 'Sport'
        disc = Discipline(disc_id, disc_name)
        self.assertEqual(len(disc_repo.get_all()), 0)
        disc_repo.add(disc)
        self.assertEqual(len(disc_repo.get_all()), 1)
        # testing if the disc added is truly the disc we wanted to add with getters
        self.assertEqual(disc_repo.get_discipline_by_id(disc_id), disc)
        self.assertEqual(disc_repo.get_discipline_by_name(disc_name), disc)
        # find functions
        self.assertEqual(disc_repo.find_id(disc_id), disc)
        self.assertEqual(disc_repo.find_name(disc_name), disc)
        self.assertEqual(disc_repo.find(disc), disc)
        # ADDING THE SAME ENTITY
        self.assertRaises(ExistingEntityError, disc_repo.add, disc)
        #
        self.assertEqual(disc_repo.get_all_names(), [disc_name])
        self.assertEqual(disc_repo.get_all_ids(), [disc_id])
        self.assertEqual(disc_repo.get_all(), [disc])

    def test_update(self):
        disc_repo = DisciplineRepository()
        disc_id = 2
        disc_name = 'Sport'
        disc = Discipline(disc_id, disc_name)
        disc_repo.add(disc)
        #
        new_id = 2
        new_name = 'History'
        new_disc = Discipline(new_id, new_name)
        disc_repo.update(disc, new_disc)
        self.assertEqual(disc_repo.get_discipline_by_name(new_name), new_disc)
        self.assertRaises(InexistingEntityError, disc_repo.get_discipline_by_name, disc_name)

    def test_delete(self):
        disc_repo = DisciplineRepository()
        disc_id = 2
        disc_name = 'Sport'
        disc = Discipline(disc_id, disc_name)
        disc_repo.add(disc)
        #
        new_id = 2
        new_name = 'History'
        new_disc = Discipline(new_id, new_name)
        self.assertRaises(InexistingEntityError, disc_repo.delete, new_disc)
        disc_repo.delete(disc)
        self.assertEqual(len(disc_repo.get_all()), 0)


class TestStudentRepository(unittest.TestCase):
    def set_up(self):
        new_repo = StudentRepository()

    def test_add(self):
        stud_repo = StudentRepository()
        stud_id = 2
        stud_name = 'Tudor'
        stud = Student(stud_id, stud_name)
        self.assertEqual(len(stud_repo.get_all()), 0)
        stud_repo.add(stud)
        self.assertEqual(len(stud_repo.get_all()), 1)

    def test_delete(self):
        stud_repo = StudentRepository()
        stud_id = 2
        stud_name = 'Tudor'
        student = Student(stud_id, stud_name)
        self.assertRaises(InexistingEntityError, stud_repo.delete, student)
        stud_repo.add(student)
        stud_repo.delete(student)
        self.assertEqual(len(stud_repo.get_all()), 0)

    def test_update(self):
        repo = StudentRepository()
        id = 3
        name = 'Tudor'
        name2 = 'Steve'
        student = Student(id, name)
        repo.add(student)
        self.assertRaises(InexistingEntityError, repo.update, Student(id, name2), Student(id, name2))
        repo.update(student, Student(id, name2))


class TestGradeRepository(unittest.TestCase):
    def set_up(self):
        new_repo = GradeRepository()

    def test_add(self):
        grade_repo = GradeRepository()
        stud_id = 1
        disc_id = 2
        value = 3
        grade = Grade(disc_id, stud_id, value)

    def test_delete(self):
        grade_repo = GradeRepository()
        stud_id = 1
        disc_id = 2
        grade_value = 5
        grade = Grade(disc_id, stud_id, grade_value)
        self.assertRaises(InexistingEntityError, grade_repo.delete, grade.get_id())
        grade_repo.add(grade)
        grade_repo.delete(grade.get_id())
        self.assertEqual(len(grade_repo.get_all()), 0)

    def test_update(self):
        grade_repo = GradeRepository()
        stud_id = 1
        disc_id = 2
        grade_value = 5
        grade = Grade(disc_id, stud_id, grade_value)
        grade_repo.add(grade)
        stud_id2 = 2
        grade2 = Grade(disc_id, stud_id2, grade_value)
        self.assertRaises(IdError, grade_repo.update, grade2, grade)
        grade_repo.update(grade, Grade(disc_id, stud_id, 1))
