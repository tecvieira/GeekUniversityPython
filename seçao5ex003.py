num = float(input('Informe o primeiro número: '))
if num >= 0:
    nsaida = num ** (1/2)
    print(f'\033[32mO número informado {num} é positivo, a raiz quadrada dele é: {nsaida}\033[m')
if num < 0:
    nsaida = num ** 2
    print(f'\033[34mO número informado {num} é negativo, seu valor ao quadrado é: {nsaida}\033[m')
print('Fim....')