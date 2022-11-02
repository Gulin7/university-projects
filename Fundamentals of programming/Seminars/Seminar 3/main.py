def check_for_number(l, x):
    """
    Checks if a given element is part of a given list.

    :param l: list,unsorted
    :param x: int/float
    :return: True if x is in the list, False if not ( bools )
    """
    if len(l) == 0:
        return False
    if l[0] == x:
        return True
    return check_for_number(l[1:], x)


def binary_search(l, x):
    """
    Searches for a number in a sorted list.

    :param l: list, sorted, only numbers
    :param x: int/float
    :return: True if x is in l, False otherwise
    """
    mid = len(l) // 2
    if len(l) == 0:
        return False
    if x == l[mid]:
        return True
    if x > l[mid]:
        return binary_search(l[mid + 1:], x)
    return binary_search(l[:mid], x)


def bubble_sort(l):
    """
    Sort a list using the bubble sort.

    :param l: list, unsorted, only numbers
    :return:
    """
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]
            ok = 1
    while ok == 1:
        ok = 0
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                ok = 1


def merge(left, right):
    """
    Merges 2 sorted lists into a 3rd sorted one.

    :param left: list,sorted
    :param right: list,sorted
    :return:
    """
    result = []
    while 0 < len(left) and 0 < len(right):
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    result.extend(left + right)


def merge_sort(l):
    """
    Sorts a list using the merge sort.

    :param l: list
    :return:
    """
    if len(l) < 2:
        return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)


def print_options():
    pass


def run_menu():
    """
    Menu for lab!
    
    Option 1 Basic search
    Option 2 Binary search
    Option 3 
    :return: 
    """
    commands = { 1: check_for_number, 2:binary_search}
    while True:
        print_options()
        option = input("Choose a command: ")
        if option == 'x':
            break
        option=int(option)
        commands[option]()

if __name__ == '__main__':
    run_menu()
    """
    Binary_search + bubble sort:
    
    my_list = [4, 6, 3, 2, 2, 6, 8, 6, 4, 3, 2, 1,75,54,5,42,4,33,56,45,7,46,5,6,5,8,64,84,8,6,8,65,657567,57,65,7,35,5,543,4543,5]
    bubble_sort(my_list)
    x=int(input("Check for a number: "))
    print(check_for_number(my_list,x))
    """
    """
    First function:
    
    my_list = [1,2,3,4,5,6,12,13,4,5,9,2,3,5,6,0]
    x=int(input("Enter a number: "))
    if check_for_number(my_list,7):
        print(" :P ")
    """
