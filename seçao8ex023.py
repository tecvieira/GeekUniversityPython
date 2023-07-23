def triangulo(n):
    x = 0
    for i in range(1, n + 1):
        x = i + (x * 10)
        print(f'{x:.>{n}}')

triangulo(5)

#nao esta correto