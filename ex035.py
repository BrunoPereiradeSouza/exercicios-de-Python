print('=-=' * 10)
print('\033[1;35mANALISANDO TRIÂNGULOS!\033[m')
print('=-=' * 10)

l1 = float(input('Medida do 1° lado: '))
l2 = float(input('Medida do 2° lado: '))
l3 = float(input('Medida do 3° lado: '))

if (l1 < (l2 + l3)) and (l2 < (l1 + l3)) and (l3 < (l1 + l2)):
    print('Os lados informados \033[32mPODEM\033[m formar um triângulo!')
else:
    print('Os lados informados \033[31mNÃO PODEM\033[m formar um triângulo!')
