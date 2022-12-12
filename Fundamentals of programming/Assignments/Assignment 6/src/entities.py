def create_contestant(p1, p2, p3):
    return {"p1": p1, "p2": p2, "p3": p3}


def get_problem(contestant, problem):
    """
    Gets the score of a certain problem from a certain contestant.

    :param contestant: dict, contestant
    :param problem: p1/p2/p3
    :return: the contestants score for problem
    """
    return contestant[problem]


def set_problem(contestant, problem, score):
    """

    :param contestant: dict, contestant
    :param problem: p1/p2/p3
    :param score: int, between 0 and 10, the score for the given problem
    :return:
    """
    contestant[problem] = score
