from random import randint
from time import sleep
print('\033[4;34m=-=\033[m' * 20)
print('\033[3;33mVOU PENSAR EM UM NÚMERO DE 0 A 5...\033[m')
print('\033[4;34m=-=\033[m' * 20)
num = randint(0, 5)
tentativa = int(input('Em que número pensei? '))
print('\n\033[5;35mPROCESSANDO...\033[m\n')
sleep(2)
if tentativa == num:
    print(f'\033[2;32mVocê ganhou!! Eu pensei no número {num}.\033[m')
else:
    print(f'\033[1;31mEu ganhei!! Pensei no número {num}')
