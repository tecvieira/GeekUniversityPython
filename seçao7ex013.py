vetor13 = []
n = 0
maior = menor = 0
soma = 0
while n < 5:
    num = int(input(f'Digite o {n + 1}º número: '))
    vetor13.append(num)
    n += 1
    if n == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(vetor13)
print(f'O maior número é {maior} e está na posição {vetor13.index(maior)}')
print(f'O menor valor é {menor} está na posição {vetor13.index(menor)}')

