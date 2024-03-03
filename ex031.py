distancia = float(input('Digite a distância da viagem: '))
preco = 0
if 0 < distancia <= 200:
    preco = distancia * 0.5
elif distancia > 200:
    preco = distancia * 0.45
else:
    print('Distância Inválida!')
print('=-=' * 20)
print(f'Valor a ser pago = R$ {preco:.2f}')
