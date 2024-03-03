print('=====10 TERMOS DE UMA PA=====\n')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
print('=-=' * 20)
i = 0
while i < 10:
    print(f'{p} -> ', end='')
    p += r
    i += 1
print('FIM!')
