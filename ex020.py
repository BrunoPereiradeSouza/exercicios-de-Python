from random import shuffle
from time import sleep
alunos = []
for i in range(1, 5):
    alunos.append(input(f'Digite o nome do {i}° aluno: '))
print('\033[1;31mSORTEANDO A ORDEM DE APRESENTAÇÃO...\033[m')
sleep(2)
shuffle(alunos)
print('=-=' * 20)
print(f'{alunos}')
