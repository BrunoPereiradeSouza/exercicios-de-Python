print('\033[2;32mPINTANDO A PAREDE\033[m')
print('=-=' * 20)
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = altura * largura
tinta = area / 2
print(f'A parede de dimensões {largura}m x {altura}m tem área igual a {area}m²')
print(f'Você precisará de {tinta} litros de tinta para pintar a parede.')
