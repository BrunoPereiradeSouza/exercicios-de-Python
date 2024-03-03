from time import sleep
maior, menor, termos, soma, media = 0, 0, 0, 0, 0
while True:
    n = int(input('Digite um número: '))
    termos += 1
    soma += n
    if termos == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    while True:
        r = str(input('Quer contiuar? [S/N]: ')).strip().upper()
        if r in 'SN':
            break
    if r == 'N':
        print('\n\033[1;35mENCERRANDO...\033[m\n')
        sleep(2)
        break
media = soma / termos
print(f'Você digitou {termos} termos e a média foi {media:.1f}')
print(f'Maior = {maior}     Menor = {menor}')
