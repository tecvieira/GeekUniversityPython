num = int(input('Digite um número inteiro e veja a soma de seus algarismos: '))
soma = 0
print(f'O número informado é: {num}')
while num > 0:
    soma += num % 10 # vai somar os restos de cada etapa
    print(soma)    # esta linha é apenas para vizualizar não é necessária
    num = int(num / 10) #faz num ser dividido por 10 em cada etapa
    print(num) # esta linha é apenas para vizualizar não é necessária
print(f'A soma dos seus algarismos, é igual a: {soma}')
