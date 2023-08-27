def cabecalho3():
    print('-=' * 15)
    print('CONVERTE A ÁREA EM ACRE PARA M²')
    print('-=' * 15)


def converte_mt2(area):
    """Converte uma área em Acre para metros quadrado"""
    return area * 4048.58


cabecalho3()
acre = float(input('Informe área em ACRES: '))
print(f'O valor de {acre} ACRE corresponde a {converte_mt2(acre):.2f} m².')
