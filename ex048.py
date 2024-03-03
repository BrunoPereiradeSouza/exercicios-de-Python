soma = 0
num = 0
for i in range(1, 501):
    if (i % 2 != 0) and (i % 3 == 0):
        soma += i
        num += 1
print(f'A soma dos {num} números solicitados é {soma}')
