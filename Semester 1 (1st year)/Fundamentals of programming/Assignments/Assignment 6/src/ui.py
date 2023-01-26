#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import copy

import entities
import operations


def read_command():
    """
    Reads a command from the console and returns the command as well as other possible parameters.

    :return:
    """
    command = input("Enter a command: ")
    command = command.lower()
    pos = command.find(" ")
    if pos == -1:
        return command, []
    cmd = command[:pos]
    args = command[pos + 1:]
    args = args.split(',')
    args = [s.strip() for s in args]
    args = args[0].split(' ')
    return cmd, args


def add_contestant(all_contestants, p1, p2, p3):
    """
    Adds a new contestants with scores p1,p2,p3 to the list of all contestants.

    :param all_contestants: list of dicts, representing the contestants
    :param p1: score for problem 1
    :param p2: score for problem 2
    :param p3: score for problem 3
    :return:
    """
    try:
        p1 = int(p1)
        p2 = int(p2)
        p3 = int(p3)
        if 0 > p1 or p1 > 10 or 0 > p2 or p2 > 10 or 0 > p3 or p3 > 10:
            print('Invalid command!')
        else:
            operations.add_contestant(all_contestants, p1, p2, p3)
    except ValueError as ve:
        print("Invalid input! ", ve)


def insert_contestant(all_contestants, p1, p2, p3, aux, position):
    """
    Insert a new contestants with scores p1,p2,p3 at (=aux) at position.

    :param all_contestants: list of dicts, representing the contestants
    :param p1: score for problem 1
    :param p2: score for problem 2
    :param p3: score for problem 3
    :param aux: it's supossed to be at / At / aT for the command to be valid
    :param position: the position where we will insert the new contestant
    :return:
    """
    if aux.lower() != "at":
        print("Invalid command! < insert p1 p2 p3 at position >")
    else:
        try:
            p1 = int(p1)
            p2 = int(p2)
            p3 = int(p3)
            position = int(position)
            if 0 > p1 or p1 > 10 or 0 > p2 or p2 > 10 or 0 > p3 or p3 > 10 or position < 0:
                print('Invalid command!')`
            else:
                operations.insert_contestant(all_contestants, p1, p2, p3, position)
        except ValueError as ve:
            print("Invalid input! ", ve)


def remove_contestant(all_contestants, *args):
    """
    Removes one or more contestants, depending on the given arguments.

    :param all_contestants: list of dicts, representing all the contestants
    :param args: can be:
    integer - representing the position we want to remove
    "integer1 to integer2" - meaning that we remove all participants from positions integer1 to integer2
    :return:
    """
    if len(args) == 1:
        # MAKE THE SCORE 0
        try:
            position = int(args[0]) - 1
            contestant = all_contestants[position]
            entities.set_problem(contestant, "p1", 0)
            entities.set_problem(contestant, "p2", 0)
            entities.set_problem(contestant, "p3", 0)
        except ValueError as ve:
            print("Invalid command!", ve)
        except IndexError as ie:
            print("Invalid command!", ie)
        except:
            print("Invalid command!")
        # REMOVE THE CONTESTANT FROM THE LIST
        """ 
        try:
            all_contestants.pop(int(args[0]) - 1)
        except ValueError as ve:
            print("Invalid command!", ve)
        except IndexError as ie:
                print("Invalid command!", ie)
        except:
            print("Invalid command!")
        """
    elif len(args) == 2:
        try:
            score = int(args[1])
            if args[0] == '=':
                for contestant in all_contestants:
                    total = int(
                        int(entities.get_problem(contestant, "p1")) + int(entities.get_problem(contestant, "p2")) +
                        int(entities.get_problem(contestant, "p3")))
                    if (total / 3) == score:
                        entities.set_problem(contestant, "p1", 0)
                        entities.set_problem(contestant, "p2", 0)
                        entities.set_problem(contestant, "p3", 0)
            elif args[0] == '<':
                for contestant in all_contestants:
                    total = int(
                        int(entities.get_problem(contestant, "p1")) + int(entities.get_problem(contestant, "p2")) +
                        int(entities.get_problem(contestant, "p3")))
                    if (total / 3) < score:
                        entities.set_problem(contestant, "p1", 0)
                        entities.set_problem(contestant, "p2", 0)
                        entities.set_problem(contestant, "p3", 0)
            elif args[0] == '>':
                for contestant in all_contestants:
                    total = int(
                        int(entities.get_problem(contestant, "p1")) + int(entities.get_problem(contestant, "p2")) +
                        int(entities.get_problem(contestant, "p3")))
                    if (total / 3) > score:
                        entities.set_problem(contestant, "p1", 0)
                        entities.set_problem(contestant, "p2", 0)
                        entities.set_problem(contestant, "p3", 0)
            else:
                print("Invalid command!")
        except ValueError as ve:
            print("Invalid command!", ve)
        except IndexError as ie:
            print("Invalid command!", ie)
    elif len(args) == 3:
        if args[1].lower() != 'to':
            print("Invalid command!")
        else:
            # MAKE THE SCORES 0
            try:
                start = int(args[0]) - 1
                finish = int(args[2])
                for i in range(start, finish):
                    try:
                        contestant = all_contestants[i]
                        entities.set_problem(contestant, "p1", 0)
                        entities.set_problem(contestant, "p2", 0)
                        entities.set_problem(contestant, "p3", 0)
                    except ValueError as ve:
                        print("Invalid command!", ve)
            except ValueError as ve:
                print("Invalid command!", ve)
            except IndexError as ie:
                print("Invalid command!", ie)
            except:
                print("Invalid command!")
            # REMOVE THE CONTESTANT FROM THE LIST ENTIRELY
            """
            try:
                start = int(args[0]) - 1
                finish = int(args[2])
                for i in range(start, finish):
                    all_contestants.pop(start)
                undo_list.append(all_contestants)
            except ValueError as ve:
                print("Invalid command!", ve)
            """
    else:
        print("Invalid command!")


def print_options(commands):
    """
    Print's the commands menu to the console.

    :param commands: dictionary, representing the commands
    :return:
    """
    print("     OPTIONS MENU:")
    print(*list(commands.keys()), "exit", sep="\n")


def print_all(all_contestants, *args):
    """
    This function prints a list or sublist of participants, depending on the arguments given.

    :param all_contestants: list of dictionaries, representing the list of all contestants
    :param args: a set of given arguments, that can be:
    sorted - therefor, the function will print the sorted list of contestants
    < || = || > number - the function will print all the contestants that have an average < || = || > to the given num
    :return: -
    """
    if len(args) < 1:
        print(f"The contestants are: {all_contestants}!")
    elif len(args) == 1:
        if args[0] != 'sorted':
            print("Invalid command!")
        else:
            print(f"The contestants in sorted order are: {operations.sort_contestants(all_contestants)}! ")
    else:
        printed = 0
        try:
            score = int(args[1])
            if args[0] == '=':
                for contestant in all_contestants:
                    total = int((entities.get_problem(contestant, "p1") + entities.get_problem(contestant, "p2") +
                                 entities.get_problem(contestant, "p3")))
                    if (total / 3) == score:
                        print(contestant)
                        printed += 1
            elif args[0] == '<':
                for contestant in all_contestants:
                    total = int((entities.get_problem(contestant, "p1") + entities.get_problem(contestant, "p2") +
                                 entities.get_problem(contestant, "p3")))
                    if (total / 3) < score:
                        print(contestant)
                        printed += 1
            elif args[0] == '>':
                for contestant in all_contestants:
                    total = int((entities.get_problem(contestant, "p1") + entities.get_problem(contestant, "p2") +
                                 entities.get_problem(contestant, "p3")))
                    if (total / 3) > score:
                        print(contestant)
                        printed += 1
            elif args[0] == '>=':
                for contestant in all_contestants:
                    total = int((entities.get_problem(contestant, "p1") + entities.get_problem(contestant, "p2") +
                                 entities.get_problem(contestant, "p3")))
                    if (total / 3) >= score:
                        print(contestant)
                        printed += 1
            elif args[0] == '<=':
                for contestant in all_contestants:
                    total = int((entities.get_problem(contestant, "p1") + entities.get_problem(contestant, "p2") +
                                 entities.get_problem(contestant, "p3")))
                    if (total / 3) <= score:
                        print(contestant)
                        printed += 1
            else:
                print("Invalid command!")
            if printed == 0:
                print("No contestants found!")
        except ValueError as ve:
            print("Invalid command!", ve)


def replace_contestant(all_contestants, position, problem, aux, score):
    """
    Replaces the score for one for the 3 problems for one of the contestants.

    :param all_contestants: list, representing the contestants
    :param position: the contestants whose score we want to change
    :param problem: the problem that we want to change
    :param aux: "with"
    :param score: the new score
    :return:
    """
    problem = problem.lower()
    if (problem != "p1" and problem != "p2" and problem != "p3") or aux.lower() != "with":
        print("Invalid command!")
    else:
        try:
            position = int(position)
            score = int(score)
            if position > len(all_contestants):
                print(f"There are less than {position} contestant(s)!")
            elif score > 10 or score < 0:
                print("Invalid score!")
            else:
                operations.replace_contestants(all_contestants, position, problem, score)
                # entities.set_problem(all_contestants[position - 1], problem, score)
                # all_contestants[position - 1][problem] = score
        except ValueError as ve:
            print("Invalid command!", ve)


def print_top(all_contestants, *args):
    """
    Prints the top contestants.

    :param all_contestants: list of dicts, representing all the contestants
    :param args: a set of arguments that specify how many contestants should be shown
    number - the top "number" of contestants
    number p1/p2/p3 - the top "number" of contestants by problem p1/p2/p3
    :return:
    """
    if len(args) == 1:
        try:
            number = int(args[0])
            if number == 0:
                print("Can't do the top 0!")
            else:
                top = operations.sort_contestants(all_contestants)
                top = top[::-1]
                for i in range(number):
                    print(f"Contestant number {i + 1} is: {top[i]}!")
        except ValueError as ve:
            print("Invalid command!", ve)
        except IndexError as ie:
            print("Not enough contestants!", ie)
    elif len(args) == 2:
        problem = args[1].lower()
        if problem == "p1" or problem == "p2" or problem == "p3":
            try:
                number = int(args[0])
                if number == 0:
                    print("Can't do the top 0!")
                else:
                    top = operations.sort_contestants_by_problem(all_contestants, problem)
                    top = top[::-1]
                    for i in range(number):
                        print(f"Contestant number {i + 1} is: {top[i]}!")
            except ValueError as ve:
                print("Invalid command!", ve)
            except IndexError as ie:
                print("Not enough contestants!", ie)
            except:
                print("Invalid command!")
        else:
            print("Invalid command!")


def run_console():
    """
    This is the functions that runs the application.

    :return:
    """
    commands = {
        "add": add_contestant,
        "insert": insert_contestant,
        "remove": remove_contestant,
        "replace": replace_contestant,
        "list": print_all,
        "top": print_top,
        "clear": operations.clear_contestants_list,
    }
    undo_list = []
    all_contestants = operations.create_random_contestants(10)
    while True:
        print_options(commands)
        cmd, args = read_command()
        if cmd == "exit":
            print("You've left the app! :(")
            break
        elif cmd == "undo":
            if len(undo_list) != 0:
                all_contestants = copy.deepcopy(undo_list.pop())
            else:
                print("There's nothing to be undone! :P")
        else:
            try:
                initial = copy.deepcopy(all_contestants)
                commands[cmd](all_contestants, *args)
                if initial != all_contestants:
                    undo_list.append(initial)
            except KeyError as ke:
                print("Invalid command!", ke)
            except TypeError as te:
                print("Invalid command!", te)
            except ValueError as ve:
                print("Invalid command!", ve)
            except:
                print("Invalid command!")
