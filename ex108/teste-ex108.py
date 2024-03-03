from ex108 import moeda
p = float(input('Digite o valor: R$'))
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}\n'
      f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumento de 15% em {moeda.moeda(p)} = {moeda.moeda(moeda.aumentar(p, 15))}')
print(f'Diminuição de 20% em {moeda.moeda(p)} = {moeda.moeda(moeda.diminuir(p, 20))}')
