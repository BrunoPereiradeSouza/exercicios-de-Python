print('\033[1;35m==== INFORMAÇÕES SOBRE A TABELA DO BRASILEIRÃO 2023 ====\033[m\n')
times = ('Palmeiras', 'Grêmio', 'Atlético MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense',
         'Athlético PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians',
         'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América MG')

print('\033[1;36mCLASSIFICAÇÃO:\033[m\n')
for time in times:
    print(f'{times.index(time) + 1}° - {time}')
print(f'\n{"=-=" * 20}')

print('\n\033[1;32mG-4 DA TABELA:\033[m\n')

for time in times[:4]:
    print(f'{times.index(time) + 1}° - {time}')
print(f'\n{"=-=" * 20}')
print('\n\033[1;31mZ-4 DA TABELA:\033[m\n')
for time in times[16:]:
    print(f'{times.index(time) + 1}° - {time}')
print(f'\n{"=-=" * 20}\n')
print(f'O \033[3;31mFlamengo\033[m está na {times.index("Flamengo") + 1}° posição.')
