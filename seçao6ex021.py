num = int(input('Informe um número inteiro de valor baixo: '))
num2 = int(input('Informe outro número com valor maior: '))
soma = 0
mult = 1
for numero in range(num, num2+1):
    print(f'{numero}', end=' ')
    if numero % 2 == 0:
        soma += numero
    elif numero % 2 != 0:
        mult *= numero
print(f'\nA soma dos números pares do intervalo entre {num} e {num2} = {soma}')
print(f'\nA multiplicaçãp dos números ímpares do intervalo entre {num} e {num2} = {mult}')


