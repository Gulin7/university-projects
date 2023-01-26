import entities
import copy
import random


def add_contestant(all_contestants: list, *scores):
    """
    Adds a new participants to the list of contestants.

    :param all_contestants: list of dicts, representing all the contestants
    :param scores: the scores for problem 1,2,3 of the new participant
    :return:
    """
    if len(scores) != 3:
        print('INVALID COMMAND!')
    else:
        contestant = entities.create_contestant(scores[0], scores[1], scores[2])
        all_contestants.append(contestant)


def insert_contestant(all_contestants: list, *args):
    """
    Inserts a new contestant to the list of all participants.

    :param all_contestants:
    :param args: p1 p2 p3 "at" position-> 3 integers "at" integer , representing:
    the set of arguments, representing the 3 problem scored and "at" + the position where we insert the new contestants
    :return:
    """
    if len(args) != 4:
        print('INVALID COMMAND!')
    else:
        contestant = entities.create_contestant(args[0], args[1], args[2])
        all_contestants.insert(args[3] - 1, contestant)


def sort_contestants(contestants: list):
    """

    :param contestants: list , representing
    :return: the list of contestants, sorted by their average scores
    """
    all_contestants = copy.deepcopy(contestants)
    for i in range(len(all_contestants)):
        for j in range(0, len(all_contestants) - i - 1):
            total_1 = int(
                entities.get_problem(all_contestants[j], "p1") + entities.get_problem(all_contestants[j], "p1")
                + entities.get_problem(all_contestants[j], "p1"))
            total_2 = int(
                entities.get_problem(all_contestants[j+1], "p1") + entities.get_problem(all_contestants[j + 1], "p2")
                + entities.get_problem(all_contestants[j + 1], "p3"))
            if total_1 > total_2:
                aux = all_contestants[j]
                all_contestants[j] = all_contestants[j + 1]
                all_contestants[j + 1] = aux
    return all_contestants


def sort_contestants_by_problem(contestants: list, problem):
    all_contestants = copy.deepcopy(contestants)
    for i in range(len(all_contestants)):
        for j in range(0, len(all_contestants) - i - 1):
            total_1 = int((all_contestants[j][problem]))
            total_2 = int((all_contestants[j + 1][problem]))
            if total_1 > total_2:
                aux = all_contestants[j]
                all_contestants[j] = all_contestants[j + 1]
                all_contestants[j + 1] = aux
    return all_contestants


def clear_contestants_list(all_contestants):
    """
    Clears the list of all contestants.

    :param all_contestants: list of dicts, representing the contestants
    :return:
    """
    all_contestants.clear()


def undo_operations(all_contestants):
    """
    Clears the list of all contestants.

    :param all_contestants: list of dicts, representing the contestants
    :return:
    """
    all_contestants.clear()


def create_random_contestants(number):
    """
    Creates a list of contestants with random scores.

    :param all_contestants: list, representing all the contestants
    :param number:
    :return: returns the list of new contestants
    """
    all_contestants = []
    for i in range(number):
        all_contestants.append(
            entities.create_contestant(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)))
    return all_contestants
