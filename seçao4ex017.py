def converte_polegadas(c):
    """
    Faz  conversão de uma medida em centímetros para polegada.
    :param c: valor da medida em centímetros
    :return: retorna valor convertido em polegadas.
    """
    p = c / 2.54
    return p


print(converte_polegadas(float(input('Informe a medida em centímetros: '))))
