def volule_cilindro(r, h):
    volumecil = 3.141502 * (r ** 2) * h
    print('-=' * 20)
    return print(f'O volume do cilindro é {volumecil:.1f} unidade³')


r = float(input('Informe o raio da base do cilindro: '))
h = float(input('Valor da altura do cilindro: '))
volule_cilindro(r, h)
