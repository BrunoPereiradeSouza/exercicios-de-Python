nome = str(input('Digite o seu nome completo: ')).strip()
lista = nome.split()
print('=-=' * 20)
print(f'Muito prazer em te conhecer!\n\nSeu primeiro nome é {lista[0]}\nSeu último nome é {lista[-1]}')
