def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
            return num
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não informar o valor inteiro.\033[m')
            return 0
        except:
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')


def leiareal(txt):
    while True:
        try:
            num = float(input(txt))
            return num
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não informar o valor real.\033[m')
            return 0
        except:
            print('\033[0;31mERRO! DIGITE UM NÚMERO REAL VÁLIDO!\033[m')


n1 = leiaint('Digite um número inteiro: ')
n2 = leiareal('Digite um número real: ')
print(f'\nNúmero Inteiro = {n1}\nNúmero real = {n2}')
