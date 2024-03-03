def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')


def aumentar(num, porcent):
    return num + (num * porcent / 100)


def diminuir(num, porcent):
    return num - (num * porcent / 100)


def dobro(num):
    return num * 2


def metade(num):
    return num / 2
