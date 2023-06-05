vetor11 = []
n = 0
somaNeg = 0
somaPos = 0
while n < 10:
    num = float(input(f'Informe o {n + 1}º número real: '))
    n += 1
    if num < 0:
        vetor11.append(num)
        somaNeg += 1
    elif num >= 0:
        vetor11.append(num)
        somaPos += num
print('-=' * 40)
print(f'\033[32mNúmeros informados: {vetor11}\033[m')
print(f'Foram encontrados {somaNeg} números negativos.')
print(f'A soma dos números positivos é: {somaPos:.2f}')
print('-=' * 40)
