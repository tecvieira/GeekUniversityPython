media = 0
soma = 0
boletim = []
for n in range(1, 5):
    nota = float(input(f'Informe a {n}ª nota: '))
    boletim.append(nota)
    soma += nota
media = soma / 4
print(f'A média das notas {boletim} é {media:.2f}.')


