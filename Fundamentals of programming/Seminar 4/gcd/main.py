def great_com_div(a, b):
    if a * b == 0:
        return max(a, b)
    return great_com_div(b, a % b)


def great_com_div_list(arr):
    if len(arr) == 0:
        return 1
    if len(arr) == 1:
        return arr[0]
    return great_com_div(great_com_div_list(arr[:len(arr) // 2]), great_com_div_list(arr[len(arr) // 2:]))


if __name__ == '__main__':
    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))
    print(great_com_div(a, b))
    my_list = [4, 8, 6, 120, 504, 7]
    print(great_com_div_list(my_list))
