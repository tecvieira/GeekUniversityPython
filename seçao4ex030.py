import requests
from datetime import datetime


# Necessário ter conexão com internet
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
dolar = float(cotacao_dolar)
seu_dinheiro = float(input('Quanto voçe deseja comprar de dolar? '))
convertendo = float(seu_dinheiro / dolar)
print('-=' * 27)
print(f'Atualizado em: {datetime.now()}')
print(f'Cotação atual dolar: {dolar:.2f}')
print(f'\033[34mCom R$ {seu_dinheiro:.2f} é possível comprar USD$ {convertendo:.2f} dolares.\033[m')
print('-=' * 27)
