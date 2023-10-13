"""
Trabalhando com deltas de data e hora
data_hora = datetime.datetime.now()
print(data_hora) => 2023-09-22 10:45:59.058050

# calculando quanto tempo para um evento acontecer:

import datetime

data_hora = datetime.datetime.now()
print(data_hora) => 2023-09-22 11:03:42.276194
data_aniversario = datetime.datetime(2024, 7, 5, 0)
tempo_evento = data_aniversario - data_hora
print(tempo_evento) => 286 days, 12:56:17.723806

Adicionando um vencimento a data atual (tipo boleto):
import datetime


data_compra = datetime.datetime.now()
print(data_compra) => 2023-09-22 11:12:13.640925
regra_boleto = datetime.timedelta(days=3)
vencimento_boleto = data_compra + regra_boleto
print(vencimento_boleto) => 2023-09-25 11:12:13.640925 # observe que esta com 3 dias a mais.



"""
import datetime


data_compra = datetime.datetime.now()
print(data_compra)
regra_boleto = datetime.timedelta(days=3)
vencimento_boleto = data_compra + regra_boleto
print(vencimento_boleto)
