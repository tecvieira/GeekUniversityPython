def somaInteiros(i, f):
    """
    A função soma os números inteiros existentes entre o início e fim da contagem.
    :param i: Número informado par início da contagem.
    :param f: Número final da contagem.
    :return: Retorna o valor somado dos numeros no intervalo entre inicio e fim da contagem.
    """
    smi = 0
    inicio = i
    for i in range(i + 1, f):
        smi += i
        i += 1
    print(f'A soma dos números existentes entre {inicio} e {f} é igual a {smi}.')


somaInteiros(i=int(input('Número inicial: ')), f=int(input('Número final da contagem: ')))
