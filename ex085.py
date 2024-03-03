numeros = [[], []]
for i in range(0, 7):
    numero = int(input(f'Digite o {i + 1}° valor: '))
    if numero % 2 == 0:
        numeros[0].insert(len(numeros[0]), numero)
    else:
        numeros[1].insert(len(numeros[1]), numero)
numeros[0].sort()
numeros[1].sort()
print(f'\nOs valores pares digitados foram {numeros[0]}\nOs valores ímpares digitados foram '
      f'{numeros[1]}')
