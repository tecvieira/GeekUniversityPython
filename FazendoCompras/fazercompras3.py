from datetime import datetime
from time import sleep


def cabecalho(msg):
    print('-=' * 15)
    print('       FAZENDO COMPRAS')
    print('-=' * 15)
    print(msg)
    data_hora = datetime.now()
    data_hora_txt = data_hora.strftime('%d/%m/%y - %H:%M\n')
    with open('novacompra3.txt', 'a') as arquivo:
        arquivo.write(f'{msg}\n')
        arquivo.write(data_hora_txt)
    print(data_hora_txt)


def imprimir_txt(msg):
    with open('novacompra3.txt', 'a') as arquivo:
        arquivo.write(f'{msg}\n')


print(cabecalho(input('Nome do Mercado:').upper()))
pergunta = ''
soma_produto = 0
pedido = []
cesta = []
valor1 = 0
qtde = 0
while True:
    produto = str(input('Nome do produto: ')).upper().strip()
    try:
        qtde = float(input('Quantidade: '))
        valor1 = float(input('Valor Unitário: '))
    except (ValueError, NameError):
        print('\033[33m Voçê informou um valor indevido ou usou vígula. Use o ponto para separar centavos. \033[m')
    valor_parcial = valor1 * qtde
    soma_produto += valor_parcial
    cesta = [produto, qtde, valor1, valor_parcial]
    pedido.append(cesta)
    print('--' * 15)
    print(f'\033[33mVALOR PARCIAL R$ {soma_produto:.2f}\033[m')
    print('--' * 15)
    pergunta = str(input('Deseja continuar? S/N')).upper().strip()
    if pergunta == 'N':
        break
print('Finalizando...')
sleep(2)
print('-=' * 15)
print('Produto : Qtde : Vl.Unit : Vl.Total')
imprimir_txt('-=' * 15)
imprimir_txt('Produto/ Qtde/ VUnit/ Total')
for p in pedido:
    imprimir_txt(p)
    print(p)
print('-=' * 15)
imprimir_txt('-=' * 15)
imprimir_txt(f'TOTAL A PAGAR: R$ {soma_produto:.2f}')
print(f'\033[32mVALOR TOTAL A PAGAR = R$ {soma_produto:.2f}\033[m')
