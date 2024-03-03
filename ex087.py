from time import sleep
soma_pares, soma_terceira_coluna, maior_segunda_linha = 0, 0, 0
matriz = [[], [], []]
for i in range(0, 3):
    for x in range(0, 3):
        matriz[i].insert(x, int(input(f'Digite o valor para [{i}, {x}]: ')))
print(f'\n\033[1;35mGERANDO MATRIZ...\033[m\n')
sleep(2)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}] ', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_terceira_coluna += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior_segunda_linha:
                maior_segunda_linha = matriz[l][c]
    print()

print(f'\nA soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')
