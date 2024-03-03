from time import sleep


def contador():
    i, f, p = 1, 10, 1
    print(f'Contando de {i} até {f} de {p} em {p}')
    for x in range(i, f + 1, p):
        print(f'{x} ', end='')
    print('FIM!\n')
    i, f, p = 10, 0, 2
    print(f'Contando de {i} até {f} de {p} em {p}')
    for x in range(i, f - 1, -p):
        print(f'{x} ', end='')

    print('FIM!\n')
    print('Agora é a sua vez de personalizar!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('passo: '))
    if p < 0:
        p = -p
    if p == 0:
        p = 1
    print(f'Contando de {i} até {f} de {p} em {p}')
    if f < i:
        p = -p
        n = -1
    else:
        n = +1
    for x in range(i, f + n, p):
        print(f'{x} ', end='')
        sleep(0.5)
    print('FIM!')


# Programa Principal
contador()
