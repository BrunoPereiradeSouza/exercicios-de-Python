from random import choice
alunos = []
for i in range(1, 5):
    alunos.append(input(f'Digite o nome do {i}° aluno: '))
print('=-=' * 20)
print(f'O(a) aluno(a) sorteado(a) foi {choice(alunos)}')
