<<<<<<< HEAD
def maior_primo(num):
    primos = []
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0:
            print('\033[33m', end='')
            primos.append(c)
            tot += 1
        else:
            print('\033[31m', end=' ')
        print(f'{c}', end=' ')
    print(f'\n\033[mO número {num} foi divisível por {tot} vezes. ')
    print(primos)
    if tot == 2:
        print('É primo')
    else:
        print('Não é primo')


maior_primo(10)

#falta gerar o maior fator primo atividade pendente
=======
def acha_primo(num):
    tot = 0
    primos = []
    for c in range(1, num + 1):
        if num % c == 0:
            print('\033[33m', end=' ')
            tot += 1
        else:
            print('\033[31m', end=' ')
    primos.append(tot)
    print(primos)
    print(f'\033[m O número {num} foi dividido por {tot} vezes ')


acha_primo(num=int(input('Digite um valor: ')))
>>>>>>> 2a07b611dc0b2e6b78efba21da244c5fbc5f90ca
