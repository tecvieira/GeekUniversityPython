def mede_hiponusa(a, b):
    """
    Para calcular a medida da hipotenusa:
    Elevamos as medidas dos catetos (oposto e adjacente) ao quadrado;
    Somamos os resultados;
    Extraímos a raiz quadrada.

    :param a: cateto oposto do triângulo
    :param b: cateto adjacente do triangulo
    :return: valor h = hiponusa
    """
    h = (a ** 2) + (b ** 2)
    return h ** (1 / 2)


cat_op = float(input('Informe o valor do cateto oposto: '))
cat_adj = float(input('Informe o valor do cateto adjacente: '))
print(f'A hipotenusa do triangulo cujo os catetos medem {cat_adj, cat_op} é {mede_hiponusa(cat_op, cat_adj)}')
