print('\033[33mVerifique se o número é divisível por 3 ou 5. \033[m')
numero = float(input('Informe um número: '))
if numero % 3 == 0 and numero % 5 == 0:
    print(f'\033[34mO número {numero} é divisível por 3 e 5.')
else:
    print(f'\033[31mEste número {numero} não é divisível por 3 e 5')
