jogador = {'nome': str(input('Nome do Jogador: '))}
tot_gols = 0
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for i in range(1, partidas + 1):
    n = int(input(f'Quantos gols na partida {i}? '))
    gols.append(n)
    tot_gols += n
jogador['gols'] = gols[::]
jogador['total'] = tot_gols
print(f'\n{jogador}')
print(f'{"=-=" * 20}\n')
for inf in jogador:
    print(f'O campo {inf} tem o valor {jogador[inf]}')
print(f'{"=-=" * 20}\nO jogador {jogador["nome"]} jogou {partidas} partidas: ')
for k, v in enumerate(jogador['gols']):
    print(f'   =>Na partida {k + 1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols.')
