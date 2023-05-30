n = 0
num = 0
maior = 0
menor = 0
while n < 10:
    num = int(input(f'Informe o {n + 1}º número: '))
    n += 1
    if n == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'O maior valor informado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')
