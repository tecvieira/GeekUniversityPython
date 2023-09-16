produto = float(input('Informe o valor do produto R$ '))
estado = str(input('Informe a sigla do estado destino: ')).strip().upper()
if estado == 'MG':
    valor_final = produto + (produto * 0.007)
    print(f'O valor final do produto com impostos é R$ {valor_final:.2f}')
elif estado == 'SP':
    valor_final = produto + (produto * 0.12)
    print(f'O valor final do produto com impostos é R${valor_final:.2f}')
elif estado == 'RJ':
    valor_final = produto + (produto * 0.15)
    print(f'O valor final do produto com impostos é R$ {valor_final:.2f}')
elif estado == 'MS':
    valor_final = produto + (produto * 0.08)
    print(f'O valor final do produto com impostos é R$ {valor_final:.2f}')
else:
    print(f'Para este estado não ha impostos agregados Valor final R$ {produto:.2f}')




