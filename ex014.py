print('\033[5;35mConversor de Temperatura\033[m')
print('=-=' * 20)
celsius = float(input('Digite uma temperatura em graus C°: '))
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273
print(f'{celsius}°C = {fahrenheit}°F\n{celsius}°C = {kelvin}K')
