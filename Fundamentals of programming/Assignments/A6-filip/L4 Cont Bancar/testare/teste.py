from business.cautare_tranzactii import cautare_tranzactii_dupa_suma, cautare_tranzactii_dupa_data_si_suma, \
    cautare_tranzactii_dupa_tip
from business.filtrare_tranzactii import filtrare_tip_tranzactii, filtrare_tip_si_suma_tranzactii
from business.rapoarte_tranzactii import suma_tranzactii_tip, sold_cont_data, tranzactii_tip_ordonate_dupa_suma
from business.service_tranzactie import numar_tranzactii_service, adauga_tranzactie_service, sterge_tranzactie_data, \
    sterge_tranzactie_tip, filtreaza_tranzactii_tip_si_suma, sterge_tranzactii_perioada
from domain.tranzactie import creeaza_tranzactie, get_data_tranzactie, get_suma_tranzactie, get_tip_tranzactie, \
    set_data_tranzactie, set_suma_tranzactie, set_tip_tranzactie
from infrastructura.repository_tranzactii import adauga_tranzactie, numar_tranzactii
from validare.validator_tranzactie import valideaza_tranzactie, valideaza_suma, valideaza_tip


def ruleaza_teste_tranzactie():
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    assert (data_tranzactie == get_data_tranzactie(tranzactie))
    assert (suma == get_suma_tranzactie(tranzactie))
    assert (tip == get_tip_tranzactie(tranzactie))
    data_noua = [15, 10, 2022]
    suma_noua = 1500.00
    tip_nou = "iesire"
    set_data_tranzactie(tranzactie, data_noua)
    set_suma_tranzactie(tranzactie, suma_noua)
    set_tip_tranzactie(tranzactie, tip_nou)
    assert data_noua == get_data_tranzactie(tranzactie)
    assert abs(suma_noua - get_suma_tranzactie(tranzactie)) < 0.0001
    assert tip_nou == get_tip_tranzactie(tranzactie)


def ruleaza_teste_valideaza_suma():
    suma_gresita = 0.00
    try:
        valideaza_suma(suma_gresita)
        assert False
    except ValueError as ve:
        assert str(ve) == "suma invalida!\n"


def ruleaza_teste_valideaza_tip():
    tip_gresit = 'nebunie'
    try:
        valideaza_tip(tip_gresit)
        assert False
    except ValueError as ve:
        assert str(ve) == "tip invalid!\n"


def ruleaza_teste_validator_tranzactie():
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    valideaza_tranzactie(tranzactie)

    data_tranzactie_gresita = [32, 13, 2023]
    suma_gresita = -12
    tip_gresit = ""
    tranzactie_gresita = creeaza_tranzactie(data_tranzactie_gresita, suma_gresita, tip_gresit)
    try:
        valideaza_tranzactie(tranzactie_gresita)
        assert False
    except ValueError as ve:
        assert str(ve) == "data invalida!\nsuma invalida!\ntip invalid!\n"

    ruleaza_teste_valideaza_tip()
    ruleaza_teste_valideaza_suma()


def ruleaza_teste_cautare_tranzactii():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_tranzactie = [16, 10, 2022]
    suma = 1300.20
    tip = "iesire"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_tranzactie = [16, 10, 2022]
    suma = 500.55
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    suma_cautata = 800.00
    assert cautare_tranzactii_dupa_suma(lista_tranzactii, suma_cautata) == [{
        'data': [13, 10, 2022],
        'suma': 1200.9,
        'tip': 'intrare'},
        {
            'data': [16, 10, 2022],
            'suma': 1300.2,
            'tip': 'iesire'
        }]

    data_cautata = [15, 10, 2022]
    suma_cautata = 1200.0
    assert cautare_tranzactii_dupa_data_si_suma(lista_tranzactii, data_cautata, suma_cautata) == [{
        'data': [13, 10, 2022],
        'suma': 1200.9,
        'tip': 'intrare'}]

    tip_cautat = "intrare"
    assert cautare_tranzactii_dupa_tip(lista_tranzactii, tip_cautat) == [{
        'data': [13, 10, 2022],
        'suma': 1200.9,
        'tip': 'intrare'},
        {
            'data': [16, 10, 2022],
            'suma': 500.55,
            'tip': 'intrare'
        }]


