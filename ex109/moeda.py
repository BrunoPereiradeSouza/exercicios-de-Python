def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')


def aumentar(num, porcent, f=False):
    n = num + (num * porcent / 100)
    if f:
        return moeda(n)
    else:
        return n


def diminuir(num, porcent, f=False):
    n = num - (num * porcent / 100)
    if f:
        return moeda(n)
    else:
        return n


def dobro(num, f=False):
    d = num * 2
    if f:
        return moeda(d)
    else:
        return d


def metade(num, f=False):
    m = num / 2
    if f:
        return moeda(m)
    else:
        return m
