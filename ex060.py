print('\033[1;35mCÁLCULO DE FATORIAL\033[m\n')
n = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {n}! -> ', end='')
fatorial = 0
for i in range(n, 0, -1):
    if i == n:
        fatorial = i
    else:
        fatorial *= i

    print(f'{i} ', end='')
    if i != 1:
        print('x ', end='')
    else:
        print(f'= {fatorial}.')
