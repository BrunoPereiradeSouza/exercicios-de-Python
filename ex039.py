from datetime import date
ano_atual = date.today().year
print('\033[1;36mALISTAMENTO MILITAR!\033[m\n')
ano_nasc = int(input('Em que ano você nasceu? '))
print('=-=' * 20)
idade = ano_atual - ano_nasc
print(f'Você tem \033[3;32m{idade}\033[m anos em {ano_atual}.')
if 0 <= idade < 18:
    restante = 18 - idade
    print(f'Ainda falta(m) {restante} ano(s) para você se alistar! '
          f'Seu alistamento será em {ano_atual + restante}.')
elif idade > 18:
    restante = idade - 18
    print(f'Você deveria ter se alistado há {restante} ano(s) atrás! '
          f'Seu alistamento foi em {ano_atual - restante}.')
elif idade == 18:
    print('Você deve se alistar ainda esse ano!!')
else:
    print('idade inválida!')
