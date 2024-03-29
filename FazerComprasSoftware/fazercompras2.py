from datetime import datetime
from time import sleep


def cabecalho():
    print('-=' * 15)
    print('       FAZENDO COMPRAS')
    print('-=' * 15)
    print(local)
    data_hora = datetime.now()
    data_hora_txt = data_hora.strftime('%d/%m/%y - %H:%M')
    print(data_hora_txt)


local = str(input('Informe nome do Mercado: ')).upper()
print(cabecalho())
pergunta = ''
soma_produto = 0
pedido = []
cesta = []
while True:
    produto = str(input('Nome do produto: ')).upper().strip()
    qtde = float(input('Quantidade: '))
    valor1 = float(input('Valor Unitário: '))
    valor_parcial = valor1 * qtde
    soma_produto += valor_parcial
    cesta = [produto, qtde, valor1, valor_parcial]
    pedido.append(cesta)
    pergunta = str(input('Deseja continuar? S/N')).upper().strip()
    if pergunta == 'N':
        break
print('Finalizando...')
sleep(3)
print('-=' * 15)
print('Produto : Qtde : Preço : Valor')
for p in pedido:
    print(p)
print('-=' * 15)
print(f'Valor total de compras = R${soma_produto:.2f}')
