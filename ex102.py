def fatorial(n, show=False):
    """
    -> Função que recebe um valor e calcula o seu fatorial.
    :param n: Número para calcular a fatorial
    :param show: (opcional) Mostra ou não o cálculo realizado.
    :return: O valor da fatorial de um número n
    """
    valor = 1
    p = ''
    for i in range(n, 0, -1):
        valor *= i
        if i == 1:
            p += f'{i}'
        else:
            p += f'{i} x '
    if show:
        return f'{p} = {valor}'
    else:
        return valor


# Programa Principal
n1 = fatorial(4, True)
print(n1)
help(fatorial)