def ruleaza_teste_stergere_tranzactii_perioada():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [14, 10, 2022]
    suma = 1300.2
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [16, 10, 2022]
    suma = 500.55
    tip = "iesire"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [17, 10, 2022]
    suma = 399.99
    tip = "iesire"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)
    data1 = [13, 10, 2022]
    data2 = [16, 10, 2022]
    sterge_tranzactii_perioada(lista_tranzactii, data1, data2)
    assert numar_tranzactii_service(lista_tranzactii) == 1


def ruleaza_teste_stergere_tranzactii_data_si_tip():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)
    data_tranzactie = [13, 10, 2022]
    suma = 1300.0
    tip = "iesire"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)
    data_tranzactie = [16, 10, 2022]
    suma = 300
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)
    data_tranzactie = [20, 10, 2022]
    suma = 100.0
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data = [13, 10, 2022]
    sterge_tranzactie_data(lista_tranzactii, data)
    assert numar_tranzactii_service(lista_tranzactii) == 2

    tip_spec = "intrare"
    sterge_tranzactie_tip(lista_tranzactii, tip_spec)
    assert numar_tranzactii_service(lista_tranzactii) == 0
    ruleaza_teste_stergere_tranzactii_perioada()


def ruleaza_teste_repository_tranzactii():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    assert numar_tranzactii(lista_tranzactii) == 0
    adauga_tranzactie(lista_tranzactii, tranzactie)
    assert numar_tranzactii(lista_tranzactii) == 1
    ruleaza_teste_cautare_tranzactii()
    ruleaza_teste_stergere_tranzactii_perioada()
    ruleaza_teste_stergere_tranzactii_data_si_tip()



def ruleaza_teste_suma_tranzactii_tip():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_tranzactie = [15, 10, 2022]
    suma = 1300.20
    tip = "iesire"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_tranzactie = [16, 10, 2022]
    suma = 500.55
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_tranzactie = [25, 9, 2022]
    suma = 399.99
    tip = "iesire"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    tip_cautat = "intrare"
    assert suma_tranzactii_tip(lista_tranzactii, tip_cautat) == 1701.45

    tip_cautat = "iesire"
    assert suma_tranzactii_tip(lista_tranzactii, tip_cautat) == 1700.19


def ruleaza_teste_sold_cont_data():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_tranzactie = [15, 10, 2022]
    suma = 1300.2
    tip = "iesire"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_tranzactie = [16, 10, 2022]
    suma = 500.55
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_tranzactie = [17, 10, 2022]
    suma = 399.99
    tip = "iesire"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_spec = [17, 10, 2022]
    assert abs(sold_cont_data(lista_tranzactii, data_spec) - 1.26) < 0.0001


def ruleaza_teste_tranzactii_tip_ordonate_dupa_suma():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_tranzactie = [15, 10, 2022]
    suma = 1300.2
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_tranzactie = [16, 10, 2022]
    suma = 500.55
    tip = "intrare"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    data_tranzactie = [17, 10, 2022]
    suma = 399.99
    tip = "iesire"
    tranzactie = creeaza_tranzactie(data_tranzactie, suma, tip)
    adauga_tranzactie(lista_tranzactii, tranzactie)

    tip_spec = "intrare"
    assert tranzactii_tip_ordonate_dupa_suma(lista_tranzactii, tip_spec) == [{
        'data': [16, 10, 2022],
        'suma': 500.55,
        'tip': "intrare"
    }, {
        'data': [13, 10, 2022],
        'suma': 1200.9,
        'tip': "intrare"
    }, {
        'data': [15, 10, 2022],
        'suma': 1300.2,
        'tip': "intrare"
    }]


