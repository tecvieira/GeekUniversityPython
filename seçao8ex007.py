def mostra_fahrenheit(tempC):
    tempf = (tempC * (9/5)) + 32
    return print(f'A temperatua convertida é {tempf} ºF.')


tempc = float(input('Informe a temperatura em ºC e veja em ºF: '))
mostra_fahrenheit(tempc)
