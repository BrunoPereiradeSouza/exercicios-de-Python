from time import sleep
jogador, gols = dict(), list()
jogadores = []

while True:
    total = 0
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(1, partidas + 1):
        n = int(input(f'N° de gols na {i}° partida: '))
        gols.append(n)
        total += n
    jogador['gols'] = gols[::]
    gols.clear()
    jogador['total'] = total
    jogadores.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
        else:
            print('ERRO! Por favor, digite somente S ou N.')
    if r == 'N':
        print('\n\033[1;35mCOMPUTANDO OS DADOS...\033[m\n')
        sleep(2)
        break
    print()

print(f'{"cod":<3}{"Nome":>15}{"gols":>15}{"total":>15}')
print('-' * 50)
for k, v in enumerate(jogadores):
    print(f'{k:<3}', end='')
    for i in v.values():
        print(f'{str(i):>15}', end='')
    print()

while True:
    c = int(input('\nQuer consultar as informações de qual jogador [999 para parar]: '))
    if c == 999:
        print('\n\033[1;35mENCERRANDO...\033[m')
        sleep(2)
        break
    else:
        if 0 <= c < len(jogadores):
            print(f'Levantamento do jogador \033[3;36m{jogadores[c]["nome"]}:\033[m')
            for i in range(0, len(jogadores[c]["gols"])):
                print(f'{" " * 4}{"<" * 3}Na {i + 1}° partida fez {jogadores[c]["gols"][i]} gols')
