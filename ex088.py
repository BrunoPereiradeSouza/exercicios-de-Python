from random import randint
from time import sleep
print(f'{"=-=" * 15}\n\033[1;35m{"SORTEAR JOGOS DA MEGA SENA":^45}\033[m\n{"=-=" * 15}\n')
jogos, jogo_temp = [], []
for i in range(1, int(input("Quantos jogos você quer que eu sorteie? ")) + 1):
    controle = 0
    while True:
        n = randint(1, 60)
        if n not in jogo_temp:
            jogo_temp.append(n)
            controle += 1
        if controle == 6:
            break
    jogo_temp.sort()
    jogos.append(jogo_temp[::])
    jogo_temp.clear()
z = 1
for jogo in jogos:
    print(f'{z}° jogo: {jogo} ')
    sleep(1)
    z += 1
