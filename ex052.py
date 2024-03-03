n = int(input('Digite um número: '))
print()
x = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(f'\033[1;32m{i}\033[m', end=' ')
        x += 1
    else:
        print(f'\033[1;31m{i}\033[m', end=' ')
print('\n')
if x > 2:
    print(f'{n} não é PRIMO!')
else:
    print(f'{n} é PRIMO!')
