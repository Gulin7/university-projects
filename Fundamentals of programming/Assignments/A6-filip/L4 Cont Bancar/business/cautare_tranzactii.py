from datetime import date


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
        if tranzactie["suma"] > suma_cautata:
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
        l_data = tranzactie["data"]
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
        if tranzactie["tip"] == "intrare":
            tranzactii_intrare.append(tranzactie)
        else:
            tranzactii_iesire.append(tranzactie)
    if tip_cautat == "intrare":
        return tranzactii_intrare
    else:
        return tranzactii_iesire