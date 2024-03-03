from time import sleep
alunos, nome, notas, media_list, aluno = [], [], [], [], []
while True:
    nome.append(str(input('Nome: ')).strip())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2
    media_list.append(media)
    aluno.append(nome[::])
    aluno.append(notas[::])
    aluno.append(media_list[::])
    alunos.append(aluno[::])
    nome.clear()
    notas.clear()
    media_list.clear()
    aluno.clear()
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        print(f'\n\033[1;35mCALCULANDO MÉDIAS...\033[m')
        sleep(2)
        break
print(f'\n{"No.  "}{"Nome":^5}{"Média":^12}')

for i in range(0, len(alunos)):
    print(f'{i:<3}{alunos[i][0][0]:^10}{alunos[i][2][0]:^6}')

while True:
    r = int(input('\nQuer consultar as notas de qual aluno? [999 para encerrar]: '))
    if r == 999:
        print(f'\n\033[1;35mENCERRANDO...\033[m')
        sleep(2)
        break
    if r > len(alunos) - 1:
        print('Número inválido!')
    else:
        print(f'Notas de {alunos[r][0][0]} são {alunos[r][1]}')
