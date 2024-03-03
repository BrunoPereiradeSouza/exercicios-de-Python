from time import sleep
print('\033[1;35m==== CONSULTE TERMOS DE UMA PA ====\033[m\n')
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
i, f = 0, 10

while True:
    for x in range(i, f):
        print(f'{p} -> ', end='')
        p += r
    print('PAUSA!')
    m = int(input('Quantos termos você ainda quer consultar? '
                  '[ 0 ] para sair: '))
    if m == 0:
        print('\n\033[1;35mENCERRANDO...\033[m')
        sleep(2)
        break
    else:
        i = f
        f += m
print(f'FIM!\nTERMOS EXIBIDOS = {f}')
