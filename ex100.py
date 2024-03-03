from random import randint
from time import sleep


def sorteia(lista):
    print('Valores sorteados: ', end='')
    for i in range(0, 5):
        lista.append(randint(0, 10))
        print(f'{lista[i]} ', end='')
        sleep(1)


def somapar(lista):
    soma_pares = 0
    for i in lista:
        if i % 2 == 0:
            soma_pares += i
    print(f'\nSomando os valores pares da lista {lista} temos = {soma_pares}')


# Programa Principal
numeros = []
sorteia(numeros)
somapar(numeros)
