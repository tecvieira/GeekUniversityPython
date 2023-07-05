def factorial(n):
    c = n
    f = 1
    while c > 0:
        print(f'{c}', end=' ')
        print('x' if c > 1 else '=', end=' ')
        f = f * c
        c -= 1
    print(f)


factorial(n=int(input('Digite um numero Inteiro: ')))