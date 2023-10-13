def conta_dia(x):
    sal_brut = x * 30.00
    imposto = sal_brut * (8/100)
    sal_liq = sal_brut - imposto
    return print(f'Salário bruto:....R${sal_brut:.2f}\n'
                 f'Imposto.. 8% .....R$ {imposto:.2f}\n'
                 f'Salário Liquido...R${sal_liq:.2f}')


diastrab = float(input('Informe o número de dias trabalhados: '))
conta_dia(diastrab)
