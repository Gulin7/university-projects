from domain.tranzactie import *
from datetime import date


def adauga_tranzactie(l_tranzactii, tranzactie):
    f'''
    adauga la lista de tranzactii l_tranzactii o tranzactie
    :param l_tranzactii: lista de tranzactii
    :param tranzactie: tranzactie
    :return: - (l_tranzactii' = l_tranzactii U [tranzactie])
    '''
    l_tranzactii.append(tranzactie)


def cautare_tranzactii_dupa_suma(l_tranzactii, suma_cautata):
    '''
    cauta in lista de tranzactii l_tranzactii si returneaza tranzactiile mai mari decat
    suma float suma_cautata cautata
    :param l_tranzactii: lista de tranzactii
    :param suma_cautata: float
    :return: rez: lista de tranzactii cu suma mai mare decat suma cautata
    '''
    l_tranzactii_cautate = []
    for tranzactie in l_tranzactii:
        if get_suma_tranzactie(tranzactie) > suma_cautata:
            l_tranzactii_cautate.append(tranzactie)
    return l_tranzactii_cautate


def cautare_tranzactii_dupa_data_si_suma(l_tranzactii, data_cautata, suma_cautata):
    '''
    returneaza tranzactiile realizate inainte de o data cautata sub forma unei liste
    data_cautata - data_cautata[0] = zi, data_cautata[1] = luna, data_cautata[2] = an
    si cu suma mai mare decat suma cautata float suma_cautata
    :param l_tranzactii: lista de tranzactii
    :param data_cautata: data cautata sub forma unei liste
    :param suma_cautata: float
    :return: rez: lista cu tranzactii realizate inainte de data data si cu suma mai mare
    decat suma data
    '''
    l_tranzactii_suma = cautare_tranzactii_dupa_suma(l_tranzactii, suma_cautata)
    l_tranzactii_cautate = []
    for tranzactie in l_tranzactii_suma:
        l_data = get_data_tranzactie(tranzactie)
        date1 = date(l_data[2], l_data[1], l_data[0])
        date2 = date(data_cautata[2], data_cautata[1], data_cautata[0])
        if date1 <= date2:
            l_tranzactii_cautate.append(tranzactie)
    return l_tranzactii_cautate


def cautare_tranzactii_dupa_tip(l_tranzactii, tip_cautat):
    '''
    returneaza tranzactiile de un anumit tip string tip_cautat
    :param l_tranzactii: lista de tranzactii
    :param tip_cautat: tipul cautat
    :return: rez: lista cu tranzactii de un anumit tip
    '''
    tranzactii_iesire = []
    tranzactii_intrare = []
    for tranzactie in l_tranzactii:
        if get_tip_tranzactie(tranzactie) == "intrare":
            tranzactii_intrare.append(tranzactie)
        else:
            tranzactii_iesire.append(tranzactie)
    if tip_cautat == "intrare":
        return tranzactii_intrare
    else:
        return tranzactii_iesire


def sterge_tranzactie(l_tr, tranzactie_cautata):
    l_tr[:] = [
        tranzactie for tranzactie in l_tr if tranzactie != tranzactie_cautata
    ]


def sterge_tranzactie_tip(l_tr, tip):
    '''
    sterge din l_tr tranzactiile de un anumit tip string tip
    :param l_tr: lista de tranzactii
    :param tip: string
    :return:  - (modifica l_tr, elimina tranzactiile corespunzatoare)
    '''
    l_tr[:] = [
        tranzactie for tranzactie in l_tr if get_tip_tranzactie(tranzactie) != tip
    ]


def sterge_tranzactie_data(l_tr, data):
    '''
    sterge din l_tr tranzactiile de la o anumita data data sub forma unei liste
    :param l_tr: lista de tranzactii
    :param data: data sub forma unei liste
    :return:  - (modifica l_tr, elimina tranzactiile corespunzatoare)
    '''
    l_tr[:] = [
        tranzactie for tranzactie in l_tr if get_data_tranzactie(tranzactie) != data
    ]


def sterge_tranzactii_perioada(l_tr, data1, data2):
    '''
    sterge din l_tr tranzactiile dintr-o anumita perioada
    :param l_tr: lista de tranzactii
    :param data1: inceputul perioadei (data sub forma unei liste)
    :param data2: sfarsitul perioadei (data sub forma unei liste)
    :return:  - (modifica l_tr, elimina tranzactiile corespunzatoare)
    '''
    data_a = date(data1[2], data1[1], data1[0])
    data_b = date(data2[2], data2[1], data2[0])
    l_tr[:] = [
        tranzactie for tranzactie in l_tr if data_a > date(get_data_tranzactie(tranzactie)[2], get_data_tranzactie(tranzactie)[1], get_data_tranzactie(tranzactie)[0]) or date(get_data_tranzactie(tranzactie)[2], get_data_tranzactie(tranzactie)[1], get_data_tranzactie(tranzactie)[0]) > data_b
    ]


def modifica_tranzactie(tranzactie, tranzactie_noua):
    set_data_tranzactie(tranzactie, get_data_tranzactie(tranzactie_noua))
    set_suma_tranzactie(tranzactie, get_suma_tranzactie(tranzactie_noua))
    set_tip_tranzactie(tranzactie, get_tip_tranzactie(tranzactie_noua))


def numar_tranzactii(l_tranzactii):
    '''
    returneaza numarul de tranzactii din lista l_tranzactii
    :param l_tranzactii: lista de tranzactii
    :return: rez: int - |l_tranzactii|
    '''
    return len(l_tranzactii)


def get_all_lista_tranzactii(l_tr):
    return l_tr[:]
