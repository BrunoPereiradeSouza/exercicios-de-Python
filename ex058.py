from random import randint
print('\033[3;32mJOGO DA ADIVINHAÇÃO!!\033[m')
print('\nOlá! Eu sou o \033[1;33mPython\033[m e acabei de pensar em um número inteiro '
      'entre 0 e 10.\n'
      'Será que você é capaz de adivinhar?\n')
num_pc = randint(0, 10)
tentativas = 0
while True:
    tentativas += 1
    palpite = int(input('Qual o seu palpite? '))
    if num_pc == palpite:
        print(f'\n\033[1;32mVocê acertou!\033[m Eu pensei no número {num_pc}.')
        break
    else:
        if num_pc > palpite:
            print('\n\033[1;31mMaior!! Tente novamente:\033[m\n')
        elif num_pc < palpite:
            print('\n\033[1;33mMenor!! Tente novamente:\033[m\n')
print(f'\nVocê acertou em {tentativas} tentativas.')
