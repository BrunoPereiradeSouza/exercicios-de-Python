nome = str(input('Digite o seu nome completo: ')).lower().strip()
lista = nome.split()
condicao = False
if 'silva' in lista:
    condicao = True
    print('=-=' * 20)
print(f'Seu nome tem Silva? {condicao}')
