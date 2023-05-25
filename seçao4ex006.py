print('=== Conversão de temperatura ===')
temp = float(input('Informe o valor da temperatura:'))
escala = str(input('Informe a escala lida: digite C ou F :')).strip().upper()
print('=' * 50)
if escala in 'C':
    tempF = (temp * (9.0 / 5.0)) + 32.0
    print(f'A temperatura {temp}ºC, convertida para Fahrenheit  é {tempF:.2f}ºF')
if escala in 'F':
    tempC = (5 * (temp - 32)) / 9.0
    print(f'A temperatura de {temp}ºF, convertida para Celsius  é {tempC:.2f}ºC')
