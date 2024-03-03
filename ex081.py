numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
numeros.sort(reverse=True)
print(f'\nVocê digitou {len(numeros)} números\nOs valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 \033[1;32mFAZ\033[m parte da lista!')
else:
    print('O valor 5 \033[1;31mNÃO\033[m faz parte da lista!')
