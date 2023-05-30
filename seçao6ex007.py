n = 0
num = 0
soma = 0
while n < 10:
    num = int(input(f'Digite o {n + 1}º número: '))
    n = n + 1
    if num >= 0:
        soma = soma + num
    else:
        print(f'\033[31mNúmero {num} negativo valor será descartado.\033[m')
media = soma / 10
print(f'Foram somados {n} números cujo total = {soma} e sua média {media}')
