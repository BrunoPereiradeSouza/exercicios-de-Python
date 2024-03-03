n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

#UTILIZANDO A LÓGICA DE PROGRAMAÇÃO
'''maior, menor = 0, n1

if n2 <= n1 >= n3:
    maior = n1
elif n1 <= n2 >= n3:
    maior = n2
else:
    maior = n3

if n3 >= n2 <= n1:
    menor = n2
elif n2 >= n3 <= n1:
    menor = n3

print('=-=' * 20)
print(f'Maior = {maior}\nMenor = {menor}')'''

#UTILIZANDO FUNÇÕES PRONTAS (MAX E MIN)
lista = [n1, n2, n3]
print('=-=' * 20)
print(f'Maior = {max(lista)}\nMenor = {min(lista)}')
