from functions import *


def naive_sum(start, elements, lst, given):
    for index in range(start, len(lst)):
        elements.append(lst[index])
        check_value = check_if_equal(elements, given)
        if check_value == 1:
            return elements
        elif check_value == 2:
            naive_sum(index + 1, elements, lst, given)
        elements.pop()
    return []


if __name__ == '__main__':
    print("""1-FOR BACKTRACKING
2-FOR DYNAMIC""")
    while True:
        try:
            problem_number = int(input('Pick one: '))
            if problem_number == 1 or problem_number == 2:
                break
            else:
                print('Invalid Command')
        except ValueError:
            print('Invalid Command')

    if problem_number == 1:
        print("""           PICK ONE
Choose 1 for recursive backtracking!
Choose 2 for iterative backtracking!""")
        # Valid option check
        while True:
            try:
                n = int(input('Enter 1 or 2: '))
                if n == 1 or n == 2:
                    break
                else:
                    print('You did not enter a valid value!')
            except ValueError:
                print('You did not enter a valid value!')

        print("""Do you want to generate a random list? 
1-Yes
2-No, input manually""")
        while True:
            try:
                option = int(input('Chose an option: '))
                if option == 1 or option == 2:
                    break
            except ValueError:
                print('Invalid command!')
        while True:
            try:
                length = int(input('Enter a list length: '))
                break
            except ValueError:
                print('You did not enter a valid value!')
        if option == 1:
            # Auto generates a list of given length and prints it
            a = generate_list(length)
        else:
            a = []
            for i in range(length):
                a.append(int(input('Enter an integer:')))
        print(a)
        print("-------------")
        if n == 1:
            bt_rec(0, [], a)
        else:
            bt_it(a)
    else:
        print("""1-FOR NAIVE IMPLEMENTATION
2-FOR DYNAMIC IMPLEMENTATION""")
        while True:
            try:
                nr = int(input('Pick one: '))
                if nr == 1 or nr == 2:
                    break
                else:
                    print('Invalid Command')
            except ValueError:
                print('Invalid Command')
        while True:
            try:
                length = int(input('Enter a list length: '))
                break
            except ValueError:
                print('You did not enter a valid value!')
        s = []
        for i in range(length):
            s.append(int(input('Enter an integer:')))
        while True:
            try:
                k = int(input('Enter element k: '))
                break
            except ValueError:
                print('You did not enter a valid value!')
        print(f'The list is {s}')
        print("------------------")
        """
        s= the list
        k= the given element
        nr is 1 for naive, and 2 for dynamic
        """
        if nr == 1:
            solution = naive_sum(0, [], s, k)
            if len(solution) == 0:
                print('No solution!')
            else:
                print(solution)
        else:
            dynamic_sum(s, k)
