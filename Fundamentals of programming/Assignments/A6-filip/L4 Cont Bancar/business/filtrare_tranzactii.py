def filtrare_tip_tranzactii(l_tr_cautate, tip_spec):
    '''
    returneaza o lista de tranzactii filtrate dupa un tip specificat string tip_spec
    din lista de tranzactii cautate l_tr_cautate
    :param l_tr_cautate: lista tranzactiilor cautate
    :param tip_spec: string
    :return: rez: lista de tranzactii filtrate
    '''
    l_tr_filtrata = []
    for tranzactie in l_tr_cautate:
        if tranzactie['tip'] != tip_spec:
            l_tr_filtrata.append(tranzactie)
    return l_tr_filtrata


def filtrare_tip_si_suma_tranzactii(l_tr_cautate, tip_spec, suma_spec):
    '''
    returneaza o lista de tranzactii filtrate dupa un tip specificat string tip_spec si
    mai mici decat o suma specificata float suma_spec, din lista de tranzactii cautate
    l_tr_cautate
    :param l_tr_cautate: lista de tranzactii cautate
    :param tip_spec: string
    :param suma_spec: float
    :return: lista de tranzactii filtrate
    '''
    l_tr_filtrata0 = filtrare_tip_tranzactii(l_tr_cautate, tip_spec)
    l_tr_filtrata_final = []
    for tranzactie in l_tr_filtrata0:
        if tranzactie['suma'] < suma_spec:
            l_tr_filtrata_final.append(tranzactie)
    return l_tr_filtrata_final

