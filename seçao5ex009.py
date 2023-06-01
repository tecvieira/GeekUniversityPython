print('=== PROPOSTA DE EMPRÉSTIMO ===')
print()
salario = float(input('Informe o valor do salário: R$ '))
parcela = float(input('Informe o valor da parcela que deseja pagar: R$'))
calculo = (salario * 20) / 100
if parcela > calculo:
    print(f'Empréstimo não concedido valor da parcela maior que R${calculo:.2f}')
    print('Não desista, tente outra vez.')
else:
    print(f'Empréstimo concedido')
    print('Boa Sorte!!!')
