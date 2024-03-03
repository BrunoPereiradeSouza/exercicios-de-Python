distancia = float(input('Digite um distância em metros: '))
print('=-=' * 20)
print(f'''
km = {distancia / 1000}
hm = {distancia / 100}
dam = {distancia / 10}
dm = {distancia * 10}
cm = {distancia * 100}
mm = {distancia * 1000}
''')
