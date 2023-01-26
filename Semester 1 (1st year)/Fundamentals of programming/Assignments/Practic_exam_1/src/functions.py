import random
import copy


def create_festival(fname, fmonth, fcost, fartists):
    """
    Creates a festival.

    :param fname: name
    :param fmonth: month, int, 1-12
    :param fcost: int, cost
    :param fartists: list of artists
    :return:
    """
    if fmonth > 12 or fmonth < 1:
        return False
    try:
        fcost = int(fcost)
        fmonth = int(fmonth)
    except:
        return False
    festival = {'name': fname, 'month': fmonth, 'cost': fcost, 'artists': fartists}
    return festival


def add_festival_to_list(given_festival, festival_list):
    """
    Adds a festival to a list of festivals.

    :param given_festival: festival, dict
    :param festival_list: the list of festivals we add to
    :return:
    """
    list_of_festivals = copy.deepcopy(festival_list)
    ok = 1
    for festival in list_of_festivals:
        if festival['name'].lower() == given_festival['name'].lower():
            ok = 0
    if ok == 1:
        list_of_festivals.append(given_festival)
    return list_of_festivals


def get_name(festival):
    return festival['name']


def get_month(festival):
    return festival['month']


def get_cost(festival):
    return festival['cost']


def get_artists(festival):
    return festival['artists']


def get_festivals_by_artist(festival_list, artist):
    """
    Creates and returns a list with a given artist.

    :param festival_list: list of festivals
    :param artist: the given artist
    :return: a list of festivals that have a given artist
    """
    new_list = []
    for i in festival_list:
        artists = get_artists(i)
        if artist in artists:
            new_list.append(i)
    return new_list


def generate_random_festival(length):
    """
    Creates a list of random festivals.
    :param length: the length of the list of festivals
    :return:
    """
    festivals = []

    name = ['Untold', 'NeverSea', 'ElectricCastle', 'CFR', 'BerlinFestival', 'ParisFestival', 'LondonFestival',
            'DublinFestival', 'EuroFestival', 'NYFestival', 'ChicagoFestival', 'TokyoFestival', 'MadridFestival']

    artists = [['Avicii', 'Kanye', 'IronMaiden', 'Madonna', 'Beyonce', 'J.Cole', 'Eminem'],
               ['Kanye', 'IronMaiden', 'Madonna', 'Beyonce', 'J.Cole', 'Eminem'],
               ['Avicii', 'Kanye', 'IronMaiden', 'Madonna', 'Beyonce', 'J.Cole', 'Eminem'],
               ['Avicii', 'IronMaiden', 'Madonna', 'Beyonce', 'J.Cole', 'Eminem'],
               ['Avicii', 'Kanye', 'Madonna', 'Beyonce', 'J.Cole', 'Eminem'],
               ['Avicii', 'Kanye', 'IronMaiden', 'Madonna', 'Beyonce'],
               ['Avicii', 'Kanye', 'Beyonce', 'J.Cole', 'Eminem'],
               ['Kanye', 'IronMaiden', 'Madonna', 'Eminem'],
               ['Avicii', 'Kanye', 'Eminem'],
               ['Avicii', 'Kanye', 'J.Cole', 'Eminem'],
               ['Kanye''J.Cole', 'Eminem'],
               ['Avicii', 'Kanye', ],
               ['J.Cole', 'Eminem'],
               ['Madonna', 'Beyonce'],
               ]

    while len(festivals) < length:
        new_fest = create_festival(random.choice(name), random.randint(1, 12), random.randint(100, 1000),
                                   random.choice(artists))
        ok = 1
        for festival in festivals:
            if festival['name'].lower() == new_fest['name']:
                ok = 0
        if ok == 1:
            festivals.append(new_fest)

    return festivals
