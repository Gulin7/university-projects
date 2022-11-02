def search_for_max(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return max(search_for_max(arr[:len(arr) // 2]), search_for_max(arr[len(arr) // 2:]))


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 49, 345, 34, 24, 54]
    print(search_for_max(my_list))
