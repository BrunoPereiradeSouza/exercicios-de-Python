lista_completa, lista_pares, lista_impares = [], [], []

while True:
    numero = int(input('Digite um número: '))
    lista_completa.append(numero)
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
print(f'\nA lista completa é {lista_completa}\nA lista dos pares é {lista_pares}\nA lista dos '
      f'ímpares é {lista_impares}')
