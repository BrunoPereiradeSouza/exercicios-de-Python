print('\033[1;32mCÁLCULO DE REAJUSTE SALARIAL!\033[m\n Veja as porcentagens abaixo:')
print('\033[1;34mSalário <= R$1250.00 = 15%\nSalário > R$1250.00 = 10%\033[m\n')
salario = float(input('Digite o seu salário: R$'))
print('=-=' * 20)
novo_salario = 0
if 0 < salario <= 1250:
    novo_salario = salario + (salario * (15 / 100))
    print(f'Você recebeu \033[1;32m15% de aumento\033[m!\n'
          f'Novo salário = R$ {novo_salario:.2f}')
elif salario > 1250:
    novo_salario = salario + (salario * (10 / 100))
    print(f'Você recebeu \033[1;32m10% de aumento\033[m!\n'
          f'Novo salário = R$ {novo_salario:.2f}')
else:
    print('\033[1;31mSalário Inválido!\033[m')
