hidade, hnome, soma_idades, num_mulheres = 0, '', 0, 0
for i in range(1, 5):
    print(f'====== {i}° PESSOA ======')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    soma_idades += idade
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if sexo in 'MF':
            break
    if sexo == 'M':
        if i == 1:
            hidade = idade
            hnome = nome
        else:
            if idade > hidade:
                hidade = idade
                hnome = nome
    else:
        if idade < 20:
            num_mulheres += 1
    print()
media_idade = soma_idades / 4

print(f'\nMédia de idade do grupo = {media_idade:.0f} anos.')
print(f'Homem mais velho = {hnome} ({hidade} anos).')
print(f'Ao todo são {num_mulheres} mulheres com menos de 20 anos.')
