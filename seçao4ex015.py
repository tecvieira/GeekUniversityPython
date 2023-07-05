def converte_graus(angulo):
    """
    Converte o ângulo em radianos para gráus
    :param angulo: valor do ângulo e radiano
    :return: o valor convertido em gráus
    """
    graus = (angulo * 180) / 3.14
    return graus


print(converte_graus(float(input('Informe o ângulo em radianos: '))))
