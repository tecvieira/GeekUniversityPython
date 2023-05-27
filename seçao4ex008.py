print('==== Convertendo Temperatura Kelvin x Celcius ====')
print('=' * 50)
tempI = float(input('Informe o valor da temperatura: '))
print("""
INFORME A ESCALA DO VALOR INFORMADO:

         [1] Em Celcius
         [2] Em Kelvin
""")
escala = int(input('Qual a escala? '))
if escala == 1:
    tempK = tempI + 273.15
    print(f'A temperatura de {tempI}ºC corresponde a {tempK}ºK')
elif escala == 2:
    tempC = tempI - 273.15
    print(f'A temperatura de {tempI}ºK corresponde a {tempC}ºC')
else:
    print('\033[31mERRO! O valor digitado não válido.\033[m')
