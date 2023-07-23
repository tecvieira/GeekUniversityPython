def converte_centimetros(p):
    """
    Converte a medida em polegada para centímetros.
    :param p: Medida informada pelo usuário em polegadas
    :return: Valor da medida convertida em centímetros.
    """
    c = p * 2.54
    return c


print(converte_centimetros(float(input('Informe a medida em polegadas: '))))
