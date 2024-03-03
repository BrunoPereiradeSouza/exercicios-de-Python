print('\033[1;35mCADASTRO DE PESSOAS\033[m\n')
maiores_idade, homem, mulher = 0, 0, 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    if idade > 18:
        maiores_idade += 1
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            break
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    print('-' * 30)
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
print(f'\nPessoas com mais de 18 anos = {maiores_idade}')
print(f'Total de homens = {homem}\nMulheres com menos de 20 anos = {mulher}')
