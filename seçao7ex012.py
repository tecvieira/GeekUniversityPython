from time import sleep

vetor12 = []
maior = 0
menor = 0
soma = 0
n = 0
print('=== Iniciando análise dos números ===')
while n < 5:
    num = int(input(f'Informe o {n + 1}º número inteiro: '))
    vetor12.append(num)
    n += 1
    if n == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    soma = soma + num
media = soma / n
print()
print('\033[34m=== ANALISANDO OS DADOS ===')
sleep(1.5)
print('- =' * 20)
print(f'Números informados: {vetor12}')
print(f'A soma dos números lidos: {soma}')
print(f'A média dos {n} números são: {media}')
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
print('- =' * 20)
