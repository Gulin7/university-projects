from business.service_tranzactie import *
from domain.tranzactie import creeaza_tranzactie
from infrastructura.repository_tranzactii import adauga_tranzactie, numar_tranzactii


def adauga_tranzactii_ui(l_tr, params):
    if len(params) != 5:
        print("Numar parametri invalid!\n")
        return
    data_tranzactie = []
    for i in range(0, 3):
        data_tranzactie.append(int(params[i]))
    suma_tranzactie = float(params[3])
    tip_tranzactie = params[4]
    adauga_tranzactie_service(l_tr, data_tranzactie, suma_tranzactie, tip_tranzactie)


def sterge_tranzactie_ui(l_tr, params):
    if len(params) != 5:
        print("Numar parametri invalid!\n")
        return
    data_tranzactie = []
    for i in range(0, 3):
        data_tranzactie.append(int(params[i]))
    suma_tranzactie = float(params[3])
    tip_tranzactie = params[4]
    sterge_tranzactie_service(l_tr, data_tranzactie, suma_tranzactie, tip_tranzactie)


def tipareste_tranzactii_ui(l_tr, params):
    if len(params) != 0:
        print("Numar parametri invalid!\n")
        return
    if numar_tranzactii(l_tr) == 0:
        print("Nu exista tranzactii\n")
        return
    tranzactii = get_all_service_tranzactii(l_tr)
    for tranzactie in tranzactii:
        print(tranzactie, "\n")


def ui_modifica_tranzactie(l_tr, params):
    if len(params) != 6:
        print("Numar parametri invalid!\n")
        return
    tranzactie = l_tr[int(params[0])-1]
    data_noua = []
    for i in range(1, 4):
        data_noua.append(int(params[i]))
    suma_noua = float(params[4])
    tip_nou = params[5]
    tranzactie_noua = creeaza_tranzactie(data_noua, suma_noua, tip_nou)
    modifica_tranzactie(tranzactie, tranzactie_noua)


def ui_cauta_tranzactii_suma(l_tr, params):
    if len(params) != 1:
        print("Numar parametri invalid!\n")
        return
    suma_cautata = float(params[0])
    l_tr_cautate = cautare_tranzactii_dupa_suma(l_tr, suma_cautata)
    for tranzactie in l_tr_cautate:
        print(tranzactie, "\n")


def ui_cauta_tranzactii_data_si_suma(l_tr, params):
    if len(params) != 4:
        print("Numar parametri invalid!\n")
        return
    data_tr = []
    for i in range(0, 3):
        data_tr.append(int(params[i]))
    suma_cautata = float(params[3])
    l_tr_cautate = cautare_tranzactii_dupa_data_si_suma(l_tr, data_tr, suma_cautata)
    for tranzactie in l_tr_cautate:
        print(tranzactie, "\n")


def ui_cauta_tranzactii_tip(l_tr, params):
    if len(params) != 1:
        print("Numar parametri invalid!\n")
        return
    tip_cautat = params[0]
    l_tr_cautate = cautare_tranzactii_dupa_tip(l_tr, tip_cautat)
    for tranzactie in l_tr_cautate:
        print(tranzactie, "\n")


def ui_suma_totala_tranzactii_tip(l_tr, params):
    if len(params) != 1:
        print("Numar parametri invalid!\n")
        return
    tip = params[0]
    print(suma_tranzactii_tip(l_tr, tip))


def ui_sold_cont_data(l_tr, params):
    if len(params) != 3:
        print("Numar parametri invalid!\n")
        return
    data = []
    for i in range(0, 3):
        data.append(int(params[i]))
    print(sold_cont_data(l_tr, data))


def ui_elimina_tranzactii_tip(l_tr, params):
    if len(params) != 1:
        print("Numar parametri invalid!\n")
        return
    tip = params[0]
    filtreaza_tranzactie_tip(l_tr, tip)


def ui_elimina_tranzactii_tip_suma(l_tr, params):
    if len(params) != 2:
        print("Numar parametri invalid!\n")
        return
    tip_spec = params[0]
    suma_spec = float(params[1])
    filtreaza_tranzactii_tip_si_suma(l_tr, tip_spec, suma_spec)


def ui_sterge_tranzactie_data(l_tr, params):
    if len(params) != 3:
        print("Numar parametri invalid!\n")
        return
    data = []
    for i in range(0, 3):
        data.append(int(params[i]))
    sterge_tranzactie_data(l_tr, data)


def ui_sterge_tranzactie_perioada(l_tr, params):
    if len(params) != 6:
        print("Numar parametri invalid!\n")
        return
    data1 = []
    data2 = []
    for i in range(0, 3):
        data1.append(int(params[i]))
    for i in range(4, 7):
        data2.append(int(params[i]))
    sterge_tranzactii_perioada(l_tr, data1, data2)


def undo(l_tr, s, inputs):
    if len(s) == 0:
        print("No operations left to undo!\n")
        return
    op = s.pop()
    if op[0] == "sterge_tranzactii_tip" or op[0] == "filtreaza_tranzactii_tip" or \
            op[0] == "sterge_tranzactii_data" or op[0] == "filreaza_tranzactii_perioada" or \
            op[0] == "filreaza_tranzactii_tip_suma":
        l_tr[:] = [
            tranzactie for tranzactie in op[1]
        ]
    else:
        inputs[op[0]](l_tr, op[1])


