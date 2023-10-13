def soma_divisores(x):
    """
    Calcula a soma dos divisores de um número inteiro informado pelo usuário excluindo o número informado.
    :param x: Número informado pelo usuário
    :return: retorna a soma deste número
    """
    soma = 0
    for c in range(1, x):
        if x % c == 0:
            print(f'\033[31m {c} ', end='')
            soma += c
    return print(f'\n\033[mA soma dos divisores é: {soma}')


soma_divisores(int(input('Informe um número inteiro: ')))
