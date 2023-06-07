vetor14 = []
repetidos = set()
valores = []
print('\033[32m=== Informe 10 valores inteiros ===\033[m')
for n in range(0, 10):
    num = int(input(f'Informe o {n + 1}º número: '))
    vetor14.append(num)
    n += 1
for dado in vetor14:
    if dado not in valores:
        valores.append(dado)
    else:
        repetidos.add(dado)
print(f'\033[32mO valores informados são: {vetor14}')
print(f'Os valores ao lado se repetiram na sugetão: {repetidos}')
