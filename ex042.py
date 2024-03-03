l1 = float(input('1° lado do triângulo: '))
l2 = float(input('2° lado de triângulo: '))
l3 = float(input('3° lado do triângulo: '))

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print('\nOs lados informados \033[1;32mPODEM\033[m formar um triângulo', end=' ')
    if l1 == l2 == l3:
        print('\033[1;33mEQUILÁTERO!\033[m')
    elif (l1 == l2 != l3) or (l1 == l3 != l2) or (l2 == l3 != l1):
        print('\033[1;34mISÓSCELES!\033[m')
    else:
        print('\033[1;35mESCALENO!\033[m')
else:
    print('Os lados informados \033[1;31mNÃO PODEM\033[m formar um triângulo')
