<<<<<<< HEAD
def factorial(num):
    c = num
    f = 1
    while c > 0:
        f = f * c
        c = c - 1
    print(f'O fatorial de {num}! é = \033[35m {f} ')


factorial(num=int(input('\033[32mInforme um número e veja seu fatorial: \033[m')))
=======
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
>>>>>>> 4e5e536d8ae4be71855b54cadc3739dd13253755
