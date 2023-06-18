from math import sqrt, floor


def testaQuadradoNumero(numero):
    if numero < 0:
        return False
    else:
        raiz = sqrt(numero)
        print(raiz)
        while numero > 0:
            if raiz ** 2 == floor(numero):
                return True
            else:
                return False




print(testaQuadradoNumero(int(input('Informe um número, veja se ele tem um quadrado perfeito: '))))
