def desenhaLinha(medida):
    """
    Desenha uma linha usando sinais de '=' de forma automática banta informar o tamanho
    :param medida: informe um valor inteiro e determine o tamanho da linha
    :return: formará uma linha no tamnho desejado
    """
    print('=' * medida)


desenhaLinha(medida=int(input('Tamanho da linha: ')))
