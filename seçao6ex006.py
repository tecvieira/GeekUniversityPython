from time import sleep
soma = 0
n = 1
while n < 11:
    num = int(input(f'Digite o {n}º número: '))
    n += 1
    soma += num
media = soma / 10
print('Calculando....')
sleep(2.0)
print(f'A soma dos 10 números é: {soma}, E sua média é: {media}')
print('Acabou...')
