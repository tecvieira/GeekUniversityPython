num = int(input('Informe um número inteiro positivo: '))
somanum = 0
if num >= 0:
    for num in range(0, num + 1):
        if num == 0:
            print(f'{num}', end=' ')
        else:
            print(f'+ {num} ', end=' ')
        somanum += num
    print(f'= {somanum}')
else:
    print('Este não é um número positivo.')

