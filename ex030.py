print('\033[1;34mIMPAR OU PAR!!\033[m\n')
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'{num} é \033[2;32mPAR!\033[m')
else:
    print(f'{num} é \033[1;31mÍMPAR!!\033[m')
