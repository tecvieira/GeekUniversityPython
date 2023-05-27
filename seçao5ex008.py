print('==== Verifique a Nota ====')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota:'))
if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    media = (nota1 + nota2) / 2
    print(f'A média entre as notas {nota1} e nota {nota2} é igual a {media}')
else:
    if nota1 < 0 or nota1 > 10.0:
        print(f'A nota {nota1} informada não é válida.')
    if nota2 < 0 or nota2 > 10.0:
        print(f'A nota {nota2} informada não é válida.')
print('Fim...')
