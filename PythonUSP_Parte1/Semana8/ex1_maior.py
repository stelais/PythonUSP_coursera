def maior_elemento(lista):
    biggest = lista[0]
    for i in lista:
        if i <= biggest:
            pass
        else:
            biggest = i	
    return biggest


def teste():
    lista=[1,7,3,6]
    print(maior_elemento(lista))


