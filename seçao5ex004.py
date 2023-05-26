num = int(input('Informe um número inteiro: '))
if num >= 0:
    snum = num ** (1/2)
    print(f'A raiz quadrada do número {num} é igual a {snum}')
else:
    print(f'O valor informado {num}, não é permitido.')
print('Fim...')
