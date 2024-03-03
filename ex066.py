from time import sleep
t, s = 0, 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        print('\n\033[1;35mENCERRANDO...\033[m\n')
        sleep(2)
        break
    else:
        t += 1
        s += n
print(f'Número de valores digitados = {t}\nSoma = {s}')
