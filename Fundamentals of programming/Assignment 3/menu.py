import copy
import random
from functions import insert_time, insert_sort, comb_time, comb_sort, generate_list, calc_time_sort


def show_menu():
    print("""                        MENU
            Press:
            1-To generate a list of random numbers 
            2-Sort the list using the insert sort
            3-Sort the list using the comb sort
            4-Worst case scenario for the two sorts
            5-Best case scenario for the two sorts
            6-Average case for the two sorts
            0-Exit menu
            ----------------------------------------------------------------------------------------""")


def run_app():
    my_list = []
    while True:
        command = 1
        while True:
            try:
                command = int(input("Choose a command: "))
                break
            except ValueError:
                print("You didn't enter a valid command! Try again!")
            if command < 0 or command > 6:
                print("You didn't enter a valid command! Try again!")
        # ---------------------------------------------------------------
        if command == 1:
            my_list = []
            while True:
                try:
                    n = int(input("Choose a number: "))
                    break
                except ValueError:
                    print("You didn't enter a number! Try again!")
            while n > 0:
                my_list.append(random.randint(1, 100))
                n -= 1
            print(f"The list is {my_list} !")
        elif 1 < command < 4:
            if len(my_list) == 0:
                print("There is no list to be sorted yet! Enter 1 to generate a list!")
            else:
                while True:
                    try:
                        step = int(input("Enter an integer: "))
                        break
                    except ValueError:
                        print("You didn't enter an integer! Try again!")
                if command == 2:
                    insert_sort(my_list, step)
                else:
                    comb_sort(my_list, step)
                print(f"The sorted list is {my_list} !")
        # ---------------------------------------------------------------
        elif 3 < command < 7:
            while True:
                try:
                    length = int(input("Enter the starting length!: "))
                    break
                except ValueError:
                    print("You didn't enter a valid length.")
            insert_duration = []
            comb_duration = []
            if command == 4:
                print("         YOU CHOSE THE WORST CASE SCENARIO: ")
                for i in range(5):
                    my_list = generate_list(length)
                    my_list.sort(reverse=True)
                    list_insert = copy.deepcopy(my_list)
                    list_comb = copy.deepcopy(my_list)
                    insert_duration.append(calc_time_sort(insert_time, list_insert))
                    comb_duration.append(calc_time_sort(comb_time, list_comb))
                    length *= 2
            elif command == 5:
                print("         YOU CHOSE THE BEST CASE SCENARIO: ")
                for i in range(5):
                    my_list = generate_list(length)
                    my_list.sort()
                    list_insert = copy.deepcopy(my_list)
                    list_comb = copy.deepcopy(my_list)
                    insert_duration.append(calc_time_sort(insert_time, list_insert))
                    comb_duration.append(calc_time_sort(comb_time, list_comb))
                    length *= 2
            else:
                print("         YOU CHOSE THE AVERAGE CASE: ")
                for i in range(5):
                    my_list = generate_list(length)
                    list_insert = copy.deepcopy(my_list)
                    list_comb = copy.deepcopy(my_list)
                    insert_duration.append(calc_time_sort(insert_time, list_insert))
                    comb_duration.append(calc_time_sort(comb_time, list_comb))
                    length *= 2
            print(f"The results for insert sort are: {insert_duration} .")
            print(f"The results for comb sort are: {comb_duration}")
        if command == 0:
            print("You've exit the app! :(")
            break
