escolha = 0
num2 = []
num = [3, 7, 4, 8, 9, 5, 14, 19]
print('Determine o valor de X e Y escolhendo na lista surpresa.')
print('-' * 60)
for n in range(1, 3):
    escolha = num[int(input(f'Digite {n}º número entre 0 e {len(num) - 1}: '))]
    num2.append(escolha)
print('=' * 60)
print(f'Lista principal de números; {num}')
print(f'Elemento X = {num2[0]}, elemento Y = {num2[1]} escolhidos na lista principal')
print('=' * 60)
print(f'\033[32mA soma entre os elemntos X e Y escolhidos é: {num2[0] + num2[1]}')
