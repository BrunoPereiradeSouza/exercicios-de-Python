from random import randint
from time import sleep
print('\033[1;35mPEDRA, PAPEL OU TESOURA!\033[m')
print('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')

opcao = int(input('Digite a sua opção: '))
print('\n\033[1;35mPEDRA!', end=' ')
sleep(0.5)
print('PAPEL!!', end=' ')
sleep(0.5)
print('TESOURA!!!\033[m\n')
sleep(0.5)
if opcao == 0 or opcao == 1 or opcao == 2:
    computador = randint(0, 2)
    opcoes = {0: 'Pedra', 1: 'Papel', 2: 'Tesoura'}
    empate = f'\033[1;33mEmpate!\033[m\nVocê = {opcoes[opcao]}\nPc = {opcoes[computador]}'
    derrota = f'\033[1;31mVocê perdeu!\033[m\nVocê = {opcoes[opcao]}\nPc = {opcoes[computador]}'
    vitoria = f'\033[1;32mVocê ganhou!\033[m\nVocê = {opcoes[opcao]}\nPc = {opcoes[computador]}'

    if opcao == 0:
        if computador == 0:
            print(empate)
        elif computador == 1:
            print(derrota)
        elif computador == 2:
            print(vitoria)
    elif opcao == 1:
        if computador == 0:
            print(vitoria)
        elif computador == 1:
            print(empate)
        elif computador == 2:
            print(derrota)
    elif opcao == 2:
        if computador == 0:
            print(derrota)
        elif computador == 1:
            print(vitoria)
        elif computador == 2:
            print(empate)
else:
    print('\033[1;31mOpção Inválida!\033[m')
