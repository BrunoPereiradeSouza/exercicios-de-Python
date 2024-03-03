def notas(* num, sit=False):
    """
    < - Função que análise uma ou n notas de um aluno, retorna a quantidade de notas
    informadas, a maior, a menor, a média e a situação do aluno.
    :param num: números informados (1 ou n)
    :param sit: (opcional) Exibe ou não a situação do aluno.
    :return: Um dicionário com todas as informações do aluno.
    """
    total, maior, menor, media, situacao, soma_notas = 0, 0, 0, 0, '', 0
    for n in num:
        total += 1
        soma_notas += n
        if num.index(n) == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
    media = soma_notas / total
    if media >= 9:
        situacao = 'ÓTIMA'
    elif 6 <= media < 9:
        situacao = 'BOA'
    elif 3 <= media < 6:
        situacao = 'RUIM'
    elif 0 <= media < 3:
        situacao = 'PÉSSIMA'
    else:
        situacao = 'INVÁLIDA'
    info = {'total': total, 'maior': maior, 'menor': menor, f'media': f'{media:.2f}'}
    if sit:
        info['situação'] = situacao
    return info


# Programa Principal
resp = notas(8, 9, 3, 6, 7.9, sit=True)
help(notas)
