import unittest

from src.domain.Student import Student
from src.domain.Grade import Grade
from src.domain.Discipline import Discipline
from src.exceptions.exceptions import *
from src.repository.StudentRepository import StudentRepository
from src.repository.GradeRepository import GradeRepository
from src.repository.DisciplineRepository import DisciplineRepository
from src.services.DisciplineService import DisciplineService
from src.services.GradeService import GradeService
from src.services.StudentService import StudentService


class TestDisciplineService(unittest.TestCase):
    def set_up(self):
        disc_repo = DisciplineRepository()
        disc_service = DisciplineService(disc_repo)

    def test_add(self):
        disc_repo = DisciplineRepository()
        disc_service = DisciplineService(disc_repo)
        disc_id = 7
        disc_name = 'Sport'
        disc = Discipline(disc_id, disc_name)
        disc_name_2 = 'English'
        disc_id_2 = 19
        disc_2 = Discipline(disc_id_2, disc_name_2)
        disc_service.add(disc)
        self.assertRaises(ExistingEntityError, disc_service.add, disc)
        self.assertEqual(5, len(disc_service.get_all()))

    def test_delete(self):
        disc_repo = DisciplineRepository()
        disc_service = DisciplineService(disc_repo)
        disc_id = 7
        disc_name = 'Sport'
        disc = Discipline(disc_id, disc_name)
        disc_name_2 = 'English'
        disc_id_2 = 19
        disc_2 = Discipline(disc_id_2, disc_name_2)
        self.assertRaises(InexistingEntityError, disc_service.delete, disc)
        disc_service.add(disc)
        disc_service.delete(disc)
        self.assertEqual(4, len(disc_service.get_all()))

    def test_update(self):
        disc_repo = DisciplineRepository()
        disc_service = DisciplineService(disc_repo)
        disc_id = 7
        disc_name = 'Sport'
        disc = Discipline(disc_id, disc_name)
        disc_name_2 = 'English'
        disc_id_2 = 19
        disc_2 = Discipline(disc_id_2, disc_name_2)
        self.assertRaises(InexistingEntityError, disc_service.update, disc, disc)
        disc_service.add(disc)
        self.assertRaises(IdError, disc_service.update, disc, disc_2)
        disc_service.update(disc, Discipline(disc_id, disc_name_2))


class TestStudentService(unittest.TestCase):
    def set_up(self):
        new_repo = StudentRepository()
        new_service = StudentService(new_repo)

    def test_add(self):
        stud_repo = StudentRepository()
        stud_service = StudentService(stud_repo)
        stud_id = 12
        stud_name = 'Tudor'
        stud = Student(stud_id, stud_name)
        stud_service.add(stud)
        self.assertEqual(stud, stud_service.find_id(stud_id))
        self.assertEqual(stud, stud_service.find_name(stud_name))

    def test_delete(self):
        stud_repo = StudentRepository()
        stud_service = StudentService(stud_repo)
        stud_id = 12
        stud_name = 'Tudor'
        student = Student(stud_id, stud_name)
        self.assertRaises(InexistingEntityError, stud_service.delete, student)
        stud_service.add(student)
        stud_service.delete(student)
        self.assertEqual(len(stud_service.get_all()), 4)  # 4 are randomly generated

    def test_update(self):
        repo = StudentRepository()
        stud_service = StudentService(repo)
        id = 13
        name = 'Tudor'
        name2 = 'Steve'
        student = Student(id, name)
        stud_service.add(student)
        self.assertRaises(InexistingEntityError, stud_service.update, Student(id, name2), Student(id, name2))
        stud_service.update(student, Student(id, name2))


class TestGradeService(unittest.TestCase):
    def set_up(self):
        grade_repo = GradeRepository()
        stud_repo = StudentRepository()
        disc_repo = DisciplineRepository()
        disc_service = DisciplineService(disc_repo)
        stud_service = StudentService(stud_repo)
        grade_service = GradeService(grade_repo, disc_service, stud_service)

    def test_add(self):
        grade_repo = GradeRepository()
        stud_repo = StudentRepository()
        disc_repo = DisciplineRepository()
        disc_service = DisciplineService(disc_repo)
        stud_service = StudentService(stud_repo)
        grade_service = GradeService(grade_repo, disc_service, stud_service)
        stud_id1 = 6
        stud_name1 = 'Giulia'
        stud1 = Student(stud_id1, stud_name1)
        disc_id1 = 9
        disc_name1 = 'Sport'
        disc1 = Discipline(disc_id1, disc_name1)
        grade_value1 = 10
        grade1 = Grade(disc_id1, stud_id1, grade_value1)

    def test_delete(self):
        grade_repo = GradeRepository()
        stud_repo = StudentRepository()
        disc_repo = DisciplineRepository()
        disc_service = DisciplineService(disc_repo)
        stud_service = StudentService(stud_repo)
        grade_service = GradeService(grade_repo, disc_service, stud_service)
        stud_id1 = 6
        stud_name1 = 'Giulia'
        stud1 = Student(stud_id1, stud_name1)
        disc_id1 = 9
        disc_name1 = 'Sport'
        disc1 = Discipline(disc_id1, disc_name1)
        grade_value1 = 10
        grade1 = Grade(disc_id1, stud_id1, grade_value1)
        grade_service.add(grade1)
        self.assertEqual(grade1, grade_service.get_by_id(grade1.get_id()))
        self.assertEqual(grade1, grade_service.find(grade1))
        self.assertEqual(grade1, grade_service.find_id(grade1.get_id()))

    def test_update(self):
        grade_repo = GradeRepository()
        stud_repo = StudentRepository()
        disc_repo = DisciplineRepository()
        disc_service = DisciplineService(disc_repo)
        stud_service = StudentService(stud_repo)
        grade_service = GradeService(grade_repo, disc_service, stud_service)
        stud_id1 = 6
        stud_name1 = 'Giulia'
        stud1 = Student(stud_id1, stud_name1)
        disc_id1 = 9
        disc_name1 = 'Sport'
        disc1 = Discipline(disc_id1, disc_name1)
        grade_value1 = 10
        grade1 = Grade(disc_id1, stud_id1, grade_value1)
