from time import sleep
print('\033[1;35mTABUADA!\033[m\n')
while True:
    n = int(input('Quer ver a tabuada de qual valor? [ número negativo para encerrar]: '))
    if n < 0:
        print('\n\033[1;35mENCERRANDO...\033[m')
        sleep(2)
        break

    for i in range(1, 11):
        print(f'{n} x {i:2} = {n * i}')
