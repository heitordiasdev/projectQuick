import random

def quicksort(lista):
    listaMaior = []
    listaMenor = []
    tamanho = len(lista)

    if tamanho <= 1:
        return lista
    else:
        pivo = lista.pop()

    for x in lista:
        if x > pivo:
            listaMaior.append(x)

        elif x < pivo:
            listaMenor.append(x)

    menorLista = quicksort(listaMenor)
    maiorLista = quicksort(listaMaior)

    sequenciaOrdenada = menorLista + [pivo] + maiorLista
    return sequenciaOrdenada