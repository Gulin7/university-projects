class InexistingEntityError(Exception):
    pass


class ExistingEntityError(Exception):
    pass


class InvalidInput(Exception):
    pass


class InvalidStudentAttribute(Exception):
    pass


class InvalidDisciplineAttribute(Exception):
    pass


class InvalidGradeAttribute(Exception):
    pass


class InvalidGradeValue(Exception):
    pass


class StudentOrDisciplineInexistingError(Exception):
    pass


class IdError(Exception):
    pass
