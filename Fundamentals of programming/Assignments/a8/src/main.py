from src.repository.DisciplineRepository import DisciplineRepository
from src.repository.GradeRepository import GradeRepository
from src.repository.StudentRepository import StudentRepository
from src.services.DisciplineService import DisciplineService
from src.services.GradeService import GradeService
from src.services.StudentService import StudentService
from src.ui.console import Console
from src.tests.tests import run_all_tests


def main():
    run_all_tests()
    student_repository = StudentRepository()
    student_service = StudentService(student_repository)
    discipline_repository = DisciplineRepository()
    discipline_service = DisciplineService(discipline_repository)
    grade_repository = GradeRepository()
    grade_service = GradeService(grade_repository, discipline_service, student_service)
    console = Console(student_service, discipline_service, grade_service)
    console.run_console()


if __name__ == '__main__':
    main()
