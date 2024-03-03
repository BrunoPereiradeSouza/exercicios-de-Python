print('=-=' * 10)
print('\033[1;35mNUBANK EMPRÉSTIMOS\033[m')
print('=-=' * 10)
valor_casa = float(input('\nQual o valor da casa que você deseja comprar?'
                         ' R$'))
salario = float(input('Qual o seu salário mensal? R$'))
anos = int(input('Em quantos anos você deseja pagar a casa? '))
print('=-=' * 20)
num_parcelas = anos * 12
valor_parcela = valor_casa / num_parcelas
if valor_parcela > (salario * (30 / 100)):
    print(f'Empréstimo \033[1;31mNEGADO!\033[m O valor da parcela'
          f' (R${valor_parcela:.2f}) excede 30% do seu salário mensal!')
elif 0 < valor_parcela <= (salario * (30 / 100)):
    print(f'Empréstimo \33[1;32mAPROVADO!\033[m\nValor da parcela = '
          f'R${valor_parcela:.2f}')
