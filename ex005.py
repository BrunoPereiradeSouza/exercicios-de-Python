# Recebe um número e imprime o seu sucessor e antecessor
num = int(input('Digite um número: '))
print(f'\033[2;32mSucessor\033[m de {num} = {num + 1}\n\033[1;31mAntecessor\033[m de {num} ='
      f' {num -1}')
