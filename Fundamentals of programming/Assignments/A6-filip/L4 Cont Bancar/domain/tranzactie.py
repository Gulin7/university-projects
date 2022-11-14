def creeaza_tranzactie(l_data, suma, tip):
    '''
    creeaza o tranzactie pe baza unei date sub forma unei liste l_data, a unei sume (float)
    si a unui tip (string)
    :param l_data: lista, pe l[0] se afla ziua realizarii tranzactiei, pe l[1] luna realizarii
                tranzactiei, iar pe l[2] anul realizarii tranzactiei
    :param suma: float
    :param tip: string - intrare/iesire
    :return: rez: tranzactie (cu data sub forma listei l_data, cu suma int sum si tipul
                  string tip
    '''
    return {
        "data": l_data,
        "suma": suma,
        "tip": tip
    }


def get_data_tranzactie(tranzactie):
    '''
    returneaza data sub forma unei liste a unei tranzactii
    :param tranzactie: tranzactie
    :return: data tranzactiei
    '''
    return tranzactie["data"]


def get_suma_tranzactie(tranzactie):
    '''
    returneaza suma int a unei tranzactii
    :param tranzactie: tranzactie
    :return: suma tranzactiei
    '''
    return tranzactie["suma"]


def get_tip_tranzactie(tranzactie):
    '''
    returneaza tipul string a unei tranzactii
    :param tranzactie: tranzactie
    :return: tipul tranzactie
    '''
    return tranzactie["tip"]


def set_data_tranzactie(tranzactie, data_noua):
    '''
    seteaza data tranzactiei la data sub forma de lista data_noua: data_noua[0] = zi, data_noua[1] = luna,
    data_noua[2] = an
    :param tranzactie: tranzactie
    :param data_noua: data noua sub forma de lista
    :return: - (tranzactia va avea data schimbata in data_noua)
    '''
    tranzactie["data"] = data_noua


def set_suma_tranzactie(tranzactie, suma_noua):
    '''
    seteaza suma tranzactiei la suma float suma_noua
    :param tranzactie: tranzactie
    :param suma_noua: float
    :return: - (tranzactia va avea suma schimbata in suma float suma_noua)
    '''
    tranzactie["suma"] = suma_noua


def set_tip_tranzactie(tranzactie, tip_nou):
    '''
    seteaza tipul tranzactiei la tipul string tip_nou
    :param tranzactie: tranzactie
    :param tip_nou: string ("intrare" / "iesire")
    :return: - (tranzactia va avea tipul schimbat in tipul string tip_nou)
    '''
    tranzactie["tip"] = tip_nou
