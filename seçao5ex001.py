num = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
if num > num2:
    print(f'O número {num} é maior que {num2}.')
elif num2 > num:
    print(f'O número {num2} é maior que {num}.')
else:
    print(f'Os números {num} e {num2} são iguais.')
print()
print('Fim...')
