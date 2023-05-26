print('===== PAR ou ÍMPAR =====')
num = int(input('Digite um número inteiro: '))
saida = num % 2
if saida == 0:
    print(f'O número {num} é PAR.')
elif saida == 1:
    print(f'O número {num} é ÍMPAR.')

