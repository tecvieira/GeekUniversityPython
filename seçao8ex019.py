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