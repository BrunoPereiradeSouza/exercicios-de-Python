soma = 0
num = 0
for i in range(1, 7):
    n = int(input('Digite um valor inteiro: '))
    if n % 2 == 0:
        soma += n
        num += 1
print(f'\nSoma do(s) {num} número(s) Par(es) = {soma}')
