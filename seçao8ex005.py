def volume_esfera(r):
    if r > 0:
        vesfera = (4/3 * 3.14) * (r ** 3)
        return print(f'O volume da esfera é {vesfera:.2f}cm³')
    else:
        return print('Erro! escolha um valor positivo.')


volume_esfera(float(input("tamanho do Raio em centímetros: ")))
