"""
Os pesos das notas n1, n2, n3, são respectivamente iguais a 2, 3, 5.
Assim independente  das notas n1 e n2 ele deve tirar no mínimo n3 >= 5
"""
n3 = 0
for i in range(0, 11):
    n3 = (5 * i) / 10
    i += 1
    if n3 < 3:
        print(f'\033[31mNo exame final se ele tirar {n3}, está reprovado\033[m')
    elif 3 <= n3 < 5:
        print(f'\033[33mNo exame final se ele tirar {n3}, está recuperação\033[m')
    elif n3 >= 5:
        print(f'\033[34mNo exame final se ele tirar no mínimo {n3}, está aprovado\033[m')
print('fim...')
