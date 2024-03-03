
from time import sleep
num = int(input('Informe um número: '))
unidade = ((num % 1000) % 100) % 10
dezena = ((num % 1000) % 100) // 10
centena = (num % 1000) // 100
milhar = num // 1000
print('=-=' * 20)
print(f'\033[3;33mAnalisando o número {num}\033[m\n')
sleep(2)
print(f'Unidade = {unidade}\nDezena = {dezena}\nCentena = {centena}\nMilhar = {milhar}')
