from time import sleep
frase = str(input('Digite um frase: ')).strip().lower()
print('\033[1;31mAnalisando a frase digitada...\033[m\n')
sleep(2)
print(f'A letra "A" aparece {frase.count("a")} vezes na frase.')
print(f'Posição do 1° "A" = {frase.find("a") + 1}\nPosição do último "A" = {frase.rfind("a") + 1}')
