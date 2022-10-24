import random

from functions import insert_sort
from functions import comb_sort


def show_menu():
    print(
        """                        MENU
            Press:
            1-To generate a list of n random numbers ( n is your choice :) )
            2-Sort the list using the insertion sort
            3-Sort the list using the comb sort
            0-Exit menu""")


def run_app():
    my_list = []
    while True:
        while True:
            command = 0
            try:
                command = int(input("Choose a command: "))
                break
            except ValueError:
                print("You didn't enter a valid command! Try again!")
            if command < 0 or command > 3:
                print("You didn't enter a valid command! Try again!")
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
        else:
            if len(my_list) == 0:
                print("There is no list to be sorted yet!")
            else:
                while True:
                    try:
                        step = int(input("Enter an integer: "))
                        break
                    except ValueError:
                        print("You didn't enter an integer! Try again!")
                if command == 2:
                    insert_sort(my_list, step)
                    print(f"The sorted list is {my_list} !")
                else:
                    comb_sort(my_list, step)
                    print(f"The sorted list is {my_list} !")
        if command == 0:
            print("You've exit the app! :(")
            break
