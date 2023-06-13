num = int(input('Digite um número inteiro e veja a soma de seus algarismos: '))
soma = 0
print(f'O número informado é: {num}')
while num > 0:
    soma += num % 10
    num = int(num / 10)
print(f'A soma dos seus algarismos, é igual a: {soma}')
