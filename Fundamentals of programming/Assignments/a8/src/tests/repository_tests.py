from src.domain.Student import Student
from src.domain.Discipline import Discipline
from src.domain.Grade import Grade
from src.exceptions.exceptions import *
from src.repository.StudentRepository import StudentRepository
from src.repository.DisciplineRepository import DisciplineRepository
from src.repository.GradeRepository import GradeRepository


# todo: DO THE TESTS WITH PYUNIT TESTING
def run_student_repository_tests():
    # CREATE STUDENT 1
    stud_id1 = 5
    stud_name1 = 'Marcel'
    stud1 = Student(stud_id1, stud_name1)
    # CREATE STUDENT 2
    stud_id2 = 3
    stud_name2 = 'Dorian'
    stud2 = Student(stud_id2, stud_name2)
    # CREATE STUDENT REPOSITORY
    student_repo = StudentRepository()
    assert (len(student_repo.get_all()) == 0)
    # ASSERT ADD AND FIND_ID FUNCTIONS
    student_repo.add(stud1)
    assert (len(student_repo.get_all()) == 1)
    assert (student_repo.find(stud1))
    assert (not student_repo.find(stud2))
    # ASSERT DELETE FUNCTION
    try:
        student_repo.delete(stud2)
    except InexistingEntityError as iee:
        assert str(iee) == 'inexisting entity'
    # ASSERT ADD NO DUPLICATE ID
    student_repo.add(stud2)
    try:
        student_repo.add(stud2)
    except ExistingEntityError as eee:
        assert str(eee) == 'existing student id'
    assert (len(student_repo.get_all()) == 2)
    # ASSERT UPDATE AND FIND FUNCTION
    # create a student with the same id as student 1
    stud_name3 = 'Kanye West'
    stud3 = Student(stud_id1, stud_name3)
    """print(stud1, stud3)
    for student in student_repo.get_all():
        print(student)"""
    student_repo.update(stud1, stud3)
    assert (not student_repo.find(Student(stud_id1, stud_name1)))
    """for student in student_repo.get_all():
        print(student)
    print(stud3)"""
    assert (stud3 in student_repo.get_all())


def run_discipline_repository_tests():
    # CREATE FIRST DISCIPLINE
    discipline_id1 = 5
    discipline_name1 = 'Mathematics'
    discipline1 = Discipline(discipline_id1, discipline_name1)
    # CREATE SECOND DISCIPLINE
    discipline_id2 = 3
    discipline_name2 = 'Dorian'
    discipline2 = Discipline(discipline_id2, discipline_name2)
    # CREATE DISCIPLINE REPOSITORY
    discipline_repo = DisciplineRepository()
    # ASSERT LENGTH 0
    assert (len(discipline_repo.get_all()) == 0)
    # ASSERT ADD FIND_ID FUNCTION
    discipline_repo.add(discipline1)
    assert (len(discipline_repo.get_all()) == 1)
    assert (discipline_repo.find_id(discipline_id1))
    assert (not discipline_repo.find_id(discipline_id2))
    # ASSERT DELETE FUNCTION
    try:
        discipline_repo.delete(discipline2)
    except InexistingEntityError as iee:
        assert str(iee) == 'inexisting discipline'
    # ASSERT: CAN'T ADD DUPLICATE ID
    discipline_repo.add(discipline2)
    try:
        discipline_repo.add(discipline2)
    except ExistingEntityError as eee:
        assert str(eee) == 'existing discipline id' or str(eee) == 'existing discipline name'
    assert (len(discipline_repo.get_all()) == 2)
    # ASSERT UPDATE AND FIND FUNCTION
    discipline_name3 = 'Computational Logic'
    discipline3 = Discipline(discipline_id1, discipline_name3)
    discipline_repo.update(discipline1, discipline3)
    """for discipline in discipline_repo.get_all():
        print(discipline)
    print('-------------')
    print(discipline3)"""
    assert (not discipline_repo.find(Discipline(discipline_id1, discipline_name1)))
    assert (discipline_repo.find(discipline3))


def run_grade_repository_tests():
    # CREATE GRADE 1
    student_id1 = 5
    discipline_id1 = 3
    grade_value1 = 8
    grade1 = Grade(discipline_id1, student_id1, grade_value1)
    # CREATE GRADE 2
    student_id2 = 3
    discipline_id2 = 1
    grade_value2 = 10
    grade2 = Grade(discipline_id2, student_id2, grade_value2)
    # CREATE GRADE REPOSITORY
    grade_repo = GradeRepository()
    assert (len(grade_repo.get_all()) == 0)
    # ASSERT ADD FUNCTION AND FIND_ID FUNCTION
    grade_repo.add(grade1)
    assert (len(grade_repo.get_all()) == 1)
    assert (grade_repo.find_id(grade1.get_id()))
    assert (not grade_repo.find_id(grade2.get_id()))
    # ASSERT DEL FUNCTION
    try:
        grade_repo.delete(grade2)
    except InexistingEntityError as iee:
        assert str(iee) == 'inexisting entity'
    # ASSERT ADD NO DUPLICATE ID
    grade_repo.add(grade2)
    assert (len(grade_repo.get_all()) == 2)
    try:
        grade_repo.add(grade2)
    except ExistingEntityError as eee:
        assert str(eee) == 'existing grade'
    assert (len(grade_repo.get_all()) == 2)
    # ASSERT UPDATE AND FIND FUNCTION
    grade_value3 = 2
    grade3 = Grade(discipline_id1, student_id1, grade_value3)
    grade_repo.update(grade1, grade3)
    assert (grade_repo.find_id(grade1.get_id()))
    assert (not grade_repo.find(Grade(discipline_id1, student_id1, grade_value1)))
    assert (grade_repo.find(grade3))


def run_repository_tests():
    run_student_repository_tests()
    run_discipline_repository_tests()
    run_grade_repository_tests()
