num = int(input('Informe um número: '))
if num >= 0:
    nsaida = num ** (1/2)
    print(f'A raiz quadrada do número informado {num} é {nsaida}')
if num < 0:
    print('Número inválido.')
print('Fim...')