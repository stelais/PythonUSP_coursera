def remove_repetidos(lista):
    nova_lista=[]
    for i in range(len(lista)):
        if lista[i] in nova_lista:
            pass
        else:
            nova_lista.append(lista[i])
    return sorted(nova_lista)        

def teste():
    lista = [1, 2, 3, 3, 3, 4]
    print (remove_repetidos(lista))
   

    