import ex115
from time import sleep


while True:
    n = ex115.mostramenu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do Sitema'])
    if n == 1:
        ex115.mostrarpessoas()
        sleep(2)
    elif n == 2:
        ex115.cadastrarpessoa('Nome: ', 'Idade: ')
        sleep(1)
    elif n == 3:
        print('\n\033[1;35mENCERRANDO...\033[m')
        sleep(2)
        break
