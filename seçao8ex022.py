def faz_triangulo(n):
    for i in range(0, n+1, 1):
        print('!' * i)
    for i in range(n -1, 0, -1):
        print('!' * i)


faz_triangulo(n=int(input('Informe um número inteiro: ')))