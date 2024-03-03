lista, maior, menor = [], 0, 0
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
for i in lista:
    if lista.index(i) == 0:
        maior = i
        menor = i
    else:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
print(f'\nValores digitados = {lista}\nMaior = {maior}\nMenor = {menor}')
