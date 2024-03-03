print('\033[1;35m==== SEQUÊNCIA DE FIBONACCI ====\033[m\n')
n = int(input('Quantos termos você quer mostrar? '))

a, b, c = 0, 1, 0

for i in range(0, n):
    print(f'{a} -> ', end='')
    c = a
    a += b
    b = c
print('FIM!')
