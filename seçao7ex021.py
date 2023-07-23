primeiro = []
segundo = []
terceiro = []
for numeros in range(1,4):
    dados1 = int(input(f'Digite o {numeros} número:  '))
    primeiro.append(dados1)
    numeros += 1
for dados in range(1, 4):
    dados2 = int(input(f'Digite o {dados} número:  '))
    segundo.append(dados2)
    dados += 1
for primeiro, segundo in zip(primeiro, segundo):
        terceiro.append(primeiro - segundo)
print(primeiro)
print(segundo)
#print(terceiro)
