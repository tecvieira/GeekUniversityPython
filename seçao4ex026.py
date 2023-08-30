"""
def hectare(mt):
    return mt * 0.0001


terreno1 = float(input('Informe a área do terreno em m²: '))
print(f'Para {terreno1} temos o equivalente a {hectare(terreno1)} hectare.')

Segue abaixo outra forma de resolver usando expressões lambdas

"""

hect = lambda mt: 0.0001 * mt

print(hect(float(input('Informe área do terreno em m²: '))))
