print('\033[1;33mCONVERSOR DE BASES\033[m')
print('=-=' * 10)
n = int(input('Digite um número: '))
print('''
Escolha uma das bases para conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL
''')
opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    print(f'{n} em binário = {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} em octal = {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} em hexadecimal = {hex(n)[2:]}')
else:
    print('\033[1;31mOpção inválida!\033[m')
