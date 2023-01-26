from functions import *


def run_add_tests():
    name = 'Untold'
    month = 12
    cost = 432
    artists = ['Bon Jovi', 'Avicii']
    fest1 = create_festival(name, month, cost, artists)
    festival_list = []
    festival_list = add_festival_to_list(fest1, festival_list)
    assert len(festival_list) == 1
    festival_list = add_festival_to_list(fest1, festival_list)
    assert len(festival_list) == 1
    name = 'Neversea'
    fest1 = create_festival(name, month, cost, artists)
    festival_list = add_festival_to_list(fest1, festival_list)
    assert len(festival_list) == 2
    name = 'NYFest'
    month = 13
    cost = 'no'
    fest1 = create_festival(name, month, cost, artists)
    assert fest1 == False


def run_3_tests():
    name = 'Untold'
    month = 12
    cost = 432
    artists = ['Bon Jovi', 'Avicii']
    fest1 = create_festival(name, month, cost, artists)
    festival_list = []
    festival_list = add_festival_to_list(fest1, festival_list)
    list1 = get_festivals_by_artist(festival_list, 'Kanye')
    assert len(list1) == 0
    list2 = get_festivals_by_artist(festival_list, 'Avicii')
    assert len(list2) == 1


def run_all_tests():
    print('Starting command 1 tests... ')
    run_add_tests()
    print('Finished command 1 tests...')
    print('Starting command 3 tests...')
    run_3_tests()
    print('Finished command 3 tests...')
