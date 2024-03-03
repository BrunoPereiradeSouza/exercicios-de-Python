n1 = int(input('1° valor: '))
n2 = int(input('2° valor: '))
print('')
if n1 > n2:
    print('O \033[1;32mprimeiro\033[m é maior!')
elif n2 > n1:
    print('O \033[1;31msegundo\033[m é maior!')
else:
    print('Os dois valores são \033[1;33mIGUAIS!\033[m')
