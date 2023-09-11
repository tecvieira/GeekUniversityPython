def volume_cilindro(r, h):
    return 3.141502 * (r ** 2) * h

raio = float(input('Informe o raio da base: '))
altura = float(input('Informe altura do cilindro: '))
print(f'O volume do cilindro informado é {volume_cilindro(raio, altura):.2f} unidade cúbica.')
