print(f'{"-" * 50}\n{"LISTAGEM DE PREÇOS":^50}\n{"-" * 50}\n')

itens = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for item in itens:
    if itens.index(item) % 2 == 0:
        print(f'{item}{"." * (40 - len(item))}R$ ', end='')
    else:
        print(f'{item:>7.2f}')
