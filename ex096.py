def area(c, l):
    a = c * l
    print(f'\n{"=-=" * 15}')
    print(f'Um terreno com dimensões {c}x{l}m tem área igual a {a}m².')


# Programa Principal
area(float(input('Digite o comprimento do terreno: ')),
     float(input('Digite a largura do terreno: ')))
