numeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado! Não vou adicionar...')
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
numeros.sort()
print(f'{"=-=" * 20}\nVocê digitou os valores {numeros}')
