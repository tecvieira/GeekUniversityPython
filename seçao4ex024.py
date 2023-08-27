def cabecalho2():
    print('-=' * 15)
    print('CONVERTE ÁREA DE M² PARA ACRE')
    print('-=' * 15)


def converte_acres(area):
    """Converte uma área em m² para Acres"""
    return area * 0.000247


cabecalho2()
metro = float(input('Informe área em m²: '))
print(f'O valor de {metro}m² corresponde a {converte_acres(metro):.4f} Acres.')
