def converte_radianos(angulo):
    """
    Faz a conversão do ângulo em gráus, par radianos.
    :param angulo: valor do ângulo em gráus
    :return: retorna o valor em radianos
    """
    radiano = (angulo * 3.14) / 180
    return radiano


print(converte_radianos(float(input('Informe o ângulo em gráus: '))))
