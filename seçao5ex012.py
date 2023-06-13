import math
calc = 0
print('=== Calculando o LOGARÍTMO DE UM NÚMERO ===')
num = int(input('Informe o número inteiro: '))
base = int(input('Qual a base do logarítmo: '))
if num <= 0 or base == 1 or base <= 0:
    if num <= 0:
        print(f'Este número: {num} não permite calcular o logarítmo.')
    if base == 1:
        print(f'O número {base} não satifaz a condição exigida como base. ')
    if base <= 0:
        print(f'Este número {base} não é permitido como base.')
else:
    calc = math.log(num, base)
    print(f'O logarítmo de {num} na base {base} é {calc:.1f}')
print()
print('Fim....')
