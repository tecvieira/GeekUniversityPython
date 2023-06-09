vetor18 = []
n = 0
num = ''
multiplos = []
soma = 0
print('\033[33m=== ESCOLHA 10 NÚMEROS ===\033[m')
while n < 10:
    num = float(input(f'Digite o {n + 1}º número: '))
    vetor18.append(num)
    n += 1
print()

print(vetor18)
x = int(input('\033[33mEscolha um número, verifique se há multiplos na lista: \033[m'))
for valor in vetor18:
    if valor % x == 0:
        multiplos.append(valor)
        soma += 1
print('===' * 15)
print(f'Os multiplos de {x} na lista acima sao: {multiplos}')
print(f'Foram encontrados {soma} múltiplos.')
print('===\033[m' * 15)
print('\033[31mByTecVander')
