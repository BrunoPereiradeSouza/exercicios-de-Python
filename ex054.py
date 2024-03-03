from datetime import date
maior, menor = 0, 0
ano_atual = date.today().year
for i in range(1, 8):
    ano = int(input(f'Em que ano a {i}° pessoa nasceu: '))
    if ano_atual - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'\nmaiores de idade = {maior}\nMenores de idade = {menor}')
