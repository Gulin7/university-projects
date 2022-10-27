import random


def binary_search(arr, lft, rgt, num):
    if lft <= rgt:
        mid = (lft + rgt) // 2
        if arr[mid] == num:
            #print('Item found :D')
            return True
        elif num > arr[mid]:
            binary_search(arr, mid + 1, rgt, num)
        else:
            binary_search(arr, lft, mid - 1, num)
    else:
        return False


def exponential_search(arr, num):
    if arr[0] == num:
        return True
    index = 1
    while arr[index] <= num and index < len(arr):
        index *= 2
    return binary_search(arr, index // 2, min(index, len(arr) - 1), num)


if __name__ == '__main__':
    my_list = []
    for i in range(50):
        my_list.append(random.randint(1, 100))
    my_list.sort()

    print(my_list)

    while True:
        try:
            x = int(input('Enter a number: '))
            break
        except ValueError:
            print('You didn\'t enter a valid value.')
    print(exponential_search(my_list, x))
    if exponential_search(my_list, x):
        print('Item found!')
    else:
        print(' :( ')
