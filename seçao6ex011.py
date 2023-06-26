n = int(input('Informe um número inteiro e positivo: '))
for n in range(0, n + 1):
    if n % 2 == 0:
        print(f'\033[33m{n}\033[m', end=' ')
    else:
        print(f'{n}', end=' ')
print('Fim...')
