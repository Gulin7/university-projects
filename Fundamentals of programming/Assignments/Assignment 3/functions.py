import random
import time


def insert_sort(my_list, step):
    """
    Insertion sort
    :param my_list: list, unsorted, to be sorted
    :param step: the frequency we are printing
    :return:
    """
    length = len(my_list)
    current_step = 0
    for i in range(1, length):
        aux = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > aux:
            """aux=the value to be inserted; we go through the list and for every element bigger than aux 
            we move the element on the current position to the left;once aux is bigger than our current element 
            we insert it on the above position"""
            my_list[j + 1] = my_list[j]
            j = j - 1
        my_list[j + 1] = aux
        current_step += 1
        if current_step == step:
            current_step = 0
            print(my_list)


def comb_sort(my_list, step):
    gap = len(my_list)
    ok = True
    current_step = 0
    while ok or gap > 1:
        gap = max(1, int(gap / 1.3))
        ok = False
        for i in range(len(my_list) - gap):
            j = i + gap
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
                ok = True
                current_step += 1
                if current_step == step:
                    current_step = 0
                    print(my_list)


# under we have the functions without the step counter
def insert_time(my_list):
    for i in range(1, len(my_list)):
        j = i - 1
        aux = my_list[i]
        while j >= 0 and my_list[j] > my_list[i]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = aux
    return my_list


def comb_time(my_list):
    gap = len(my_list)
    ok = True
    while ok or gap > 1:
        gap = max(1, int(gap / 1.3))
        ok = False
        for i in range(len(my_list) - gap):
            j = i + gap
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
                ok = True
    return my_list


def generate_list(length):
    generated_list = []
    for i in range(length):
        generated_list.append(random.randint(1, 1000))
    return generated_list


def calc_time_sort(function, my_list):
    start = time.time()
    function(my_list)
    stop = time.time()
    return round((stop - start) * 1000, 5)
