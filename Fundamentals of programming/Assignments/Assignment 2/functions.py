def insert_sort(my_list, step):
    """
    Insertion sort


    :param my_list: list, unsorted, to be sorted
    :param step: the frequency we are printing
    :return:
    """
    lenght = len(my_list)
    current_step = 0
    for i in range(1, lenght):
        aux = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > aux:
            """
            aux  is used to store the value we have to insert
            we itterate through the list and for every element bigger than aux
            we move the element on the current position to the left
            once aux is bigger than our current element we insert it on the above position
            """
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
