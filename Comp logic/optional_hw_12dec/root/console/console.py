from root.services.rapid_conversions import *
from root.services.functions import *
from root.services.conversions import *


def get_command():
    list_of_commands = ['exit', 'add', 'convert', 'sub', 'multiply', 'divide']
    while True:
        command = input('Enter a command: ').lower()
        if command in list_of_commands:
            break
        print('Invalid command! 👎')
    return command


def get_base():
    """
    Gets a base from the user as input.
    :return: the base
    """
    while True:
        try:
            base = int(input('Enter a base: '))
            if base == 16 or (base > 1 and base < 11):
                break
            else:
                print('Invalid base! 😪')
        except ValueError as ve:
            print('Invalid base! 😪', ve)
        except:
            print('Invalid base! 😪')
    return base


def get_number_in_base(base):
    """
    Gets the number and checks if its in base "base"
    :param base: the base the number is supposed to be in, integer
    :return: the number
    """
    while True:
        number = input('Enter a number: ')
        if base == 16:
            if check_number_base16(number):
                break
        else:
            if check_number_and_base(number, base):
                break
        print(f'Invalid number for base {base}! 😪')
    return number


def show_in_base10(number, base):
    """
    Prints the number in base 10.

    :param number: given number, int or str
    :param base: int, given base
    :return:
    """
    print(convert_to_base10(number, base))


def add_2_numbers():
    """
    GETS 2 NUMBERS AS WELL AS THEIR BASE AND COMPUTES THE SUBSTRACTION OF THE 2 NUMBERS.
    :return: 
    """
    base = get_base()
    number1 = get_number_in_base(base)
    number2 = get_number_in_base(base)
    number1_in_base10 = convert_to_base10(number1, base)
    number2_in_base10 = convert_to_base10(number2, base)
    result_in_base10 = number1_in_base10 + number2_in_base10
    print(f"""Your result is:
-> in base 10: {result_in_base10}
-> in base {base}: {convert_from_base10_to_base(result_in_base10, base)}""")


def sub_2_numbers():
    """
    GETS 2 NUMBERS AS WELL AS THEIR BASE AND COMPUTES THE SUBSTRACTION OF THE 2 NUMBERS.
    :return:
    """
    base = get_base()
    number1 = get_number_in_base(base)
    number2 = get_number_in_base(base)
    number1_in_base10 = convert_to_base10(number1, base)
    number2_in_base10 = convert_to_base10(number2, base)
    result_in_base10 = number1_in_base10 - number2_in_base10
    print(f"""Your result is:
-> in base 10: {result_in_base10}
-> in base {base}: {convert_from_base10_to_base(result_in_base10, base)}""")


def convert_number():
    print('Enter the number you want to convert and the base you want to convert it to...')
    print('First, the number and its base: ')
    number_base = get_base()
    number = get_number_in_base(number_base)
    print('The base you want to convert into: ')
    convert_to_this_base = get_base()
    rapid_conversion_basis = [2, 4, 8, 16]
    if number_base == convert_to_this_base:
        print('The number is already in that base! 😂')
    elif number_base in rapid_conversion_basis and convert_to_this_base in rapid_conversion_basis:
        result = 'a'
        if convert_to_this_base != 2:
            result_in_base2 = rapid_convert_to_base2_from_given_base(number, number_base)
            result = rapid_convert_from_base2_to_given_base(result_in_base2, convert_to_this_base)
            print(result)
        if convert_to_this_base == 2:
            result = str(rapid_convert_to_base2_from_given_base(number, number_base))
            print(result)
    else:
        result_in_base10 = convert_to_base10(number, number_base)
        result = convert_from_base10_to_base(result_in_base10, convert_to_this_base)
        print(result)


def show_menu():
    """
    PRINTS THE MENU!
    """
    print("""               MENU-COMMANDS
              ----------------
>>>Type one of the following commands and see the magic happening!
1. ADD
2. SUB
3. MULTIPLY
4. DIVIDE
5. CONVERT
6. EXIT
>>> add,sub,multiply,divide -> input 1 base and 2 numbers in that base
>>> convert -> input a base and a number in that base, as well as the base you want to convert into
>>> exit -> to close the program
>>> you can type with or without capslock on, ex.: "MulTiPly" will work just fine
------------------------------------------------------------------------------------------------------""")


def run_console():
    while True:
        show_menu()
        command = get_command()
        if command == 'exit':
            print('You\'ve left the app! Goodbye! 👋😢😭')
            break
        elif command == 'add':
            add_2_numbers()
        elif command == 'sub':
            sub_2_numbers()
        elif command == 'multiply':
            pass
        elif command == 'divide':
            pass
        elif command == 'convert':
            convert_number()
