def ajuda(func):
    from time import sleep
    while True:
        print(f'{cores["amarelo"]}{"=-=" * 15}\n{"SISTEMA DE AJUDA pyHELP":^45}\n{"=-=" * 15}')
        print(f'{cores["fechamento"]}', end='')
        sleep(1)
        txt = input(func).lower().strip()
        if txt == 'fim':
            print(f'{cores["vermelho"]}{"=-=" * 10}\n{"ATÉ LOGO":^30}\n{"=-=" * 10}')
            print(cores["fechamento"])
            sleep(2)
            break
        print(f'{cores["azul"]}{"=-=" * 15}\n{"ACESSANDO O MANUAL DO COMANDO "}\'{txt}\'\n'
              f'{"=-=" * 15}')
        print(cores['fechamento'], end='')
        sleep(2)
        print(cores['branco'])
        help(txt)
        print(cores['fechamento'], end='')
        sleep(2)


# Programa Pricipal
cores = {'amarelo': '\033[43m', 'azul': '\033[44m', 'branco': '\033[30;47m', 'fechamento':
         '\033[m', 'vermelho': '\033[41m'}
ajuda('Função ou Biblioteca (fim para encerrar) > ')
