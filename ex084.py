from time import sleep
pessoas, pesos = [], []
while True:
    pessoas.append(str(input('Nome: ')))
    pesos.append(float(input('Peso: ')))
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
print('\n\033[1;35mANALISANDO...\033[m\n')
sleep(2)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {max(pesos):.1f}kg. Peso de ', end='')
for i in range(0, len(pesos)):
    if pesos[i] == max(pesos):
        print(f'[{pessoas[i]}] ', end='')
print(f'\nO menor peso foi de {min(pesos)}kg. Peso de ', end='')
for i in range(0, len(pesos)):
    if pesos[i] == min(pesos):
        print(f'[{pessoas[i]}] ', end='')
