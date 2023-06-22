def mede_consumo(km, lts):
    """
    Função para verificar consumo do veículo e o custo benefício na condução.
    :param km: Quilometragem percorrida após completar o tanque antes de analizar.
    :param lts: Quantidade de combustível completada após percorrer distância informada.
    :return: Quantidade de quilometros percorrido com 1 litro de combustível.
    by TecVander.
    """
    consumo = 0
    consumo = km / lts
    if consumo < 8:
        print(f'Consumo elevado de {consumo:.3f} Km/l. Venda seu carro!!!')
    elif 8 <= consumo <= 12:
        print(f'Vaículo econômico, está fazendo {consumo:.3f} km/l.')
    elif consumo > 12:
        print(f'Seu veículo é muito econômico, está fazendo {consumo:.3f}. Parabéns!!!')

print('=-'*40)
mede_consumo(km = float(input('Quilometragem percorrida: ')),lts = float(input('Quantidade de combustível: ')))
