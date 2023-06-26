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