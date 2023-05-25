from time import sleep
print('=== Conversão de temperatura ===')
print('=' * 32)
resp = ' '
while resp not in 'C' or 'F':
    temp = float(input('Informe o valor da temperatura:'))
    print('=' * 32)
    print("""
    INFORME A ESCALA DESTA TEMPERATURA:
    [C] Para Celsius
    [F] Fahrenheit
    """)
    print('=' * 32)
    resp = str(input('Informe a escala:')).strip().upper()
    if resp == 'C':
        tempf = (temp * (9.0 / 5.0)) + 32.0
        print(f'\033[32mA temperatura {temp}ºC, convertida para Fahrenheit  é {tempf:.1f}ºF\033[m')
    elif resp == 'F':
        tempC = (5 * (temp - 32)) / 9.0
        print(f'\033[34mA temperatura de {temp}ºF, convertida para Celsius  é {tempC:.1f}ºC\033[m')
    else:
        print('\033[31mERRO! opção inválida.\033[m')
    pergunta = str(input('Deseja continuar? [S/N]')).strip().upper()
    while pergunta not in 'SN':
        print('\033[31mERRO! opção inválida.\033[m')
        pergunta = str(input('Deseja continuar? [S/N]')).strip().upper()
    if pergunta == 'N':
        break
print('FINALIZANDO....')
sleep(2.0)
print('Obrigado volte sempre!!!')
