from time import sleep
print('=' * 40)
print(f'{"10 TERMOS DE UMA PA":^40}')
print('=' * 40)
p = int(input('Primeiro termo: '))
r = int(input('razão da PA: '))

for i in range(0, 10):
    print(f'{p} -> ', end='')
    sleep(0.5)
    p += r
print('ACABOU!')
