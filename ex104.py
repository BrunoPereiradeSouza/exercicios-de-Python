def leiaint(txt):
    while True:
        n = input(txt).strip()
        if n.isnumeric():
            print()
            return n
        else:
            print('\033[1;31mERRO! POR FAVOR, INFORME UM NÚMERO VÁLIDO!\033[m')


# Programa Principal
n1 = leiaint('Digite um número: ')
print(f'Você digitou o número {n1}')
