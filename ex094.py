pessoas, lista = dict(), list()
media, soma_idades = 0, 0
while True:
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    lista.append(idade)
    lista.append(sexo)
    pessoas[nome] = lista[::]
    lista.clear()
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            print()
            break
        else:
            print('ERRO! Por favor, digite apenas S ou N.')
    if r == 'N':
        break
print(f'\nA) Ao todo temos {len(pessoas)} pessoas;')
for pessoa in pessoas:
    soma_idades += pessoas[pessoa][0]
media = soma_idades / len(pessoas)
print(f'B) A média de idade do grupo é {media:.1f} anos;')
print('c) As mulheres do grupo são ', end='')
for pessoa in pessoas:
    if pessoas[pessoa][1] == 'F':
        print(f'{pessoa} ', end='')
print('\nD)Lista das pessoas que estão com a idade acima da média: ')
for pessoa in pessoas:
    if pessoas[pessoa][0] > media:
        print(f'{" " * 4}{"Nome:"} {pessoa}{" " * 3}idade: {pessoas[pessoa][0]}{" " * 3}sexo: '
              f'{pessoas[pessoa][1]}')
