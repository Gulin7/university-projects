import random
import copy


def generate_list(length):
    """
    Generates a list of random elements.

    :param: my_list: list
    :param: length: the length of the list
    :return: list, random elements
    """
    my_list = []
    for i in range(length):
        my_list.append(random.randint(1, 100))
    return my_list


def check_increasing(my_list):
    """
    Checks if a list is strictly increasing or not.

    :param my_list: list, int
    :return: true if the list is strictly increasing
    """
    length = len(my_list)
    if length == 0:
        return 0
    for i in range(1, length):
        if my_list[i] <= my_list[i - 1]:
            return 0
    return 1


def bt_rec(start, cur, lst):
    """
    This is a recursive backtracking way to generate all increasing subsets of a given list (lst).

    :param start: the starting index
    :param cur: the current subset
    :param lst: the list
    :return:
    """
    for ind in range(start, len(lst)):
        cur.append(lst[ind])
        if check_increasing(cur):
            print(cur)
            bt_rec(ind, cur, lst)
        cur.pop()


def bt_it(lst):
    length_list = len(lst)
    for ind in range(length_list):
        stack = [[lst[ind]]]
        if check_increasing(stack[0]):
            print(stack[0])
        for j in range(ind + 1, length_list):
            for k in stack:
                aux = copy.deepcopy(k)
                aux.append(lst[j])
                if check_increasing(aux):
                    print(aux)
                    stack.append(aux)
        stack.clear()


def check_if_equal(elements, k):
    """
    Checks if the elements of a list add up to k or not.

    :param elements: list, positive integers
    :param k: a positive integer
    :return: 1 if the sum is k, 0 if it's bigger and 2 if it's lower;
    we return 2 so inside the backtrack-function we know to backtrack that list of elements too(cause maybe we find a
    new element that adds up to k;
    if total>k we need to pop the last element, cause adding other elements would just result in an even bigger number
    """
    total = 0
    for index in elements:
        total += index
    if total == k:
        return 1
    elif total < k:
        return 2
    return 0


def dynamic_sum(my_list, sum):
    length = len(my_list)
    matrix = [[False for x in range(sum + 1)] for y in range(length + 1)]
    for i in range(length + 1):
        matrix[i][0] = True
    for i in range(1, length + 1):
        for j in range(1, sum + 1):
            if my_list[i - 1] > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = (matrix[i-1][j] or matrix[i-1][j-my_list[i-1]])
    if not matrix[length][sum]: #matrix[i][j]
        print('No solution :(')
    else:
        nr_of_elements = length
        final_result = []
        while sum > 0:
            if not matrix[nr_of_elements-1][sum]: # if it is false then the current element is used
                final_result.append(my_list[nr_of_elements-1])
                sum-=my_list[nr_of_elements-1]
            nr_of_elements -=1
        print(final_result)
