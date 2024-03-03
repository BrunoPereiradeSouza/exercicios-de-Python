aluno = {'nome': str(input('Nome: '))}
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = '\033[1;32mAPROVADO\033[m'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = '\033[1;33mRECUPERAÇÃO\033[m'
elif 0 <= aluno['media'] < 5:
    aluno['situacao'] = '\033[1;31mREPROVADO\033[m'
else:
    aluno['situacao'] = 'Média inválida!'
print(f'\nNome do aluno = {aluno["nome"]}\nMédia de {aluno["nome"]} = {aluno["media"]}')
print(f'Situação de {aluno["nome"]} = {aluno["situacao"]}')
