from math import sqrt
def mostra_hipotenusa(a, b):
    hipotenusa = sqrt((a ** 2) + (b ** 2))
    return print(f'O valor da hipotenusa é {hipotenusa:.1f}')

a = float(input('Comprimento do cateto oposto:'))
b = float(input('Comprimento do cateto adjacente: '))
mostra_hipotenusa(a, b)