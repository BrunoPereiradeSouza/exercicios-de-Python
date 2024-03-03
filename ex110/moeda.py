from ex108.moeda import moeda


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


def resumo(num, a, r):
    print(f'{"-" * 50}\n{"RESUMO DO VALOR":^50}\n{"-" * 50}')
    print(f'''
Preço analisado: \t\t\t\t\t{moeda(num)}
Dobro de {moeda(num)}: \t\t\t\t\t{moeda(num * 2)}
Metade de {moeda(num)}: \t\t\t\t{moeda(num / 2)}
{a}% de aumento em {moeda(num)}: \t\t{moeda(num + (num * a / 100))}
{r}% de redução em {moeda(num)}: \t\t{moeda(num - (num * r / 100))}
{"-" * 50}
''')
