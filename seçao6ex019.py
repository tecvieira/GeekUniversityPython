numeros = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
num = int(input('Digite um número inteiro entre 100 e 999:'))
if 100 <= num <= 999:
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 100
    print(f'O número {num} é formado por extenso:\033[34m {numeros[c]}, {numeros[d]}, {numeros[u]}')
