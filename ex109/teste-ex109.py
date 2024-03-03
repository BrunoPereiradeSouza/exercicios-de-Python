from ex109 import moeda

n = float(input('Digite um valor: R$'))
print(f'Dobro de {moeda.moeda(n)} = {moeda.dobro(n, True)}\nMetade de {moeda.moeda(n)} = '
      f'{moeda.metade(n, True)}')
print(f'Aumento de 15% em {moeda.moeda(n)} = {moeda.aumentar(n, 15, True)}')
print(f'Diminuição de 20% em {moeda.moeda(n)} = {moeda.diminuir(n, 20, True)}')
