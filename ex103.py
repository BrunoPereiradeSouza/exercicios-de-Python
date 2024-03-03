def ficha(nome='<desconhecido>', n=0):
    return f'O jogador {nome} fez {n} gol(s) no campeonato.'


# Programa Principal
jogador = str(input('Nome: ')).strip()
gols = str(input('N° de gols: ')).strip()
if gols.isnumeric():
    int(gols)
else:
    gols = 0
if jogador == '':
    j1 = ficha(n=gols)
else:
    j1 = ficha(jogador, gols)
print(j1)
