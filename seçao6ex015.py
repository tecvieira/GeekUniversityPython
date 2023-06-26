num = int(input('Informe um número inteiro ímpar: '))
if num % 2 != 0:
    for num in range(1, num +1):
        if num % 2 != 0:
            print(f'{num}', end=' ')
else:
    print('Este número não é ímpar.')