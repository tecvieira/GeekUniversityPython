num = int(input('Informe um número inteiro ímpar: '))
if num % 2 != 0:
    for num in range(num, 0, -1):
        if num % 2 != 0:
            print(f'\033[34m-> \033[m{num}', end=' ')
else:
    print('Este número não é ímpar.')
