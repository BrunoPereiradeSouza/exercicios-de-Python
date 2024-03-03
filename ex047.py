from time import sleep
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
        sleep(0.5)
print('ACABOU!')
