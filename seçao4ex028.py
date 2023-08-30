soma = 0
numeros = []
for n in range(1, 4):
    num = int(input(f'Informe o {n}º valor: '))
    numeros.append(num)
    soma += (num ** 2)

print(f'A soma dos números {numeros} ao quadrado é {soma}')
