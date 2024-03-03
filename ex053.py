frase = str(input('Digite uma frase: ')).upper().strip()
print()
nova_frase = ''.join(frase.split())
inverso_frase = nova_frase[::-1]

if nova_frase == inverso_frase:
    print(f'{nova_frase} ao inverso fica {inverso_frase}, \nLogo '
          f'\033[1;32mTEMOS UM PALÍNDROMO!\033[m')
else:
    print(f'{nova_frase} ao inverso fica {inverso_frase}, \nLogo '
          f'\033[1;31mNÃO TEMOS UM PALÍNDROMO!\033[m')
