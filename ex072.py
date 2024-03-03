nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    n = int(input('Digite um número inteiro entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    else:
        print('Tente novamente! ', end='')
print(f'\nVocê digitou o número {nums[n]}')
