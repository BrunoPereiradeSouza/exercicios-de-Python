print('\033[2;32mCalculando reajuste salarial\033[m')
print('=-=' * 20)
salario_atual = float(input('Digite o salário: R$'))
novo_salario = salario_atual + (salario_atual * (15 / 100))
print(f'Após o aumento de 15% o salário de R$ {salario_atual} será = R$ {novo_salario}')
