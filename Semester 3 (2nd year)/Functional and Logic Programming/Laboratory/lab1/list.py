class Nod:
    def __init__(self, e):
        self.e = e
        self.urm = None


class Lista:
    def __init__(self):
        self.prim = None


'''
crearea unei liste din valori citite pana la 0
'''


def creareLista():
    lista = Lista()
    lista.prim = creareLista_rec()
    return lista


def creareLista_rec():
    x = int(input("x="))
    if x == 0:
        return None
    else:
        nod = Nod(x)
        nod.urm = creareLista_rec()
        return nod


'''
tiparirea elementelor unei liste
'''


def tipar(lista):
    tipar_rec(lista.prim)


def tipar_rec(nod):
    if nod != None:
        print(nod.e)
        tipar_rec(nod.urm)


'''
program pentru test
'''


def createList(list: Lista):
    myList = []
    nod = list.prim
    while nod != None:
        myList.append(nod.e)
        nod = nod.urm
    return myList


def addEvenSubstractOdd(lista):
    """
    Returns the number obtained by adding all even numbers and substracting all the odd ones from the list.

    :param lista: Lista
    :return: int
    """
    number = 0
    nod = lista.prim
    return addEvenSubstractOddRec(number, nod)


def addEvenSubstractOddRec(number, nod):
    if nod == None:
        return number
    if nod.e % 2 == 0:
        return addEvenSubstractOddRec(number + nod.e, nod.urm)
    else:
        return addEvenSubstractOddRec(number - nod.e, nod.urm)


def setDifference(set1: Lista, set2: Lista):
    """
    Returns the difference of the 2 sets.

    :param set1: Lista
    :param set2: Lista
    :return:
    """
    return setDifferenceRec(set1.prim, set2, [])


def setDifferenceRec(nod1: Nod, set2: Lista, myList):
    if nod1 == None:
        return myList
    else:
        currentNode = set2.prim
        ok = 1
        while currentNode != None and ok:
            if currentNode.e == nod1.e:
                ok = 0
            currentNode = currentNode.urm
        if ok:
            myList.append(nod1.e)
        return setDifferenceRec(nod1.urm, set2, myList)


def exA():
    print("a:")
    list = creareLista()
    tipar(list)
    number = addEvenSubstractOdd(list)
    print(number)


def exB():
    print("b:")
    list1 = creareLista()
    tipar(list1)
    list2 = creareLista()
    tipar(list2)
    myList = setDifference(list1, list2)
    print(myList)


def main():
    exA()
    exB()


main()
