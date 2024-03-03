from random import randint
print('\033[1;35m==== JOGO DO PAR OU ÍMPAR ====\033[m\n')
x = 0
while True:
    situacao = ''
    n = int(input('Escolha um número: '))
    while True:
        opc = str(input('PAR OU ÍMPAR? [P/I]: ')).strip().upper()[0]
        if opc in 'PI':
            break
    pc = randint(0, 10)
    soma = n + pc
    if opc == 'I':
        if soma % 2 == 0:
            situacao = '\033[1;31mVOCÊ PERDEU!\033[m'
        else:
            situacao = '\033[1;32mVOCÊ GANHOU!\033[m'
            x += 1
    elif opc == 'P':
        if soma % 2 == 0:
            situacao = '\033[1;32mVOCÊ GANHOU!\033[m'
            x += 1
        else:
            situacao = '\033[1;31mVOCÊ PERDEU!\033[m'
    print(f'\nVocê = {n}\nPC = {pc}\nResultado = {situacao}')
    if situacao == '\033[1;31mVOCÊ PERDEU!\033[m':
        break
print(f'\nGAMEOVER! Você venceu {x} vezes.')
