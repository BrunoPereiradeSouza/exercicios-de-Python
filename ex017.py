from math import sqrt
print('\033[2;32mCálculo de Hipotenusa\033[m')
print('=-=' * 20)
cateto_oposto = float(input('Digite a medida do cateto oposto: '))
cateto_adjacente = float(input('Digite a medida do cateto adjacente: '))
hipo_quadrado = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
hipotenusa = sqrt(hipo_quadrado)
print(f'Hipotenusa = {hipotenusa:.2f}')
