sexo = str(input('digite M para masculino ou  F para feminino. ')).upper().strip()
altura = float(input('Informe sua altura: '))
if sexo == 'M':
    pesoIdeal = (72.7 * altura) - 44.7
    print(f'O peso ideal para você é: {pesoIdeal:.2f} ')
elif sexo == 'F':
    pesoIdeal = (62.1 * altura) - 44.7
    print(f'O peso ideal para você é: {pesoIdeal:.2f}')
else:
    if sexo != "MF":
        print('Sexo informado de forma indevida.')

