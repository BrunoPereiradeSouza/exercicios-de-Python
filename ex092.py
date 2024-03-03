from datetime import date
ano_atual = date.today().year
nome = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
pessoa = {'nome': nome, 'idade': ano_atual - ano_nasc,
          'ctps': int(input('Carteira de Trabalho [0 se não possuir]: '))}

if pessoa['ctps'] != 0:
    pessoa['Ano de contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = (pessoa['Ano de contratacao'] - ano_nasc) + 35
print(f'\n{"=-=" * 15}\n')
for informacao in pessoa:
    print(f'{informacao} = {pessoa[informacao]}')
