vetor4 = []
n = 0
print('-' * 55)
print('\033[35m=== ESCOLHA NÚMEROS INTEIROS PAR E CRIE SEU VETOR ===\033[m')
print('-' * 55)
while n < 6:
    num = int(input(f'Informe o {n + 1}º número:  '))
    n += 1
    if num % 2 == 0:
        vetor4.append(num)
    else:
        n -= 1
        print(f'\033[31mERRO! Escolha um número inteiro par.\033[m')
print(f'Elementos escolhidos: {vetor4}')
vetor4.reverse()
print(f'O inverso da opção escolhida é: {vetor4}')
