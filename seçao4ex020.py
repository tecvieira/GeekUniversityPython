def k_para_lb(k):
    """
    Converte o pelo em quilos para libra
    :param k: valor informado pelo usuário em quilos.
    :return: Retorna o valor convertido para libra
    """
    return print(f'{k} Quilos correspondem a {k / 0.45:.2f} Libras')


k_para_lb(float(input('Informe o peso em quilos: ')))
