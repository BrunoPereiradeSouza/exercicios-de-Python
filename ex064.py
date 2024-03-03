from time import sleep
s,  t = 0, 0
while True:
    n = int(input('Digite um número [ 999 para parar]: '))
    if n == 999:
        print('\n\033[1;35mCALCULANDO...\033[m\n')
        sleep(2)
        break
    else:
        s += n
        t += 1
print(f'A soma entre os {t} termos digitados é {s}.')
