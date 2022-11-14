from infrastructura.repository_tranzactii import *
from validare.validator_tranzactie import valideaza_tranzactie


def adauga_tranzactie_service(l_tr, data_tr, suma_tr, tip_tr):
    '''
    functia va crea o tranzactie pe baza datei sub forma unei liste data_tr, a unei sume
    float suma_tr si a unui tip string tip_tr si va incerca sa o valideze, iar daca
    tranzactia este valida va fi adaugata in lista de tranzactii l_tr
    :param l_tr: lista de tranzactii
    :param data_tr: data sub forma unei liste
    :param suma_tr: float
    :param tip_tr: string
    :return: - (daca tranzactia este valida)
    :raises: ValueError - daca data tranzactiei este invalida - 0>zi sau zi>32, luna<0 sau
                          luna>12, an<0 sau an>2022 - se concateneaza stringul
                          "data invalida!\n"
                        - daca suma tranzactiei este invalida - suma<=0.0 - concateneaza
                          stringul "suma invalida!\n"
                        - daca tipul tranzactiei este invalid - tip != "intrare" sau
                        tip != "iesire" concateneaza stringul "tip invalid!\n"
    '''
    tranzactie = creeaza_tranzactie(data_tr, suma_tr, tip_tr)
    valideaza_tranzactie(tranzactie)
    adauga_tranzactie(l_tr, tranzactie)


def sterge_tranzactie_service(l_tr, data, suma, tip):
    tranzactie_cautata = creeaza_tranzactie(data, suma, tip)
    valideaza_tranzactie(tranzactie_cautata)
    sterge_tranzactie(l_tr, tranzactie_cautata)


def numar_tranzactii_service(l_tr):
    '''
    returneaza numarul de tranzactii din lista l
    :param l_tr: lista de tranzactii
    :return: rez: |l_tr|
    '''
    return numar_tranzactii(l_tr)


def get_all_service_tranzactii(l_tr):
    return get_all_lista_tranzactii(l_tr)


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
        if get_tip_tranzactie(tranzactie) == tip_cautat:
            sumtr += get_suma_tranzactie(tranzactie)
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
        if get_tip_tranzactie(tranzactie) == 'intrare':
            sold += get_suma_tranzactie(tranzactie)
        else:
            sold -= get_suma_tranzactie(tranzactie)
    return sold


def tranzactii_tip_ordonate_dupa_suma(l_tr, tip_spec):
    '''
    returneaza tranzactiile din lista de tranzactii l_tr, de un anumit tip specificat
    string tip_spec, ordonate crescator dupa suma
    :param l_tr: lista de tranzactii
    :param tip_spec: string
    :return: rez: lista de tranzactii de un anumit tip ordonate crescator dupa suma
    '''
    l_tranzactii = cautare_tranzactii_dupa_tip(l_tr, tip_spec)
    l_tranzactii.sort(key=get_suma_tranzactie)
    return l_tranzactii


def filtreaza_tranzactie_tip(l_tr, tip):
    '''
    sterge din l_tr tranzactiile de un anumit tip string tip
    :param l_tr: lista de tranzactii
    :param tip: string
    :return:  - (modifica l_tr, elimina tranzactiile corespunzatoare)
    '''
    l_tr[:] = [
        tranzactie for tranzactie in l_tr if get_tip_tranzactie(tranzactie) != tip
    ]


def filtreaza_tranzactii_tip_si_suma(l_tr, tip, suma):
    '''
    elimina tranzactiile din l_tr de un anumit tip dat string tip si mai mici decat o
    suma data float suma
    :param l_tr: lista de tranzactii
    :param tip: string
    :param suma: float
    :return: - (modifica l_tr, elimina tranzactiile corespunzatoare)
    '''
    filtreaza_tranzactie_tip(l_tr, tip)
    l_tr[:] = [
        tranzactie for tranzactie in l_tr if get_suma_tranzactie(tranzactie) < suma
    ]
