taxa = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}
valor = float(input('Informe o valor: '))
estado = str(input('Informe o estado: ')).strip().upper()
if estado in taxa.keys():
    print(f'Este estado: {estado} é taxado em {(taxa[estado]) * 100:.2f} % - valor final: R$ {valor + (valor * taxa[estado])}')
else:
    print(f'Para este estado; {estado} não há imposto, valor final:  R$ {valor:.2f}')
