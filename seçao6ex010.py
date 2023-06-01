n = 0
soma = 0
while n < 51:
    if n % 2 == 0:
        print(f'{n}', end=' ')
        soma += n
    n += 1

print(f'\nA soma dos primeiros pares de 0 até 50 é {soma}')