def ruleaza_teste_rapoarte_tranzactii():
    ruleaza_teste_suma_tranzactii_tip()
    ruleaza_teste_sold_cont_data()
    ruleaza_teste_tranzactii_tip_ordonate_dupa_suma()


def ruleaza_teste_filtrare_tip_tranzactii():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [15, 10, 2022]
    suma = 1300.2
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [16, 10, 2022]
    suma = 500.55
    tip = "iesire"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [17, 10, 2022]
    suma = 399.99
    tip = "iesire"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    tip_spec = "intrare"
    sterge_tranzactie_tip(lista_tranzactii, tip_spec)
    assert numar_tranzactii_service(lista_tranzactii) == 2


def ruleaza_teste_filtrare_tip_si_suma_tranzactii():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [15, 10, 2022]
    suma = 1300.2
    tip = "iesire"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [16, 10, 2022]
    suma = 500.55
    tip = "iesire"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [17, 10, 2022]
    suma = 399.99
    tip = "iesire"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    tip_spec = "intrare"
    suma_spec = 1300.2
    filtreaza_tranzactii_tip_si_suma(lista_tranzactii, tip_spec, suma_spec)
    print(">>>", lista_tranzactii)
    assert numar_tranzactii_service(lista_tranzactii) == 2


def ruleaza_teste_filtrare_tranzactii():
    ruleaza_teste_filtrare_tip_tranzactii()
    ruleaza_teste_filtrare_tip_si_suma_tranzactii()


def ruleaza_teste_stergere_tranzactii_perioada():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [14, 10, 2022]
    suma = 1300.2
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [16, 10, 2022]
    suma = 500.55
    tip = "iesire"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data_tranzactie = [17, 10, 2022]
    suma = 399.99
    tip = "iesire"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)
    data1 = [13, 10, 2022]
    data2 = [16, 10, 2022]
    sterge_tranzactii_perioada(lista_tranzactii, data1, data2)
    assert numar_tranzactii_service(lista_tranzactii) == 1


def ruleaza_teste_stergere_tranzactii_data_si_tip():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)
    data_tranzactie = [13, 10, 2022]
    suma = 1300.0
    tip = "iesire"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)
    data_tranzactie = [16, 10, 2022]
    suma = 300
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)
    data_tranzactie = [20, 10, 2022]
    suma = 100.0
    tip = "intrare"
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)

    data = [13, 10, 2022]
    sterge_tranzactie_data(lista_tranzactii, data)
    assert numar_tranzactii_service(lista_tranzactii) == 2

    tip_spec = "intrare"
    sterge_tranzactie_tip(lista_tranzactii, tip_spec)
    assert numar_tranzactii_service(lista_tranzactii) == 0
    ruleaza_teste_stergere_tranzactii_perioada()


def ruleaza_teste_service_tranzactii():
    lista_tranzactii = []
    data_tranzactie = [13, 10, 2022]
    suma = 1200.90
    tip = "intrare"
    assert numar_tranzactii_service(lista_tranzactii) == 0
    adauga_tranzactie_service(lista_tranzactii, data_tranzactie, suma, tip)
    assert numar_tranzactii_service(lista_tranzactii) == 1

    data_tranzactie_gresita = [15, 13, 2022]
    suma_gresita = 0.00
    tip_gresit = ''
    try:
        adauga_tranzactie_service(lista_tranzactii, data_tranzactie_gresita, suma_gresita, tip_gresit)
        assert False
    except ValueError as ve:
        assert str(ve) == "data invalida!\nsuma invalida!\ntip invalid!\n"
    ruleaza_teste_filtrare_tranzactii()
    ruleaza_teste_rapoarte_tranzactii()


def ruleaza_toate_testele():
    ruleaza_teste_tranzactie()
    print("Teste tranzactie rulate cu succes!")
    ruleaza_teste_validator_tranzactie()
    print("Teste validator_tranzactie rulate cu succes!")
    ruleaza_teste_repository_tranzactii()
    print("Teste repository_tranzactii rulate cu succes!")
    ruleaza_teste_service_tranzactii()
    print("Teste service_tranzactii rulate cu succes!")
