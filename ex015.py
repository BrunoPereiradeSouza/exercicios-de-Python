print('\033[6;36mCalculando aluguel de carro\033[m')
print('-' * 20)
print('\033[1;31mATENÇÃO AOS VALORES!\n\033[mKm rodado = R$0.15\nDia de uso = R$60.00')
print('-' * 20)
km = float(input('Digite a quantidade de km rodados: '))
dias = float(input('Digite a quantidade de dias rodados: '))
valor = (km * 0.15) + (dias * 60)
print(f'O valor a ser pago é = R$ {valor:.2f}')
