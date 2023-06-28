n = 0
maior = 0
soma = 0
listageral = []
num = int(input('Quantos número deseja inserir? '))
while n < num:
    numeros = int(input(f'Informe o {n + 1}º número: '))
    listageral.append(numeros)
    n += 1
    if n == 1:
        maior = numeros
    else:
        if numeros > maior:
            maior = numeros

print('==== RESULTADO ====')
print(listageral)
print(f'\033[31mO maior número informado foi {maior} este foi adicionado {listageral.count(maior)} vezez.')
