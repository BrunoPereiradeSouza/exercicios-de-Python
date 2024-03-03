expressao = str(input('Digite uma expressão: ')).strip()
lista = []

for i in expressao:
    if i == '(':
        lista.append(i)
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão é \033[1;32mVÁLIDA!\033[m')
else:
    print('A expressão \033[1;31mNÃO É VÁLIDA!\033[m')
