numeros = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0:
        numeros.insert(4, n)
        print('Valor adicionado ao final da lista...')
    else:
        if n > max(numeros):
            numeros.insert(4, n)
            print('Valor adicionado ao final da lista...')
        elif n < min(numeros):
            numeros.insert(0, n)
            print('Valor adicionado na posição 0 da lista...')
        else:
            if n <= numeros[1]:
                numeros.insert(1, n)
                print('valor adicionado na posição 1 da lista...')
            elif n <= numeros[2]:
                numeros.insert(2, n)
                print('valor adicionado na posição 2 da lista...')
            elif n <= numeros[3]:
                numeros.insert(3, n)
                print('valor adicionado na posição 3 da lista...')
print(f'{"=-=" * 20}\nA lista ordenada é {numeros}')
