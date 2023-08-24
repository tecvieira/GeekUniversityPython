"""
def multiMatriz(n):
    matriz = []
    for coluna in range(n):
        for linha in range(n):
            matriz.append(linha * coluna)
    return print(matriz) # está saindo uma lista única com os valores certos


multiMatriz(4)

# Gerando uma matriz com o produto da linha por colunas
# Usando list comprehension
print([[i * j for i in range(0, 4)] for j in range(0, 4)])
"""

print([[linha * coluna for linha in range(4)] for coluna in range(4)])


