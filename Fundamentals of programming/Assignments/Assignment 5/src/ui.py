from functions import *


def input_number():
    """
    This function gets a complex number from the user.

    :return: return a dictionary/list containing the real and the imaginary part of a number.
    """
    print("Input the imaginary number as following: ")
    # following gets the real part from the user
    while True:
        try:
            real_part = float(input("Please enter the real part of the number:"))
            if real_part == int(real_part):
                real_part = int(real_part)
            break
        except ValueError:
            print("You didn't input a number! Please try again!")  #
    # following gets the imaginary part from the user
    while True:
        try:
            imaginary_part = float(input("Please enter the imaginary part of the number:"))
            if imaginary_part == int(imaginary_part):
                imaginary_part = int(imaginary_part)
            break
        except ValueError:
            print("You didn't input a number! Please try again!")
    return create_number(real_part, imaginary_part)


def display_set(complex_set):
    """
    Prints the list of complex numbers written as a+bi.

    :param: complex_set: list of dict/lists
    :return:
    """
    string_set = list()
    for i in complex_set:
        string_set.append(to_string(i))
    print(f"The current set is: \n{string_set} of length {len(string_set)}!")


def display_subarray_w_length(complex_set):
    """
    Prints the subarray of complex numbers written as a+bi as well as its length.

    :param: complex_set: list of dict/lists
    :return:
    """
    string_set = list()
    for i in range(len(complex_set)):
        string_set.append(to_string(complex_set[i]))
    print(f"The longest subarray is: \n{string_set} of length {len(string_set)}!")


def show_menu():
    print(
        """ MENU:
1. Read a list of complex numbers
2. Display the list
3. Display the given properties
4. Exit the app
---------------------
5. To generate a list of random complex numbers
---------------------
""")


def run_application():
    """
    This functions runs the app.

    It asks the user a command until it the app is left(command 4) and displays to the console whatever is required.
    Command 1: the user can input a set of complex numbers.
    Command 2: the current list/dict of complex numbers is displayed.
    Command 3: 2 computations are done ( with outside functions ) and the results are displayed. There are 2
    sub-options for this command, A/a and B/b .
    Command 4: leaves the app.
    Command 5: creates a list/dict with random complex numbers.
    :return:
    """
    show_menu()
    complex_set = generate_random_complex_number_set(10)
    while True:
        # following gets the command
        while True:
            try:
                command = int(input("Enter a command: "))
                if 0 < command < 6:
                    break
                else:
                    print("Invalid command! ")
            except ValueError:
                print("Invalid command! ")
        if command == 4:
            print("You've left the app! :(")
            break
        if command == 1 or command == 5:
            # gets length
            while True:
                try:
                    length = int(input("Enter the list length(integer): "))
                    break
                except ValueError:
                    print("Invalid length! ")
            complex_set.clear()
            if command == 1:
                for index in range(length):
                    complex_set.append(input_number())
            else:
                complex_set = generate_random_complex_number_set(length)
        if command == 2:
            display_set(complex_set)
        if command == 3:
            # following gets the option, A or B
            while True:
                try:
                    option = input(
                        """Choose option A for set A or option B for set B: """)
                    option = option.upper()
                    if option == 'A' or option == 'B':
                        break
                    else:
                        print("Invalid command! ")
                except ValueError:
                    print("Invalid command! ")
            if option == 'A':
                result = []
                result = longest_increasing_modulus_subsequence(0, [], [], complex_set, result)
                print(f"The subsequence is: "
                      f"{result} of length {len(result)}!")
            else:
                result = longest_subarray_modulus(complex_set)
                display_subarray_w_length(result)
                # print(result)
