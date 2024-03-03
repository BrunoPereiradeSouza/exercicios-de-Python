cidade = str(input("Em qual cidade você nasceu? ")).lower().strip()
lista = cidade.split()
condicao = False
if 'santo' in lista[0]:
    condicao = True
print('=-=' * 20)
print(condicao)
