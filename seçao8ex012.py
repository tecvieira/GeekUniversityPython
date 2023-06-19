def soma_algarismo(n):
    soma = 0
    while n > 0:
        soma += n % 10
        n = int(n / 10)
    return print(f'A soma dos algarismos do número informado é igual a {soma}')


soma_algarismo(n=int(input('Informe um número inteiro: ')))
