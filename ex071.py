from time import sleep
print(f'{"-" * 20}\n{"BANCO CEV":^20}\n{"-" * 20}\n')
n = int(input('Qual valor deseja sacar? R$'))

num_cedulas_de_cinquenta = n // 50
num_cedulas_de_vinte = (n % 50) // 20
num_cedulas_de_dez = ((n % 50) % 20) // 10
num_cedulas_de_um = ((n % 50) % 20) % 10
lista_cedulas = {'50': num_cedulas_de_cinquenta, '20': num_cedulas_de_vinte,
                 '10': num_cedulas_de_dez, '1': num_cedulas_de_um}

print('\n\033[1;35mSACANDO...\033[m\n')
sleep(2)

for v, k in enumerate(lista_cedulas):
    if lista_cedulas[k] != 0:
        print(f'{lista_cedulas[k]} cédulas de R${k} reais.')
