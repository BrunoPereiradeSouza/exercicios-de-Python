peso = float(input('Digite o seu peso: (kg) '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
situacao = ''

if 0 < imc < 18.5:
    situacao = 'ABAIXO DO PESO'
elif 18.5 <= imc < 25:
    situacao = 'PESO IDEAL'
elif 25 <= imc < 30:
    situacao = 'SOBREPESO'
elif 30 <= imc < 40:
    situacao = 'OBESIDADE'
elif imc > 40:
    situacao = 'OBESIDADE MÓRBIDA'
else:
    situacao = None
    print('\nPeso ou altura inválidos!')
print(f'\nIMC = {imc:.2f}\nSITUAÇÃO = {situacao}.')
