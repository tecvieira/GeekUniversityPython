def triangulo_lateral(n):
    """
    Forma um triângulo lateral de acordo com tamanho solicitado pelo usuário
    :param n: valor informado pelo usuário
    :return: triângulo lateral formado por "*"
    """
    for i in range(0, n + 1, 1):
        print("*" * i)
    for i in range(n -1, 0, -1):
        print("*" * i)


print(triangulo_lateral(n=int(input('Digite um valor: '))))
