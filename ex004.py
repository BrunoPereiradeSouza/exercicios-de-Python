# Recebe uma entrada do usuário e analisa as informações sobre essa entrada
algo = input('Digite algo: ')

print(f'''
O tipo primitivo desse valor é {type(algo)}
Só tem espaços? {algo.isspace()}
É um número? {algo.isnumeric()}
É alfabético? {algo.isalpha()}
É alfanumérico? {algo.isalnum()}
Está em maiúsculas? {algo.isupper()}
EStá em minúsculas? {algo.islower()}
Está capitalizada? {algo.istitle()}
''')
