vetor1 = []
n = 1
contPar = 0
while n <= 10:
    num = (int(input(f'Informe 0 {n}º número: ')))
    n += 1
    if  num % 2 == 0:
        vetor1.append(num)
        contPar += 1
print(f'Encontramos {contPar} números pares, que são: {vetor1}')
