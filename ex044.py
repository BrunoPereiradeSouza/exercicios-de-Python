from time import sleep
title = '\033[1;34mSuper Varejo\033[m'
print('=-=' * 10)
print(f'{title:^40}')
print('=-=' * 10)
novo_preco = 0
preco = float(input('Informe o valor da compra: R$'))
print('''\nOpções de Pagamento:
[ 1 ] - À vista no dinheiro/cheque;
[ 2 ] - Á vista no cartão;
[ 3 ] - Até 2x no cartão;
[ 4 ] - 3x ou mais no cartão;
''')
opcao = int(input('Digite a sua opção de pagamento: '))
valor_parcela = 0
if opcao == 1:
    novo_preco = preco - (preco * (10 / 100))
elif opcao == 2:
    novo_preco = preco - (preco * (5 / 100))
elif opcao == 3:
    parcelas = int(input('Digite o número de parcelas [1 ou 2]: '))
    if parcelas == 1:
        novo_preco = preco
        valor_parcela = preco
    elif parcelas == 2:
        novo_preco = preco
        valor_parcela = preco / 2
    else:
        print('Número de parcelas inválido!')
elif opcao == 4:
    parcelas = int(input('Digite o número de parcelas [3 ou mais]: '))
    novo_preco = preco + (preco * (20 / 100))
    valor_parcela = novo_preco / parcelas
print('\033[1;35mCALCULANDO...\033[m\n')
sleep(3)

print(f'Opção = {opcao}')
if opcao == 3 or opcao == 4:
    print(f'Número de parcelas = {parcelas}\nValor de cada parcela = '
          f'R${valor_parcela:.2f}')
print()
print(f'Valor inicial = R${preco:.2f}\nValor final = R${novo_preco:.2f}')
