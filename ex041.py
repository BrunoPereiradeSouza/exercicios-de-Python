from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - ano_nasc
categoria = ''

if 0 < idade <= 9:
    categoria = '\033[1;35mMIRIM\033[m'
elif 9 < idade <= 14:
    categoria = '\033[1;32mINFANTIL\033[m'
elif 14 < idade <= 19:
    categoria = '\033[1;33mJUNIOR\033[m'
elif 19 < idade <= 25:
    categoria = '\033[1;36mSÊNIOR\033[m'
elif idade > 25:
    categoria = '\033[1;34mMASTER\033[m'
else:
    categoria = None
    idade = None
    print('\033[1;31mIdade inválida!\033[m')
print('=-=' * 20)
print(f'Idade = {idade}\nCategoria = {categoria}')
