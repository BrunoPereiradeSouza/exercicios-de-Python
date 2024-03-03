from time import sleep


def maior(* num):
    print(f'{"=-=" * 15}\nAnalisando os valores informados...')
    print('Valores informados = ', end='')
    for i in num:
        print(f'{i} ', end='')
        sleep(1)
    if len(num) == 0:
        n = 0
    else:
        n = max(num)
    print(f'\nQuantidade de valores = {len(num)}\nMaior valor'
          f' informado = {n}\n')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
