def leiadin(txt):
    while True:
        n = input(txt).replace(',', '.').strip()
        n1 = ''.join(n.split())
        if n1.isalnum() and not n1.isnumeric() or n == '':
            print(F'\033[1;31mERRO! O VALOR \'{n1}\' NÃO É VÁLIDO!\033[m')
        else:
            return float(n1)


def leiaint(txt):
    while True:
        n = input(txt).strip()
        if n.isnumeric():
            print()
            return n
        else:
            print('\033[1;31mERRO! POR FAVOR, INFORME UM NÚMERO VÁLIDO!\033[m')