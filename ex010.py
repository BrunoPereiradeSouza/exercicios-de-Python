reais = float(input('Quantos reais você tem? R$'))
euro = reais / 5.35
dolar = reais / 4.92
print(f'R$ {reais:.2f} = US${dolar:.2f} doláres.\nR$ {reais:.2f} = {euro:.2f} euros.')
