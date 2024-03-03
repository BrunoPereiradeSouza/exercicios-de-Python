maior, menor = 0, 0
for i in range(1, 6):
    peso = float(input(f'Peso da {i}° pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(F'\nMaior peso = {maior}kg\nMenor peso = {menor}kg')
