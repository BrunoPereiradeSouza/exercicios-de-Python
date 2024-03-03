from time import sleep
matriz = [[], [], []]
for i in range(0, 3):
    for x in range(0, 3):
        matriz[i].insert(x, int(input(f'Digite o valor para [{i}, {x}]: ')))
print(f'\n\033[1;35mGERANDO MATRIZ...\033[m\n')
sleep(2)
for lista in matriz:
    for n in lista:
        print(f'[{n:^3}] ', end='')
    print()
