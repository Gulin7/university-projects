import copy


def partial_sol(lst):
    length = len(lst)
    for ind in range(length):
        for ind2 in range(ind + 1, length):
            if lst[ind] == lst[ind2]:
                return False
    for ind in range(0, length - 1):
        if abs(lst[ind] - lst[ind + 1]) == 1:
            return False
    if len(lst) < 4:
        return True
    one_between = [0] * length
    for ind in range(length - 2):
        if abs(lst[ind] - lst[ind + 2]) == 1:
            one_between[ind] = 1
            one_between[ind + 2] = 1
    two_between = [0] * length
    for ind in range(length - 3):
        if abs(lst[ind] - lst[ind + 3]) == 1:
            two_between[ind] = 1
            two_between[ind + 2] = 1
    for ind in range(length):
        if two_between[ind] == 0 and one_between[ind] == 0:
            return False

    return True


def backtrack(result, initial):
    for ind in range(1, len(initial) + 1):
        result.append(ind)
        if partial_sol(result):
            if len(result) == len(initial):
                print(result)
            else:
                backtrack(result, initial)
        result.pop()


def backtrack_it(initial):
    for ind in range(1, len(initial) + 1):
        stack = [[ind]]
        for j in range(1, len(initial) + 1):
            for k in stack:
                for f in range(1, len(initial) + 1):
                    b = copy.deepcopy(k)
                    b.append(f)
                    if partial_sol(b):
                        if b not in stack:
                            if len(b) == len(initial):
                                print(b)
                            stack.append(b)
        stack.clear()


if __name__ == '__main__':
    while True:
        try:
            lung = int(input('Enter a length: '))
            break
        except ValueError:
            print('Invalid length!')
    n = []
    for i in range(1, lung + 1):
        n.append(i)
    while True:
        try:
            option = int(input("""1 - Recursive backtracking
2- Iterative backtracking
"""))
            if 0 < option < 3:
                break
            print('Invalid option!')
        except ValueError:
            print('Invalid option!')
    if option == 1:
        backtrack([], n)
    else:
        backtrack_it(n)
