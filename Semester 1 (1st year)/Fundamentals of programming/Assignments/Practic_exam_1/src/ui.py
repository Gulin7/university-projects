from functions import *
import copy


def get_command():
    command = input('Enter a command: ')
    command = command.lower()
    return command


def show_menu():
    print("""       MENU        
1. add -> to add a new music festival
2. show-season -> to show festivals based on the current season
3. show-artist -> to show festivals based on an artist
4. exit -> to exit the app""")


def add_festival(festival_list):
    # name
    name = input('Enter the festival name: ')

    # month
    month = 1
    while True:
        try:
            month = int(input('Enter the festival month: '))
            if month < 1 or month > 12:
                print('That is not a month! 👎')
            else:
                break
        except ValueError:
            print('Invalid input! 👎')
        except:
            print('Invalid input! 👎')

    # ticket cost
    cost = 0
    while True:
        try:
            cost = int(input('Enter the ticket cost: '))
            break
        except ValueError:
            print('Invalid input! 👎')
        except:
            print('Invalid input! 👎')

    # list of artists
    while True:
        try:
            length = int(input('Enter the number of artists: '))
            if length < 1:
                print('Not a valid length')
            else:
                break
        except ValueError:
            print('Invalid input! 👎')
        except:
            print('Invalid input! 👎')
    list_of_artists = []
    for i in range(length):
        artist = input('Enter an artist: ')
        list_of_artists.append(artist)

    festival = create_festival(name, month, cost, list_of_artists)
    copied = copy.deepcopy(add_festival_to_list(festival, festival_list))
    if copied == festival_list:
        print('The festival name already existed! ')
    else:
        return copied


def show_season(festival_list):
    """
    Shows all the festivals in a given season.
    :param festival_list: list of festivals
    :return:
    """
    seasons = ['winter', 'summer', 'spring', 'autumn']
    while True:
        season = input('Enter a season: ').lower()
        if season not in seasons:
            print('Invalid season.')
        else:
            break
    new_list = []
    for festival in festival_list:
        if season == 'winter':
            if festival['month'] == 12 or festival['month'] < 3:
                new_list.append(festival)
        elif season == 'spring':
            if festival['month'] > 2 and festival['month'] < 6:
                new_list.append(festival)
        elif season == 'summer':
            if festival['month'] > 5 and festival['month'] < 9:
                new_list.append(festival)
        elif season == 'autumn':
            if festival['month'] < 12 and festival['month'] > 8:
                new_list.append(festival)

    new_list.sort(key=get_month)
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    if len(new_list) == 0:
        print('No festivals in that season.')
    else:
        for i in new_list:
            print(
                f"""The festival name is: {get_name(i)},
                            month: {months[get_month(i)]}, 
                            cost: {get_cost(i)}, 
                            artists: {get_artists(i)}!""")


def show_artist(festival_list):
    """
    Prints all the festivals with a given artist.

    :param festival_list: the list of festivals
    :return:
    """
    artist = input('Enter an artist: ')
    new_list = get_festivals_by_artist(festival_list, artist)
    if len(new_list) == 0:
        print('No festivals with the given artist')
    else:
        new_list.sort(key=get_month)
        for i in new_list:
            print(
                f"""The festival name is: {get_name(i)},
                month: {get_month(i)}, 
                cost: {get_cost(i)}, 
                artists: {get_artists(i)}!""")


def run_console():
    festival_list = generate_random_festival(10)

    while True:
        show_menu()
        command = get_command()
        if command == 'exit':
            print('You\'ve left the app! Goodbye!😢')
            break
        elif command == 'add':
            festival_list = add_festival(festival_list)
        elif command == 'show-artist':
            show_artist(festival_list)
        elif command == 'show-season':
            show_season(festival_list)
        else:
            print('Invalid command!')
