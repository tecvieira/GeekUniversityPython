print('**** VEJA QUEM É O MAIOR E A DIFERENÇA ****')
num = int(input('Informe o primeiro número:'))
num2 = int(input('Informe o segundo número: '))
if num > num2:
    dif = num - num2
    print(f'O número {num} é maior que {num2} e a diferença entre eles é {dif}')
elif num2 > num:
    dif = num2 - num
    print(f'O número {num2} é maior que {num} e a diferença entre eles é {dif}')
else:
    print(f'Voçê informou  números iguais, {num} e não há diferença entre eles.')
