velocidade = int(input('Digite a velocidade: '))
if 0 <= velocidade <= 80:
    print('\033[2;32mDirija com segurança! Boa viagem!\033[m')
elif velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'\033[1;31mVOCÊ FOI MULTADO POR ULTRAPASSAR O LIMITE DA RODOVIA!!\033[m\nMulta = \033[1;31mR${multa:.2f}')
else:
    print('Velocidade inválida!')
