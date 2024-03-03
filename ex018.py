from math import sin, cos, tan, radians
x = float(input('Digite um ângulo: '))
angulo = radians(x)
print('=-=' * 20)
print(f'Seno de {x}° = {sin(angulo):.2f}\nCosseno de {x}° = {cos(angulo):.2f}\nTangente de {x} = '
      f'{tan(angulo):.2f}')
