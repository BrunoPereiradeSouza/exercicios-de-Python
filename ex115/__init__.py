def mostramenu(lista):
    print(f'{"=-=" * 15}\n{"MENU PRINCIPAL":^45}\n{"=-=" * 15}')
    c = 1
    for i in lista:
        print(f'\033[0;33m{c}\033[m - \033[1;34m{i}\033[m')
        c += 1
    print('=-=' * 15)
    while True:
        try:
            n = int(input('\033[1;33mSua opção:\033[m '))
            if 0 < n < 4:
                return n
            else:
                print('\033[1;31mERRO! DIGITE UMA OPÇÃO VÁLIDA!')
        except:
            print('\033[1;31mERRO! DIGITE UMA OPÇÃO VÁLIDA!')


def mostrarpessoas():
    try:
        pessoas = open('pessoas.txt', 'r')
        p = pessoas.read().strip()
        l1 = p.split('\n')
        idades = open('idades.txt', 'r')
        i = idades.read()
        l2 = i.split('\n')
        print(f'{"=-=" * 15}\n{"PESSOAS CADASTRADAS":^45}\n{"=-=" * 15}')
        for i in range(0, len(l1)):
            if i != '':
                print(f'{l1[i]:<35}{l2[i]} anos')
    except:
        print('Desculpa! Não existem pesoas cadastradas :(')


def cadastrarpessoa(n, i):
    nome = str(input(n))
    if nome == '':
        nome = 'desconhecido'
    while True:
        try:
            idade = int(input(i))
            pessoa_idade = open('idades.txt', 'a')
            pessoa_idade.write(f' {str(idade)}\n')
        except:
            print('\033[0;31mIDADE INVÁLIDA! DIGITE UM VALOR INTEIRO!\033[m')
        else:
            pessoa_nome = open('pessoas.txt', 'a')
            pessoa_nome.write(f'{nome}\n')
            print('\033[0;32mPessoa cadastrada com sucesso!\033[m')
            break
