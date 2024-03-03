while True:
    sexo = str(input('Informe o seu sexo [M/F]: ')).upper().strip()[0]
    if sexo in 'MF':
        break
    else:
        print('Dados Inválidos. ', end='')
print(f'\nSexo {sexo} informado com sucesso!')
