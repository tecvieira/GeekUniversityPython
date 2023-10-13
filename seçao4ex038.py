def calc_aumento(x):
    novo_salario = x + (x * (25/100))
    return print(f'Seu novo salário é R$ {novo_salario:.2f}')


print('Vejá aqui seu novo salário:')
calc_aumento(float(input('Informe seu salário para calcular seu aumento: R$ ')))
