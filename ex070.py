from time import sleep
print('-' * 30)
print(f'\033[1;35m{"LOJAS SUPER VAREJO":^30}\033[m')
print('-' * 30)
total, maior_mil, menor_preco, nome_menor_preco = 0, 0, 0, ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    if total == 0:
        menor_preco = preco
        nome_menor_preco = nome
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_menor_preco = nome
    total += preco
    if preco > 1000:
        maior_mil += 1
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        print('\n\033[1;35mCALCULANDO...\033[m')
        sleep(2)
        break
print(f'\nTOTAL = R$ {total:.2f}\nProdutos que custam mais de mil reais = {maior_mil}')
print(f'Menor preço = {nome_menor_preco}, R$ {menor_preco:.2f}')
