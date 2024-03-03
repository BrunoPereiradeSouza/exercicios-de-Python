from random import randint
maior, menor = 0, 0
numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9),
           randint(0, 9))
print('On números sorteados foram: ', end='')

for i in numeros:
    if numeros.index(i) == 0:
        maior = i
        menor = i
    else:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
    print(f'{i} ', end='')
print(f'\nMaior = {maior}\nMenor = {menor}')
