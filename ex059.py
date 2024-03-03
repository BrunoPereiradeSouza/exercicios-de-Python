from time import sleep
maior = 0
menor = 0
while True:
    n1 = int(input('1° valor: '))
    n2 = int(input('2° valor: '))
    while True:
        print('=-=' * 20)
        print('''
            [ 1 ] Somar;
            [ 2 ] Multiplicar;
            [ 3 ] Maior;
            [ 4 ] Novos números;
            [ 5 ] Sair do programa;
            ''')
        while True:
            opcao = int(input('Qual a sua opção? '))
            if 0 < opcao < 6:
                break
            else:
                print('opção inválida! ', end='')
        if opcao == 5:
            print('\033[1;35mENCERRANDO...\033[m')
            sleep(2)
            break
        else:
            if opcao == 1:
                print(f'{n1} + {n2} = {n1 + n2}')
            elif opcao == 2:
                print(f'{n1} x {n2} = {n1 * n2}')
            elif opcao == 3:
                if n1 > n2:
                    maior = n1
                    menor = n2
                elif n2 > n1:
                    maior = n2
                    menor = n1
                else:
                    print(f'{n1} = {n2}.')
                print(f'{maior} é maior que {menor}.')
            elif opcao == 4:
                break
            sleep(1)
    if opcao == 5:
        break
