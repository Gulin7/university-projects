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
    command = 1
    while command != 0:
        ok = 0
        while ok == 0:
            try:
                command = int(input("Choose a command: "))
                ok = 1
            except:
                print("You didn't enter a valid command! Try again!")
                ok = 0
            if command < 0 or command > 3:
                print("You didn't enter a valid command! Try again!")
                ok = 0
        if command == 1:
            ok = 0
            my_list = []
            while ok == 0:
                try:
                    n = int(input("Choose a number: "))
                    ok = 1
                except:
                    print("You didn't enter a number! Try again!")
                    ok = 0
            while n > 0:
                my_list.append(random.randint(1, 100))
                n -= 1
            print(f"The list is {my_list} !")
        elif command == 2:
            if len(my_list) == 0:
                print("There is no list to be sorted yet!")
            else:
                ok = 0
                while ok == 0:
                    try:
                        step2 = int(input("Enter an integer: "))
                        ok = 1
                    except:
                        print("You didn't enter an integer! Try again!")
                        ok = 0
                insert_sort(my_list, step2)
                print(f"The sorted list is {my_list} !")
        elif command == 3:
            if len(my_list) == 0:
                print("There is no list to be sorted yet! Enter 1!")
            else:
                ok = 0
                while ok == 0:
                    try:
                        step3 = int(input("Enter an integer: "))
                        ok = 1
                    except:
                        print("You didn't enter an integer! Try again!")
                        ok = 0
                comb_sort(my_list,step3)
                print(f"The sorted list is {my_list} !")
        if command == 0:
            print("You've exit the app! :(")
