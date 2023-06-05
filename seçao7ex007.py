vetor2 = []
maior = 0
n = 0
while n < 10:
    num = int(input(f'Digite o {n + 1}º número inteiro:'))
    vetor2.append(num)
    n += 1
    if n == 0:
        maior = num
    elif num > maior:
        maior = num
print(f'Os valores sugeridos foram: {vetor2}')
print(f'O maior valor informado é {maior}, está localizado no índice {vetor2.index(maior)} da lista.')
