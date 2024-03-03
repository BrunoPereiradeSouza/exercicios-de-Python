from datetime import date
print('\033[1;34mCONSULTE SE UM ANO É BISSEXTO OU NÃO!\033[m')
print('=-=' * 20)
ano = int(input('Digite um ano para saber se ele é bissexto. (0 para '
                'consultar o ano atual): '))
ano_atual = date.today().year
if ano == 0:
    ano = ano_atual
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é \033[1;32mBISSETO!\033[m')
else:
    print(f'{ano} Não é \033[1;31mBISSEXTO!\033[m')
