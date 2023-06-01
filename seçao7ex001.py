a = list()
a.extend([1, 0, 5, -2, -5, 7])
print(f'Os valores atribuidos ao vetor são: {a}')
soma = a[0] + a[1] + a[5]
print(f'A soma dos elementos nas posições 0, 1 e 5 é: {soma}')
a[4] = 100
print(f'O elemento na posição 4 foi modificado para {a}')
for a in (a):
    print(a)

