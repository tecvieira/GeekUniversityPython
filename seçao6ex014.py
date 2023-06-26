num = int(input('Informe um número inteiro par: '))
if num % 2 == 0:
    for num in range(num, -1, -1):
        if num % 2 == 0:
            print(f'\033[31m->\033[m {num}', end=' ')
else:
    print('Este número não é par.')