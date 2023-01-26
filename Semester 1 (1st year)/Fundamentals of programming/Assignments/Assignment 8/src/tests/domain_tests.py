from src.domain.Student import Student
from src.domain.Discipline import Discipline
from src.domain.Grade import Grade
from src.exceptions.exceptions import *


def run_grade_tests():
    # CREATE GRADE 1
    student_id1 = 1
    discipline_id1 = 1
    grade_value_1 = 10
    grade1 = Grade(discipline_id1, student_id1, grade_value_1)
    # ASSERT GRADE CREATION, GETTERS
    assert (grade1.get_id() == (discipline_id1, student_id1))
    assert (grade1.get_grade_discipline_id() == discipline_id1)
    assert (grade1.get_grade_student_id() == student_id1)
    assert (grade1.get_grade_value() == grade_value_1)
    # ASSERT SETTERS
    grade_value_2 = 8
    grade1.set_grade_value(grade_value_2)
    assert (grade1.get_grade_value() == grade_value_2)
    # ASSERT INVALID INPUT
    try:
        grade2 = Grade(discipline_id1, 'Lionel Messi wins the World Cup', grade_value_2)
    except InvalidGradeAttribute as iga:
        assert str(iga) == 'invalid attribute'
    try:
        grade2 = Grade('Lionel Messi wins the World Cup', student_id1, grade_value_1)
    except InvalidGradeAttribute as iga:
        assert str(iga) == 'invalid attribute'
    try:
        grade2 = Grade(discipline_id1, student_id1, 'Lionel Messi wins the World Cup')
    except InvalidGradeAttribute as iga:
        assert str(iga) == 'invalid attribute'
    # ASSERT INVALID INPUT FOR SETTER
    grade_value_3 = 15
    try:
        grade1.set_grade_value(grade_value_3)
    except InvalidGradeValue as igv:
        assert str(igv) == 'invalid grade_value'


def run_discipline_tests():
    id1 = 1
    name1 = 'Fundamentals of Programming'
    discipline1 = Discipline(id1, name1)
    assert (discipline1.get_discipline_id() == id1)
    assert (discipline1.get_name() == name1)
    id2 = 3
    name2 = 'Computer System Arhitecture'
    discipline1.set_discipline_id(id2)
    discipline1.set_name(name2)
    assert (discipline1.get_discipline_id() == id2)
    assert (discipline1.get_name() == name2)
    # ASSERT INVALID INPUT
    id3 = 'Marcel'
    try:
        discipline3 = Discipline(id3, name1)
    except InvalidDisciplineAttribute as ida:
        assert str(ida) == 'invalid attribute'


def run_student_tests():
    id1 = 1
    name1 = 'Tudor Gulin'
    student1 = Student(id1, name1)
    assert (student1.get_student_id() == id1)
    assert (student1.get_name() == name1)
    id2 = 2
    name2 = 'Lionel Messi'
    student2 = Student(id2, name2)
    assert (student2.get_student_id() == id2)
    assert (student2.get_name() == name2)
    student2.set_student_id(id1)
    student2.set_name(name1)
    assert (student1.get_student_id() == student2.get_student_id())
    assert (student1.get_name() == student2.get_name())
    # ASSERT INVALID INPUT
    id3 = 'Donattelo Mbappe Stupid Ninja Turtle'
    try:
        student3 = Student(id3, name1)
    except InvalidStudentAttribute as isa:
        assert str(isa) == 'invalid attribute'


def run_domain_tests():
    run_student_tests()
    run_discipline_tests()
    run_grade_tests()
