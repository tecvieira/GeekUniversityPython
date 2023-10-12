soma = 0
for c in range(0, 1001):
    if c % 3 == 0 or c % 5 == 0:
        print(f'{c} ', end='')
        soma += c
print(f'\nA soma dos multiplos de 3 e 5 até 1000 é: {soma}')
