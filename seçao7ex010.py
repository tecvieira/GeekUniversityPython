turma = []
n = 0
notas = 0
media = 0
soma = 0
while n < 15:
    notas = float(input(f'Informe a nota do {n + 1} aluno. '))
    n += 1
    soma += notas
media = soma / 5
print(f'Total de pontos da turma, {n} alunos: {soma}')
print(f'A média da turma é:{media:.2f}')
