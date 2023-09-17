estado = str(input('Informe o estado: ')).strip().upper()
preco = float(input('Informe o valor do produto sem imposto: R$ '))
taxa = ['MG', 'SP', 'RJ', 'MS']
if estado in taxa:
    if estado == 'MG':
        preco_final = preco + (preco * 7/100)
        print(f'Para o estado de {estado} o valor final é : R${preco_final:.2f}')
    if estado == 'SP':
        preco_final = preco + (preco * 12 / 100)
        print(f'Para o estado de {estado} o valor final é : R${preco_final:.2f}')
    if estado == 'RJ':
        preco_final = preco + (preco * 15 / 100)
        print(f'Para o estado de {estado} o valor final é : R${preco_final:.2f}')
    if estado == 'MS':
        preco_final = preco + (preco * 8 / 100)
        print(f'Para o estado de {estado} o valor final é : R${preco_final:.2f}')
else:
    print(f'Para o estado de {estado} o produto não será taxado: R$ {preco:.2f}')
