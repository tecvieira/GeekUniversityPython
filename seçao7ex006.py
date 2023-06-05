usuario = []
n = 0
maior = 0
menor = 0
print('\033[33m=== CRIE SEU VETOR DE 10 POSIÇÕES E DESCUBRA O MAIOR E MENOR ELEMENTO ===\033[m')
while n < 10:
    num = (int(input(f'Informe o {n + 1}º número: ')))
    usuario.append(num)
    n += 1
    if n == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('-' * 60)
print(f'\033[34mForam estes os números informados: {usuario}\033[m')
print(f'\033[32mO maior número informado é: {maior}. E o menor é: {menor}\033[m')
