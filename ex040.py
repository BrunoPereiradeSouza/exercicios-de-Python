print('\033[4;34mCALCULADOR DE MÉDIA\033[m\n')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print()
media = (n1 + n2) / 2

if 0 <= media < 5:
    print(f'Média = {media}\nSituação = \033[1;31mREPROVADO!\033[m')
elif 5 <= media < 7:
    print(f'Média = {media}\nSituação = \033[1;33mRECUPERAÇÃO!\033[m')
elif media >= 7:
    print(f'Média = {media}\nSituação = \033[1;32mAPROVADO!\033[m')
else:
    print('\033[1;31mMédia inválida!\033[m')
