from domain.tranzactie import *


def valideaza_data_tranzactie(tranzactie):
    '''
    verifica daca data tranzactiei este valida - 1<=zi<=31, 1<=luna<=12,
    0<=an<=2022 - si returneaza 0 daca data este invalida, respectiv 1 daca
    data este valida
    :param tranzactie: tranzactie
    :return: 0 - daca data tranzactiei este invalida
             1 - daca data tranzactiei este valida
    '''
    l_data = get_data_tranzactie(tranzactie)
    if l_data[0] < 1 or l_data[0] > 31:
        return False
    if l_data[1] < 1 or l_data[1] > 12:
        return False
    if l_data[2] < 0 or l_data[2] > 2022:
        return False
    return True


def valideaza_tranzactie(tranzactie):
    '''
    verifica daca data tranzactiei este valida, daca suma este valida, adica >0 si daca
    tipul este valid - adica tip="intrare" sau tip="iesire"
    :param tranzactie: tranzactie
    :return: - (daca tranzactia este valida)
    :raises: ValueError - daca data este invalida concateneaza string ul "data invalida!\n"
                        - daca suma este invalida concateneaza string ul "suma invalida!\n"
                        - daca tipul este invalid concateneaza string ul "tip invalid!\n"
    '''
    erori = ''
    if valideaza_data_tranzactie(tranzactie) == 0:
        erori += "data invalida!\n"
    if get_suma_tranzactie(tranzactie) <= 0:
        erori += "suma invalida!\n"
    if get_tip_tranzactie(tranzactie) == "intrare" or get_tip_tranzactie(tranzactie) == "iesire":
        pass
    else:
        erori += "tip invalid!\n"
    if len(erori):
        raise ValueError(erori)


def valideaza_suma(suma):
    '''
    verifica daca suma data float suma este valida: suma>0
    :param suma: float
    :return: - (daca suma este valida)
    :raises: ValueError - daca suma este invalida concateneaza stringul "suma invalida!\n"
    '''
    erori = ''
    if suma <= 0:
        erori += "suma invalida!\n"
    if len(erori):
        raise ValueError(erori)


def valideaza_tip(tip):
    '''
    verficia daca tipul data string tip este valid, adica tip="intrare" sau tip="iesire"
    :param tip: string
    :return: - (daca tipul este valid)
    :raises: ValueError - daca tipul este invalid concateneaza stringul "tip invalid!\n"
    '''
    erori = ''
    if tip == "intrare" or tip == "iesire":
        pass
    else:
        erori += "tip invalid!\n"
    if len(erori):
        raise ValueError(erori)
