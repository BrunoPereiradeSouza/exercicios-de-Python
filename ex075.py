numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um '
           'número: ')), int(input('Digite um número: ')))
print(f'\nO valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro valor 3 apareceu na posição {numeros.index(3) + 1}')
else:
    print('O valor 3 não apareceu nenhuma vez na tupla.')
print('Os valores pares são: ', end='')
for i in numeros:
    if i % 2 == 0:
        print(f'{i} ', end='')
