def voto(ano_nasc):
    """
    -> Função que recebe a data de nascimento de uma pessoa e diz se o seu voto é
    OPCIONAL, OBRIGATÓRIO, NÃO VOTA ou INVÁLIDO.
    :param ano_nasc: Ano de Nascimento da pessoa.
    :return: Idade e a situação do VOTO.
    """
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    r = f'Com {idade} anos'
    if idade < 0:
        return f'{r}: IDADE INVÁLIDA!'
    elif 0 < idade < 16:
        return f'{r}: NÃO VOTA!'
    elif (16 <= idade < 18) or (idade > 70):
        return f'{r}: VOTO OPCIONAL!'
    elif 18 <= idade <= 70:
        return f'{r}: VOTO OBRIGATÓRIO!'


# Programa Principal
pessoa1 = voto(2000)
pessoa2 = voto(2010)
pessoa3 = voto(1930)
pessoa4 = voto(2007)
pessoa5 = voto(2030)
print(f'{pessoa1}\n{pessoa2}\n{pessoa3}\n{pessoa4}\n{pessoa5}')
help(voto)
