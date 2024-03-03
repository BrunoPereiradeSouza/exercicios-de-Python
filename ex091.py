from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Bruno': randint(1, 6), 'Clarisse': randint(1, 6), 'Thamires': randint(1, 6),
             'Álex': randint(1, 6)}
print(f'{"=-=" * 15}\n\033[1;36m{"JOGANDO OS DADOS...":^45}\033[m\n{"=-=" * 15}\n')
sleep(3)
for jogador in jogadores:
    print(f'{jogador} tirou {jogadores[jogador]}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('\n=== RANKING DE JOGADORES ===')
for v, k in enumerate(ranking):
    print(f'{v + 1}° - {k[0]}')
    sleep(1)
