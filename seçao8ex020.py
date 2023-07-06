def factorial(num):
    c = num
    f = 1
    while c > 0:
        f = f * c
        c = c - 1
    print(f'O fatorial de {num}! é = \033[35m {f} ')


factorial(num=int(input('\033[32mInforme um número e veja seu fatorial: \033[m')))
