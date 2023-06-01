from time import sleep
print('==== CONVERTENDO TEMPERATURA DE CELCIUS PARA KELVIM ====')
tempC = float(input('             INFORME A TEMPERATURA EM ºC :'))
print('\033[34m-=\033[m' * 30)
print('Convertendo....')
sleep(2.0)
tempK = tempC + 273.15
print('\033[34m-=\033[m' * 30)
print(f'\033[34mTemperatura {tempC:.2f}ºC   => \033[m \033[31mTemperatura {tempK:.2f}ºK\033[m' )
print('\033[34m-=\033[m' * 30)
print('ByTecVander v.1.0')