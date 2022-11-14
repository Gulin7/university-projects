from business.cautare_tranzactii import cautare_tranzactii_dupa_data_si_suma, cautare_tranzactii_dupa_tip


def suma_tranzactii_tip(l_tranzactii, tip_cautat):
    '''
    returneaza suma tranzactiilor din lista de tranzactii l_tranzactii de un anumit tip
    string tip_cautat
    :param l_tranzactii: lista de tranzactii
    :param tip_cautat: string
    :return: suma float a tranzactiilor de un anumit tip
    '''
    sumtr = 0
    for tranzactie in l_tranzactii:
        if tranzactie["tip"] == tip_cautat:
            sumtr += tranzactie["suma"]
    return sumtr


def sold_cont_data(l_tr, data_spec):
    '''
    returneaza soldul contului cu tranzactiile salvate intr-o lista de tranzactii l_tr
    la o data specificata data_spec, sub forma unei liste - data_spec[0] = zi,
    data_spec[1] = luna, data_spec[2] = an
    :param l_tr: lista de tranzactii
    :param data_spec: data speficiata sub forma unei liste
    :return: rez: soldul contului la o data specificata
    '''
    sold = 0
    l_tranzactii = cautare_tranzactii_dupa_data_si_suma(l_tr, data_spec, 0.0)
    for tranzactie in l_tranzactii:
        if tranzactie['tip'] == 'intrare':
            sold += tranzactie['suma']
        else:
            sold -= tranzactie['suma']
    return sold


def suma(tranzactie):
    '''
    returneaza suma unei tranzactii
    :param tranzactie: tranzactie
    :return: rez: suma unei tranzactii
    '''
    return tranzactie['suma']


def tranzactii_tip_ordonate_dupa_suma(l_tr, tip_spec):
    '''
    returneaza tranzactiile din lista de tranzactii l_tr, de un anumit tip specificat
    string tip_spec, ordonate crescator dupa suma
    :param l_tr: lista de tranzactii
    :param tip_spec: string
    :return: rez: lista de tranzactii de un anumit tip ordonate crescator dupa suma
    '''
    l_tranzactii = cautare_tranzactii_dupa_tip(l_tr, tip_spec)
    l_tranzactii.sort(key=suma)
    return l_tranzactii