def print_menu():
    print("Comenzi:")
    print("- comenzi?\n"
          "- adauga_tranzactie\n- tipareste_lista_tranzactii\n- sterge_tranzactii_data\n"
          "- actualizeaza_data_tranzactie\n- actualizeaza_suma_tranzactie\n- actualizeaza_tip_tranzactie\n"
          "- sterge_tranzactii_perioada\n- sterge_tranzactii_tip\n- cauta_tranzactii_suma\n"
          "- cauta_tranzactii_data_si_suma\n- cauta_tranzactii_tip\n- tipareste_suma_totala_tranzactii_tip\n"
          "- soldul_contului_data\n- filtreaza_tranzactii_tip\n- filtreaza_tranzactii_tip_suma\n- alternate_ui\n"
          "- undo\n- exit\n")


def adauga_stiva_undo(input1, l_tr, tr_copy, s, params):
    tr_copy2 = []
    if input1 == "adauga_tranzactie":
        s.append(("sterge_tranzactie", params))
    if input1 == "actualizeaza_tranzactie":
        data_tr = get_data_tranzactie(l_tr[int(params[0])-1])
        suma_tr = get_suma_tranzactie(l_tr[int(params[0])-1])
        tip_tr = get_tip_tranzactie(l_tr[int(params[0])-1])
        s.append(("actualizeaza_tranzactie", [params[0], data_tr[0], data_tr[1], data_tr[2], suma_tr, tip_tr]))
    if input1 == "sterge_tranzactii_tip" or input1 == "filtreaza_tranzactii_tip" or \
            input1 == "sterge_tranzactii_data" or input1 == "filreaza_tranzactii_perioada" or \
            input1 == "filtreaza_tranzactii_tip_suma":
        tr_copy2[:] = [
            tranzactie for tranzactie in tr_copy
        ]
        s.append((input1, tr_copy2))


def alternate_ui(inputs, tranzactii, tr_copy, s):
    while True:
        input_str = input(">>>")
        input_array = input_str.split(";")
        for i in range(0, len(input_array)):
            cmd_elems = input_array[i].split(" ")
            comanda = cmd_elems[0]
            if comanda == "":
                continue
            if comanda == "return":
                return
            params2 = cmd_elems[1:]
            for param2 in params2:
                param2 = param2.strip()
            if comanda in inputs:
                if comanda == "comenzi?":
                    inputs["comenzi?"]()
                elif comanda == "undo":
                    inputs["undo"](tranzactii, s, inputs)
                else:
                    if comanda == "tipareste_tranzactii":
                        pass
                    else:
                        tr_copy[:] = [tr for tr in tranzactii]
                    inputs[comanda](tranzactii, params2)
                    adauga_stiva_undo(comanda, tranzactii, tr_copy, s, params2)
            else:
                print("Comanda invalida!\n")


def ruleaza_ui():
    tranzactii = []
    tr_copy = []
    s = []
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Meniu aplicatie")
    print("- 'comenzi?' pentru meniul de comenzi\n- 'exit' pentru a iesi din aplicatie")
    inputs = {
        "comenzi?": print_menu,
        "adauga_tranzactie": adauga_tranzactii_ui,
        "sterge_tranzactie": sterge_tranzactie_ui,
        "tipareste_tranzactii": tipareste_tranzactii_ui,
        "actualizeaza_tranzactie": ui_modifica_tranzactie,
        "sterge_tranzactii_data": ui_sterge_tranzactie_data,
        "sterge_tranzactii_perioada": ui_sterge_tranzactie_perioada,
        "sterge_tranzactii_tip": ui_elimina_tranzactii_tip,
        "cauta_tranzactii_suma": ui_cauta_tranzactii_suma,
        "cauta_tranzactii_data_si_suma": ui_cauta_tranzactii_data_si_suma,
        "cauta_tranzactii_tip": ui_cauta_tranzactii_tip,
        "tipareste_suma_totala_tranzactii_tip": ui_suma_totala_tranzactii_tip,
        "soldul_contului_data": ui_sold_cont_data,
        "filtreaza_tranzactii_tip": ui_elimina_tranzactii_tip,
        "filtreaza_tranzactii_tip_suma": ui_elimina_tranzactii_tip_suma,
        "alternate_ui": alternate_ui,
        "undo": undo,
    }
    while True:
        input0 = input(">>>")
        input0 = input0.strip()
        if input0 == "":
            continue
        if input0 == "exit":
            return
        if input0 == "alternate_commands":
            inputs["alternate_ui"](inputs, tranzactii, tr_copy, s)
        else:
            parti = input0.split()
            input1 = parti[0]
            params = parti[1:]
            for param in params:
                param = param.strip()
            if input1 in inputs:
                if input1 == "comenzi?":
                    inputs["comenzi?"]()
                elif input1 == "undo":
                    inputs["undo"](tranzactii, s, inputs)
                else:
                    if input1 == "tipareste_tranzactii":
                        pass
                    else:
                        tr_copy[:] = [tr for tr in tranzactii]
                    inputs[input1](tranzactii, params)
                    adauga_stiva_undo(input1, tranzactii, tr_copy, s, params)
            else:
                print("Comanda invalida!\n")
