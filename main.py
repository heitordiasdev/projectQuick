from algoritmo import *

def main():
    # Aplicando 100 números aleatórios
    lista= random.sample(range(1000), 100)

    with open("texto/ordenado.txt", "w") as arq:
        arq.write(str(lista))
    with open("texto/ordenado.txt", "r") as arq:
        sequencia = arq.read()
        print(sequencia)

        lista1= quicksort(lista)
        print(lista1)
    with open("texto/ordenado.txt", "w") as arq:
        arq.write(str(lista1))

main()