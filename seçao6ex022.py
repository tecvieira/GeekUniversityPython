soma = 0
notas = 0
while True:
    nota = float(input('Informe a sua nota:'))
    if 10 <= nota <= 20:
        soma += 1
    else:
        break
print(soma)


#faltando acabar