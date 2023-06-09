vetor17 = []
n = ''
for n in range(1, 11):
    num = float(input(f'Informe {n}º número: '))
    if num < 0:
        vetor17.append(0)
    else:
        vetor17.append(num)
    n += 1
print(vetor17)
